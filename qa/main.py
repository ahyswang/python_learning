#!/usr/bin/python
# -*- coding:utf-8 -*-

import requests
import socket

# 知识云请求（Get）
def get_yun_info(content):
    try:
        r = requests.get(
            url="http://kcbj.openspeech.cn/service/iss?ver=2.0&open.dialog=true&method=query&usr_id=kctest_music_yx&appid=552b8256&uid=222&province=北京&city=北京",
            params={"text":content}
        )
        return r.content
    except Exception as ex:
        print(str(ex))
        return ''


# 雅典娜请求（Get）
def get_aiui_info(content):
    try:
        r = requests.get(
            url="http://athena.openspeech.cn/athena/iss?ver=3.1&method=query&&uid=u108685870&appid=552b8256&open.dialog=true&topn=1",
            params={"text":content}
        )
        return r.content
    except Exception as ex:
        print(str(ex))
        return ''

def get_qa_info1(content):
    try:
        headers = {
            'Content-Length':'0',
            'Accept-Encoding':'identity',
            'accept':'text/plain',
            'usercontent':content,
            'appid':'59c3bc7e',
            'resource':'#ABNF 1.0 GB2312;mode IND;'
            'meta;#ABNF HEAD-END;$main#userSonglistName=我的歌单;',
            'telephone':'136|13693332459|null|haveCaptain;老六|13693332458|null|haveCaptain;kevin|13693332456|null|haveCaptain;刘鹤8|13693332453|null|haveCaptain;刘鹤|13693332451|null|haveCaptain;@myPhone|15055106666|null;', 
            'cfg':'{"qaCfg":{"newSchedule":"true","newNews":"true"},"tvCfg":{"tvType":"iqiyi","isLink":"true"},"msgCfg":{"namelist":"王瑞|15055105063;贺瑞宾|18709828622;"}};',
            'ServiceType':'aiui_1.0' ,
            'yuninfo':'' ,
            'aiuiinfo':'' ,
            'session':'',
        }
        r = requests.get(url = "http://127.0.0.1:8309/recognizeServer/?type=musicqa", headers=headers)
    except Exception as ex:
        print(str(ex))
        return ''

def get_qa_info(content):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('www.sina.com.cn', 80))
        s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
        buffer = []
        while True:
            d = s.recv(1024)
            if d:
                buffer.append(d)
            else:
                break
        data = b''.join(buffer)
        print data
    except Exception as ex:
        print(str(ex))
    finally:
        s.close()

# import urllib
# params = {'kw': '大大'}
# print urllib.urlencode(params)

# import httplib
# conn = httplib.HTTPSConnection("www.baidu.com")
# conn.request("GET", "/index.html")
# r1 = conn.getresponse()
# print r1.status, r1.reason
# data = r1.read()
# f1 = open("data.bin", "wb")
# f1.write(data)

# def get_http_request(host, url, params, headers):
#     try:
#         conn = httplib.HTTPSConnection(host)
#         conn.request("GET", url, params, headers)
#         response = conn.getresponse()
#         data = response.read()
#         return data
#     except Exception as ex:
#         print(str(ex))
#         return ''

# params = {
#     "ver" : "2.0",
#     "open.dialog" : "true",
#     "method" : "query",
#     "usr_id" : "kctest_music_yx",
#     "appid" : "552b8256",
#     "uid" : "222",
#     "province" : "北京",
#     "city" : "北京",
#     "text" : "查询今天的天气"
# }
# data = get_http_request("kcbj.openspeech.cn", "/service/iss", params, {})
# f11 = open("data.bin1", "wb")
# f11.write(data)



if __name__ == '__main__':
    #yun_info = get_yun_info('查下今天天气')
    #print yun_info
    #aiui_info = get_aiui_info('查下今天天气')
    #print aiui_info
    qa_info = get_qa_info1('设置上午9点的闹钟')
    print qa_info
