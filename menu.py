# -*- coding: utf-8 -*-
import re
import urllib.request

def createMenu():  
    #未认证不支持
    url = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=9eAhCuIkyQbRWTXtLjgQ8vFSyWbapUHbClWZ2SwFivIu7Rfjg2IoYX-g_tzhyKWdqI7JmKy0Mf4bcqwsw6YyGowUJvgvcRT9NV9yLR4E1CxyOMKqb6qkQdZFEc38oFoYBNJbAAAEQM"  
    values = {
        "button":[
        {
            "type":"pic_photo_or_album",
            "name":"人脸年龄识别",
            "key": "rselfmenu_0_0"
        }],
        "button":[
        {
            "type":"view",
            "name":"搜索说明",
            "url":"http://mp.weixin.qq.com/mp/homepage?__biz=MzI3MjIxNTI4Nw==&hid=1&sn=1bfe4dc0744e0f5e1df172ba72cad316#wechat_redirect"
        }]
    }
      
    data = urllib.parse.urlencode(values).encode('utf-8')
    req = urllib.request.Request(url=url,data=data,method="POST")
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf8')
    print(result)
    return result