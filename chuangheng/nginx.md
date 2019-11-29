1.代理方式
添加一个 server的节点

listen 80 监听80端口

server_name  域名的地址  如果访问的是weixin.wangnian.com就走代理 

location  /   访问根路径就走代理

代理可以直接是服务器的位置 也可以代理请求地址

直接访问服务器的位置 

 root   /data/abc/;
 index  index.html index.htm;
 
 proxy_pass配置为： 代理的地址