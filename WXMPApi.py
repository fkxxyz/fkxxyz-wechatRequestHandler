#!/usr/bin/env python


wx_api_url = 'https://api.weixin.qq.com'

import requests
import urllib
import json

def get_access_token(appid, secret):
    # 获取 access_token
    url = wx_api_url + '/cgi-bin/token?grant_type=client_credential&appid='+appid+'&secret='+secret
    result = requests.get(url)
    json_result = json.loads(json_result)
    if "errcode" in json_result.content:
        if json_result["errcode"] != 0:
            return json_result

    if "access_token" not in json_result:
        return json_result

    return json_result["access_token"]


class api:
    def __init__(self, access_token):
        self.access_token = access_token

    def cgi_bin_get(self, type_str, url_param = {}):
        url_param["access_token"] = self.access_token
        url = wx_api_url + '/cgi-bin/' + type_str +'?' + urllib.parse.urlencode(url_param)
        result = requests.get(url)
        json_result = json.loads(result.content)
        return json_result

    def cgi_bin_post(self, type_str, data = None, files = None):
        url = wx_api_url + '/cgi-bin/' + type_str +'?access_token=' + self.access_token
        result = requests.post(url, data = data, files = files)
        json_result = json.loads(result.content)
        return json_result

class menu_api(api):

    def create(self, data):
        # 创建接口
        return self.cgi_bin_post("menu/create", data)
        
    def get_current_selfmenu_info(self):
        # 查询接口
        return self.cgi_bin_get("get_current_selfmenu_info")

    def delete_all(self):
        # 删除接口
        return self.cgi_bin_get("menu/delete")

    def add_conditional(self, data):
        # 创建个性化菜单
        return self.cgi_bin_post("menu/addconditional", data)

    def del_conditional(self, data):
        # 删除个性化菜单
        return self.cgi_bin_post("menu/delconditional", data)

    def trymatch(self, data):
        # 测试个性化菜单匹配结果
        return self.cgi_bin_post("menu/trymatch", data)

    def get(self):
        # 获取自定义菜单配置
        return self.cgi_bin_get("menu/get")



