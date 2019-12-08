#!/bin/python3
#-*- encoding:utf-8 -*-

import random
import calcPython

def MakeTestTextMsgRecv(text):
    return {
        'ToUserName': 'client_user',
        'FromUserName': 'server_user',
        'CreateTime': 123123,
        'MsgType': 'text',
        'Content': text,
        'MsgId': '10101010',
    }


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
            
            # 计算器帮助
            if text.lower() == "help" or text == "帮助":
                return self.textMsg(calcPython.getHelp())
            
            # 计算器帮助
            if text.lower() == "func" or text == "函数":
                return self.textMsg(calcPython.getFuncHelp())
            
            # 计算表达式
            if calcPython.isValid(text):
                ret = calcPython.calc_t(text, 0.5)
                if ret is None:
                    return self.textMsg("计算量太大啦人家承受不住 ～.～")
                return self.textMsg(ret)
            
            # 反转字符串
            return self.textMsg(text[::-1])

        # 事件类消息
        if self.recv_dict['MsgType'] == 'event':
            event = self.recv_dict['Event']
            
            # 订阅事件
            if event == "subscribe":
                return self.textMsg("你来啦，终于等到你啦～\n我现在只能当计算器给你用哦，来试试吧。\n发送“帮助”给我我教你怎么用。")

        # 其它消息
        msg_list = [
            '你发的什么呢，我暂时理解不了。',
            '我暂时理解不了此类消息，怎么办'
        ]
        return self.textMsg(msg_list[random.randint(0,len(msg_list)-1)])

if __name__ == '__main__':
    import sys
    
    # 检查参数长度
    if len(sys.argv) < 2:
        exit(1)

    recv = sys.argv[1]
    print(fkxxyzMsgResponse(MakeTestTextMsgRecv(recv)).response()[4][1])
    
    
    

