#!/usr/bin/env python

import requests
import base64
import random
import sys


def getPicText_bdOcr(pic_binary, type_index = 1):
    '''
        利用百度 ocr 接口识别文字
        pic_binary  是图片文件的二进制数据
        type_index  是百度提供的识别类型 0 表示一般识别， 1 表示精准识别
        如果成功，则返回识别出的文字字符串
        如果出错，则返回错误信息
    '''

    # 获取 appid 的 cookie
    cookie = requests.get('http://ai.baidu.com/tech/ocr/general').headers["Set-Cookie"]
    baiduid_cookie = cookie[:cookie.find(';')]

    # 准备头部
    headers = {
        'Cookie': baiduid_cookie,
        'Referer': "http://ai.baidu.com/tech/ocr/general"
    }

    # 准备数据
    post_type_l = ['general_location' , 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate']
    if type_index is None:
        post_type = post_type_l[random.randint(0, len(post_type_l) - 1)]  # 两个类型随机选个类型
    else:
        post_type = post_type_l[type_index]

    post_data = {
        'type': post_type,
        'detect_direction': 'false',
        'image_url': None,
        'image': 'data:image/jpeg;base64,' + base64.b64encode(pic_binary).decode('utf-8'),
        'language_type': 'CHN_ENG'
    }

    # 发送 post 请求
    response = requests.post('http://ai.baidu.com/aidemo', data = post_data, headers = headers)

    # 解析请求结果
    response_json = response.json()
    errno = response_json['errno']
    if errno != 0:
        return '我这边出错啦！' + response_json['msg']

    data = response_json['data']
    words_result_num = data['words_result_num']
    words_result = data['words_result']

    result = ''
    for w in words_result:
        result += w['words'] + '\n'
    return result.strip()

if __name__ == '__main__':
    # 检查参数长度
    if len(sys.argv) < 2:
        sys.stderr.write('缺少文件位置参数\n')
        exit(1)

    pic_binary = open(sys.argv[1], 'rb').read()
    print(getPicText_bdOcr(pic_binary, 1))



