# -*- coding: UTF-8 -*-

import time
import random
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scrapy.selector import Selector
from scrapy.http import TextResponse


class XhsCrawler(object):
    def __init__(self):
        self.browser, self.action = self._init_driver()
        self.books_id = []
        self.users_profile = []


    def _init_driver(self):
        """
        初始化browser和action
        """
        options = Options()
        options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
        options.add_argument('--incognito')
        browser = webdriver.Chrome(options = options)
        action = ActionChains(browser)

        return browser, action
    

    def _log_and_search(self, key_word):
        """
        打开小红书首页，进行半自动化登录，搜索关键词，并进入到图文页面，按热度排序
        """
        self.browser.get('https://www.xiaohongshu.com/explore')
        time.sleep(10)
        url = f'https://www.xiaohongshu.com/search_result?keyword={key_word}&source=web_explore_feed'
        self.browser.get(url)
        time.sleep(10)
        self.browser.find_element(By.XPATH, '//*[@id="search-type"]/div/div/div[2]').click()

        time.sleep(3)

        element = self.browser.find_element(By.XPATH, '//*[@id="global"]/div[2]/div[2]/div/div[1]/div[2]')
        self.action.move_to_element(element).perform()
        menu = self.browser.find_element(By.CLASS_NAME, 'dropdown-items')
        option = menu.find_element(By.XPATH, f'/html/body/div[4]/div/li[3]')
        option.click()
    

    def _get_list_info(self, nums):
        """
        获取搜索页面的笔记id列表和对应的user
        """
        def _get_book_id_from_page():
            response = TextResponse(url = self.browser.current_url, body = self.browser.page_source, encoding = 'utf-8')
            selector = Selector(response)
            divs = selector.xpath('//div[contains(@class, "feeds-container")]/section/div')
            for div in divs:
                try:
                    book_id = div.xpath('./div/a/@href').extract_first().split('/')[-1]
                    user_profile = div.xpath('./div/div/a/@href').extract_first()
                    if book_id in self.books_id: continue
                    self.books_id.append(book_id)
                    self.users_profile.append(user_profile)
                    time.sleep(random.uniform(0.3, 0.6))
                except: pass

        while(len(self.books_id) < nums):
            if '- THE END -' in self.browser.page_source:
                print(f"笔记数量不足{nums}条，已到达最后一页，共{len(self.books_id)}条笔记")
                break
    
            _get_book_id_from_page()
            time.sleep(random.uniform(0.3, 0.6))
            self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(random.uniform(3, 6))
    

    def _get_info_from_pages(self, file_name):
        """
        从每个笔记页面中获取信息，内容包括：
            标题、正文、链接、发布时间、点赞数、收藏数、评论数、创作者昵称、创作者id、粉丝量
        """
        df = pd.DataFrame(columns=["user name", "user id", "fans count", "title", "content", "url", "date", "like count", "collect count", "comment count"]) 
        def _get_info_from_page(book_id, user_profile):
            time.sleep(random.uniform(5, 8))
            # 链接
            page_url = f"https://www.xiaohongshu.com/explore/{book_id}"
            self.browser.get(page_url)
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@name="description"]')))
            time.sleep(random.uniform(2, 4))
            response = TextResponse(url = self.browser.current_url, body = self.browser.page_source, encoding = 'utf-8')
            selector = Selector(response)

            # 标题
            # title = selector.xpath('//div[contains(@id, "detail-title")]/text()').extract_first()
            title = selector.xpath('//*[@name="og:title"]/@content').extract_first()

            # 正文
            content = selector.xpath('//*[@name="description"]/@content').extract_first()

            # 发布时间
            date = selector.xpath('//span[contains(@class, "date")]/text()').extract_first().split()[0]

            # 点赞数
            # like_count = selector.xpath('//span[contains(@class, "like-wrapper")]//span[contains(@class, "count")]/text()').extract_first()
            like_count = selector.xpath('//*[@name="og:xhs:note_like"]/@content').extract_first()

            # 收藏数
            # collect_count = selector.xpath('//span[contains(@class, "collect-wrapper")]//span[contains(@class, "count")]/text()').extract_first()
            collect_count = selector.xpath('//*[@name="og:xhs:note_collect"]/@content').extract_first()

            # 评论数
            # chat_count = selector.xpath('//span[contains(@class, "chat-wrapper")]//span[contains(@class, "count")]/text()').extract_first()
            comment_count = selector.xpath('//*[@name="og:xhs:note_comment"]/@content').extract_first()

            # 创作者昵称
            username = selector.xpath('//span[contains(@class, "username")]/text()').extract_first()
            
            # user页面

            user_url = f"https://www.xiaohongshu.com{user_profile}"
            self.browser.get(user_url)
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@name="description"]')))
            time.sleep(random.uniform(2, 4))
            response = TextResponse(url = self.browser.current_url, body = self.browser.page_source, encoding = 'utf-8')
            selector = Selector(response)

            # 创作者id
            user_id = selector.xpath('//span[@class="user-redId"]/text()').extract_first().split("：")[-1]

            # 粉丝量
            fans_count = selector.xpath('//*[@class="data-info"]/div[1]/div[2]/span[@class="count"]/text()').extract_first()
            return pd.DataFrame([[username, user_id, fans_count, title, content, page_url, date, like_count, collect_count, comment_count]], columns = df.columns)

        with open(f"{file_name}.csv", 'w', encoding = "utf_8_sig", newline = '') as f:
            df.to_csv(f, header = True, index = False, encoding = "utf_8_sig")
            
            for i in range(len(self.books_id)):
                try:
                    row = _get_info_from_page(self.books_id[i], self.users_profile[i])
                    row.to_csv(f, mode = 'a', header = False, index = False, encoding = "utf_8_sig")
                except: pass

    def forward(self):
        key_words = ["NBA"]

        for key_word in key_words:
            self.books_id.clear()
            self.users_profile.clear()
            self._log_and_search(key_word)
            self._get_list_info(10000)
            self._get_info_from_pages(key_word)

if __name__ == "__main__":
    crawler = XhsCrawler()
    crawler.forward()


