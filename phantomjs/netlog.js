"use strict";
var page    = require('webpage').create(),
    system  = require('system'),
    resources,
    path,
    filter,
    address;


if (system.args.length === 1) {
    console.log('Usage: netlog.js <some URL>');
    phantom.exit(1);
} else {
    address     = system.args[1];
    resources   = [];
    path        = system.args[2];
    filter      = system.args[3];

    page.onResourceRequested = function (req) {
        try {
            var _url = JSON.parse(JSON.stringify(req, undefined, 4)).url
            console.log("hook_url: " + _url);

            if (_url.indexOf(filter) > 0) {
                resources.push(_url)
            }

        }catch(e) {
            console.log(e)
        }  
    };

    page.open(address, function (status) {
        if (status !== 'success') {
            console.log('FAIL to load the address');
        }
        window.setTimeout(function () {
            try {
                var fs = require('fs');
                
                console.log("建立索引文件 ...")

                while (resources.length > 0) {
                    var url = resources.shift();
                    fs.write(path, url + "\r\n", 'w+');

                    console.log("写入: " + url)
                }
            } catch(e) {
                console.log(e)
            }

            console.log("索引文件写入完毕 ...")
            phantom.exit(1);
        }, 10000);
    });
}
