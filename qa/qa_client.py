#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket
import json
import sys 
import requests

#Python默认编码是ascii,这里设置默认编码为utf-8
#Python打印为乱码，是因为控制默认编码是gbk
reload(sys) 
sys.setdefaultencoding('utf-8') 

DATA_FORMAT = \
       'POST /recognizeServer/?type=musicqa HTTP/1.1\r\n' \
       'Accept-Encoding:identity\r\n' \
       'Content-Length: 0\r\n'\
       'usercontent:%s\r\n'\
       'appid:59c3bc7e\r\n' \
       'resource:#ABNF 1.0 GB2312;mode IND;' \
       'meta;#ABNF HEAD-END;$main#userSonglistName=我的歌单;\r\n' \
       'telephone:136|13693332459|null|haveCaptain;老六|13693332458|null|haveCaptain;kevin|13693332456|null|haveCaptain;刘鹤8|13693332453|null|haveCaptain;刘鹤|13693332451|null|haveCaptain;@myPhone|15055106666|null;\r\n' \
       'cfg:{"qaCfg":{"newSchedule":"true","newNews":"true"},"tvCfg":{"tvType":"iqiyi","isLink":"true"},"msgCfg":{"namelist":"王瑞|15055105063;贺瑞宾|18709828622;"}};\r\n'\
       'ServiceType:aiui_1.0\r\n' \
       'yuninfo:%s\r\n' \
       'aiuiinfo:%s\r\n' \
       'session:%s\r\n\r\n'

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
        return 9

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
        return 9

# QA请求(POST)
def get_qa_info(content):
    yuninfo = get_yun_info(content)
    aiuiinfo = get_aiui_info(content)
    session = ""
    data = DATA_FORMAT%(content,yuninfo,aiuiinfo,session)
    return post_socket('127.0.0.1', 8309, data)

def post_socket(host, port, data):
    try:
        socket.setdefaulttimeout(5)
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        s.send(data.encode('gbk')) # utf-8 => gbk
        #获得请求buffer数据并结果转成json
        buffer = ''  
        while True:
            d = s.recv(7000)
            if d:
               buffer+=d
            else:
                break
        buffer = buffer.decode('gbk') #gbk => utf-8
        return buffer
    except Exception as ex:
        print(str(ex))
        return 9
    finally:
        s.close()

if __name__ == '__main__':
    result = get_qa_info("设置明天上午的闹钟")
    yun1 = get_yun_info('查下今天天气')
    aiui1 = get_aiui_info('查下今天天气')