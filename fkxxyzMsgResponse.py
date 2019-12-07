#!/bin/python3
#-*- encoding:utf-8 -*-


class fkxxyzMsgResponse:
    def response(recv_dict):
        '''
            recv_dict 接收的字典，对应开发者文档的xml
            返回要回应的元组列表，对应开发者文档的xml
        '''
        if 'MsgType' not in recv_dict:
            return None
        if recv_dict['MsgType'] == 'text':
            return [
                ('ToUserName', recv_dict['FromUserName']),
                ('FromUserName', recv_dict['ToUserName']),
                ('CreateTime', int(recv_dict['CreateTime'])),
                ('MsgType', recv_dict['MsgType']),
                ('Content', recv_dict['Content'][::-1])
            ]
        else:
            return [
                ('ToUserName', recv_dict['FromUserName']),
                ('FromUserName', recv_dict['ToUserName']),
                ('CreateTime', int(recv_dict['CreateTime'])),
                ('MsgType', 'text'),
                ('Content', "你发的什么啊，我看不懂哦～")
            ]
    
    

