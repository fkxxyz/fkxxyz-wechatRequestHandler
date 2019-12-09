#!/bin/python3
#-*- encoding:utf-8 -*-

import random
import requests


import calcPython
import baiduOcr

def MakeTestTextMsgRecv(text):
    return {
        'ToUserName': 'client_user',
        'FromUserName': 'server_user',
        'CreateTime': 123123,
        'MsgType': 'text',
        'Content': text,
        'MsgId': '10101010',
    }


hello_msg = """你来啦，终于等到你啦～
我现在可以当你的计算器哦，把算式发给我我就可以帮你算算，来试试吧。
发送“帮助”给我我教你具体格式。

还可以给我发图片，我可以帮你提取出图片里的文字，比如拍照书本给我我都给你转成文字可以复制的哦。"""


class fkxxyzMsgResponse:
    def __init__(self, recv_dict):
        self.recv_dict = recv_dict

    def textMsg(self, text):
        return [
            ('ToUserName', self.recv_dict['FromUserName']),
            ('FromUserName', self.recv_dict['ToUserName']),
            ('CreateTime', int(self.recv_dict['CreateTime'])),
            ('MsgType', 'text'),
            ('Content', text)
        ]

    def response(self):
        '''
            recv_dict 接收的字典，对应开发者文档的xml
            返回要回应的元组列表，对应开发者文档的xml
        '''
        if 'MsgType' not in self.recv_dict:
            return None

        # 文本类消息
        if self.recv_dict['MsgType'] == 'text':
            text = self.recv_dict['Content'].strip()
            
            # 欢迎语
            if text.lower() == "hello" or text == "你好":
                return self.textMsg(hello_msg)
            
            # 计算器帮助
            if text.lower() == "help" or text == "帮助":
                return self.textMsg(calcPython.getHelp())
            
            # 计算器详细帮助
            if text.lower() == "detail" or text == "详细":
                return self.textMsg(calcPython.getDetailHelp())
            
            # 计算器帮助
            if text.lower() == "func" or text == "函数":
                return self.textMsg(calcPython.getFuncHelp())
            
            # 计算表达式
            if calcPython.isValid(text):
                ret = calcPython.calc_t(text, 0.5)
                if ret is None:
                    return self.textMsg("计算量太大啦人家承受不住 ～.～")
                return self.textMsg(ret)
                
            if text == '【收到不支持的消息类型，暂无法显示】':
                return self.textMsg(self.unsupportMsg())
                
            # 反转字符串
            return self.textMsg(text[::-1])

        # 事件类消息
        if self.recv_dict['MsgType'] == 'event':
            event = self.recv_dict['Event']
            
            # 订阅事件
            if event == "subscribe":
                return self.textMsg(hello_msg)

        # 图片类信息
        if self.recv_dict['MsgType'] == 'image':
            pic_url = self.recv_dict['PicUrl']
            pic_data = requests.get(pic_url).content
            ret = baiduOcr.getPicText_bdOcr(pic_data)
            if type(ret) != str:
                return self.textMsg("我这边识别图片出问题了，过段时间再来试试吧")
            if len(ret) == 0:
                msg_list = [
                    "什么都没识别到",
                    "图片里可能没有文字",
                    "我没看到图里有文字",
                    "唉，我找不到图里的文字，你帮我看看吧"
                ]
                return self.textMsg(msg_list[random.randint(0,len(msg_list)-1)])
            return self.textMsg(ret)
        return self.textMsg(self.unsupportMsg())

    def unsupportMsg(self):
        # 其它消息
        msg_list = [
            '你发的什么呢，我暂时理解不了。',
            '我暂时理解不了此类消息，怎么办'
        ]
        return msg_list[random.randint(0,len(msg_list)-1)]

if __name__ == '__main__':
    import sys
    
    # 检查参数长度
    if len(sys.argv) < 2:
        exit(1)

    recv = sys.argv[1]
    print(fkxxyzMsgResponse(MakeTestTextMsgRecv(recv)).response()[4][1])
    
    
    

