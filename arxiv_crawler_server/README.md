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

## Proxy

Nginx反向代理配置：

```nginx
map $http_upgrade $connection_upgrade {
    default upgrade;
    ''      close;
}

server {
        listen  80;
        listen  [::]:80;
        server_name  you_web_domain;
        client_max_body_size 100M;
        location / {
            proxy_pass http://127.0.0.1:8501/;
            proxy_buffer_size 1024k; 
            proxy_buffers 16 1024k; 
            proxy_busy_buffers_size 2048k;
            proxy_temp_file_write_size 2048k; 
            proxy_http_version 1.1;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header  X-Real-IP  $remote_addr;
            proxy_set_header  X-Forwarded-Proto $scheme;
            proxy_set_header Upgrade $http_upgrade; # 非常重要
            proxy_set_header Connection $connection_upgrade; # 非常重要
            proxy_set_header Host $host;
            proxy_redirect off; # 非常重要
        }
}
```