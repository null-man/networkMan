#-*-coding:utf-8-*-

import requests
import os

class Spider:
    def savePageInfo(self, url, path_root):
            #
            # url例:
            #   http://szhong.4399.com/4399swf/upload_swf/ftp20/ssj/20161101/jf2/css/reset.css

            file = requests.get(url.strip())
            # 文件名 使用域名切割定位出在本地存放的位置 一般定位在域名后面即可
            file_name = ((url.split(domain)[1])[::-1].split("/")[0])[::-1].strip()

            # 去除文件名的路径
            path = (url.split(domain)[1]).split(file_name)[0]

            path = path_root + path
            # 创建路径
            if not os.path.isdir(path):
                os.makedirs(path)


            path = path + file_name
            print "写入:" + path

            # 写入数据
            fp = open(path, 'wb')
            fp.write(file.content)

            fp.close()

    def createFile(self, path):
        f = open(path, 'w')
        f.close()

        print "文件成功: " + path


    def createDir(self, dir):
        # 创建路径
        if not os.path.isdir(dir):
            os.makedirs(dir)
        print "目录创建成功: " + dir






# 调用规则：phantomjs的全路径 netlog.js的全路径 参数一[url] 参数二[本地index路径]
cmd = "/Users/edison/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs /Users/edison/Downloads/phantomjs-2.1.1-macosx/examples/netlog.js "
url = "http://sda.4399.com/4399swf/upload_swf/ftp19/ssj/20160926/b3/index.htm "
txt_path_head = '/Users/edison/Desktop/temp/3/'
txt_path_suffix = "index.txt"
txt_path = txt_path_head + txt_path_suffix

# 解析域名
domain = '4399.com/'


# 初始化爬虫
spider = Spider()
#创建目录
spider.createDir(txt_path_head)
# 创建索引文件
spider.createFile(txt_path)

# 执行phantomjs 命令
p=os.popen(cmd + url + txt_path)
print p.read()

# 读取network
for url in open(txt_path):
    try:
        print "当前扒取url:" + url
        spider.savePageInfo(url, txt_path_head, domain)
    except Exception,e:
        print "异常了:" + str(e)


