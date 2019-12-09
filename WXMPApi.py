#!/bin/python3


wx_api_url = 'https://api.weixin.qq.com'

import requests
import json

def get_access_token(appid, secret):
    url = wx_api_url + '/cgi-bin/token?grant_type=client_credential&appid='+appid+'&secret='+secret
    result = requests.get(url)
    json_result = json.loads(json_result)
    if "errcode" in json_result.content:
        if json_result["errcode"] != 0:
            return json_result

    if "access_token" not in json_result:
        return json_result

    return json_result["access_token"]

class menu_api:
    def __init__(self, access_token):
        self.access_token = access_token

    def get(self):
        url = wx_api_url + '/cgi-bin/get_current_selfmenu_info?access_token=' + self.access_token
        result = requests.get(url)
        json_result = json.loads(result.content)
        return json_result

    def delete_all(self):
        url = wx_api_url + '/cgi-bin/menu/delete?access_token=' + self.access_token
        result = requests.get(url)
        json_result = json.loads(result.content)
        return json_result

    def put(self):
        



