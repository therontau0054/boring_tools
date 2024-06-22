# Arxiv Crawler Server

此为部署到服务器上的版本，核心功能与arxiv_crawler一样，使用[Streamlit](https://streamlit.io/)作为前端框架，将爬取到的论文信息展示在网页上，点击[此处](http://mypapers.theron.love)可以访问，较git action部署的版本，该版本的关键词和论文数量会更多、更新频率也会更快。

## TODO
- [x] 页面自动更新：检测到新的论文后自动更新页面
- [x] Docker部署
- [ ] LLM分析
- [ ] ...

## Usage

```bash
cd arxiv_crawler_server
docker build -t arxiv_crawler:001 .
docker run -d --name "arxiv_crawler" -p 8501:8501 arxiv_crawler:001
```