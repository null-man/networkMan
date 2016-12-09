"use strict";
var page    = require('webpage').create(),
    system  = require('system'),
    index_path,
    address;


// 遍历network记录到文件
var saveNetwork = function(urls, path, callbackFinal) {
    var retrieve;

    retrieve = function() {
        var url;
        if (urls.length > 0) {
            url = urls.shift();

            // 保存文件
            saveFile(path, url)
            
            // 递归
            retrieve()
        } else {
            return callbackFinal();
        }
    };

    return retrieve();
};

// 写入文件
var saveFile = function(path, url) {
    try {
        var fs = require('fs');
        fs.write(path, url + "\r\n", 'w+');
    } catch(e) {
        console.log(e)
    }
    
}



if (system.args.length === 1) {
    console.log('Usage: netlog.js <some URL>');
    phantom.exit(1);
} else {
    address         = system.args[1];
    index_path      = system.args[2];
    page.resources  = []

    page.onResourceRequested = function (req) {
        _url = JSON.parse(JSON.stringify(req, undefined, 4)).url

        // 只获取该域名的数据
        if (_url.indexOf('4399.com') > 0) {
            page.resources.push(_url)
            console.log("网络请求: " + _url);
        }
    };

    page.open(address, function (status) {
        if (status !== 'success') {
            console.log('FAIL to load the address');
        } else {
            // 保存index.html文件
            saveFile(index_path, address)

            // 遍历保存network
            saveNetwork(page.resources, index_path, function(){
                console.log("========== [网络请求收集完成] ==========")
                return phantom.exit();
            });   
        }
    });
}
