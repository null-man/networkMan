# networkMan

### 技术核心
python + phantomjs
### 功能
爬取nwtwork所有记录
### 使用方向
爬取H5游戏等

### 使用技巧

记得后面要留空格做拼接命令
cmd = "phantomjs全路径 netlog.js全路径 " 

一样留空格
url = "被访问的url（比如H5游戏） "

最后加/
txt_path_head = '本地存放路径'
txt_path_suffix = "index.txt"
txt_path = txt_path_head + txt_path_suffix

解析域名（为了还原文件的位置）
domain = '4399.com/'

初始化爬虫
spider = Spider()
创建目录
spider.createDir(txt_path_head)
创建索引文件
spider.createFile(txt_path)

提取所有network记录
p=os.popen(cmd + url + txt_path)
print p.read()

遍历所有的network记录并爬取
for url in open(txt_path):
    try:
        print "当前扒取url:" + url
        spider.savePageInfo(url, txt_path_head, domain)
    except Exception,e:
        print "异常了:" + str(e)
        
        
### 说明
当前版本network异步请求无法抓到，不知道是不是phantomjs的问题，有待研究。
当前版本已经非常能够非常快速的爬取一款H5游戏

### 联系作者
邮箱：635384073@qq.com
