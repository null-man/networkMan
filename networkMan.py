#-*-coding:utf-8-*-

import requests
import os
import time

class NetworkMan:
    def __init__(self, phantomjs, netlogjs, url, path, split = None, filter_word = None):
        # phantomjs 路径
        self.phantomjs = phantomjs
        
        # netlog 路径
        self.netlogjs = netlogjs
        
        # 请求的url
        self.url = url

        # 默认过滤url为当前url域名
        if split == None:
            split = (url.split(".com/")[0] + ".com").split("http://")[1]

        # 切割点(一般以域名为切割点, 用户还原目录结构)
        self.split = split + "/"

        # 默认network 拦截域名为当前url域名
        if filter_word == None:
            filter_word = split

        # 本地存放路径
        self.root_path = path + "/" +  str(int(time.time())) + "/"
        self.path = self.root_path + "index.txt"

        # 创建索引文件
        self.createFile(self.path)

        # 获取 network所有记录的命令
        self.cmd = " ".join([self.phantomjs, self.netlogjs, self.url, self.path, filter_word])

        print "cmd: " + self.cmd

    # 创建多级目录以及文件
    def createFile(self, path, content = None):
        if not os.path.isdir(path):
            file = path[::-1].split('/')[0][::-1]
            dir = path.split(file)[0]

            # 先创建目录
            os.makedirs(dir)
            print "目录创建完成: " + dir

            # 再创建文件
            f = open(path, 'wb')
            if content != None:
                f.write(content)
            f.close()
            print "文件创建完成: "+ path

    # 所有network记录写入index文件
    def getNetLog(self):
        # 执行phantomjs 命令
        print "开始爬取 network 记录..."
        p = os.popen(self.cmd)
        print p.read()

    # 读取所有network记录 爬取文件
    def savePageInfo(self, url):
            # 去除空格
            file = requests.get(url.strip())
            # 本地文件名
            file_name = ((url.split(self.split)[1])[::-1].split("/")[0])[::-1].strip()
            # 本地去除文件名的路径
            path = (url.split(self.split)[1]).split(file_name)[0]
            # 本地路径
            path = self.root_path + path

            print "写入目录:" + path

            # 创建路径
            if not os.path.isdir(path):
                os.makedirs(path)
                print "创建目录成功:" + path

            # 写入数据
            fp = open(path + file_name, 'wb')
            fp.write(file.content)
            fp.close()
            print "创建文件成功:" + path


    # 开始工作
    def do(self):
        # 获取network记录
        self.getNetLog()

        # 读取network记录
        for url in open(self.path):
            try:
                print "当前爬取url: " + url
                self.savePageInfo(url)
            except Exception,e:
                print "出现异常: " + str(e)









phantomjs = "/Users/edison/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs"
netlogjs  = "/Users/edison/Downloads/phantomjs-2.1.1-macosx/examples/netlog0.js"
url       = "http://www.17sucai.com/preview/161350/2016-05-17/products-WB098M36S/index.html"
path      = "/Users/edison/Desktop/temp"


# 初始化爬虫
networkMan = NetworkMan(phantomjs, netlogjs, url, path)
networkMan.do()




