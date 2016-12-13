# networkMan

### 核心技术
python + phantomjs

### 文件下载
phantomjs: http://phantomjs.org/ 版本2.1.1<br/>
python: https://www.python.org/ 版本2.7.8 

### 功能
爬取network所有记录
### 使用方向
爬取H5游戏等

### 使用技巧
    phantomjs 的物理路径
    phantomjs = "/Users/edison/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs"
    
    netlogjs 的物理路径
    netlogjs  = "/Users/edison/Downloads/phantomjs-2.1.1-macosx/examples/netlog.js"
    
    需要爬取的url
    url       = "http://sda.4399.com/4399swf/upload_swf/ftp19/ssj/20160926/b3/index.htm"
    
    本地存放物理路径
    path      = "/Users/edison/Desktop/temp"
    

    # 初始化爬虫
    networkMan = NetworkMan(phantomjs, netlogjs, url, path)
    networkMan.do()




### 说明
当前版本无法抓取到network异步请求，不知道是不是phantomjs的问题，有待研究。<br/>
networkMan主要是提供了一项解决方案。<br/>
因为我查找过很多次，发现没有类似的解决方案或者框架，于是自己动手写了一个，希望可以帮助有需要的人。<br>
当前版本重构了使用方式，简化了开发者的操作思路，只需要填写对应的参数即可。<br/>


### V1.2 更新日志
1、修复部分bug
2、重构部分代码
3、切割点添加了默认值，减去用户的操作




### 联系作者
邮箱：635384073@qq.com