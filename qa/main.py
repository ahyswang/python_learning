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

if __name__ == '__main__':
    #yun_info = get_yun_info('查下今天天气')
    #print yun_info
    #aiui_info = get_aiui_info('查下今天天气')
    #print aiui_info
    qa_info = get_qa_info('查下今天天气')
    print qa_info