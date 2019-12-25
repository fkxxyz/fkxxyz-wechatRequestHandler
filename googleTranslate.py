#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import json
import execjs
import urllib
import requests


lang_dict = {
"source_code_name":{
    "auto":"检测语言",
    "sq":"阿尔巴尼亚语",
    "ar":"阿拉伯语",
    "am":"阿姆哈拉语",
    "az":"阿塞拜疆语",
    "ga":"爱尔兰语",
    "et":"爱沙尼亚语",
    "eu":"巴斯克语",
    "be":"白俄罗斯语",
    "bg":"保加利亚语",
    "is":"冰岛语",
    "pl":"波兰语",
    "bs":"波斯尼亚语",
    "fa":"波斯语",
    "af":"布尔语(南非荷兰语)",
    "da":"丹麦语",
    "de":"德语",
    "ru":"俄语",
    "fr":"法语",
    "tl":"菲律宾语",
    "fi":"芬兰语",
    "fy":"弗里西语",
    "km":"高棉语",
    "ka":"格鲁吉亚语",
    "gu":"古吉拉特语",
    "kk":"哈萨克语",
    "ht":"海地克里奥尔语",
    "ko":"韩语",
    "ha":"豪萨语",
    "nl":"荷兰语",
    "ky":"吉尔吉斯语",
    "gl":"加利西亚语",
    "ca":"加泰罗尼亚语",
    "cs":"捷克语",
    "kn":"卡纳达语",
    "co":"科西嘉语",
    "hr":"克罗地亚语",
    "ku":"库尔德语",
    "la":"拉丁语",
    "lv":"拉脱维亚语",
    "lo":"老挝语",
    "lt":"立陶宛语",
    "lb":"卢森堡语",
    "ro":"罗马尼亚语",
    "mg":"马尔加什语",
    "mt":"马耳他语",
    "mr":"马拉地语",
    "ml":"马拉雅拉姆语",
    "ms":"马来语",
    "mk":"马其顿语",
    "mi":"毛利语",
    "mn":"蒙古语",
    "bn":"孟加拉语",
    "my":"缅甸语",
    "hmn":"苗语",
    "xh":"南非科萨语",
    "zu":"南非祖鲁语",
    "ne":"尼泊尔语",
    "no":"挪威语",
    "pa":"旁遮普语",
    "pt":"葡萄牙语",
    "ps":"普什图语",
    "ny":"齐切瓦语",
    "ja":"日语",
    "sv":"瑞典语",
    "sm":"萨摩亚语",
    "sr":"塞尔维亚语",
    "st":"塞索托语",
    "si":"僧伽罗语",
    "eo":"世界语",
    "sk":"斯洛伐克语",
    "sl":"斯洛文尼亚语",
    "sw":"斯瓦希里语",
    "gd":"苏格兰盖尔语",
    "ceb":"宿务语",
    "so":"索马里语",
    "tg":"塔吉克语",
    "te":"泰卢固语",
    "ta":"泰米尔语",
    "th":"泰语",
    "tr":"土耳其语",
    "cy":"威尔士语",
    "ur":"乌尔都语",
    "uk":"乌克兰语",
    "uz":"乌兹别克语",
    "es":"西班牙语",
    "iw":"希伯来语",
    "el":"希腊语",
    "haw":"夏威夷语",
    "sd":"信德语",
    "hu":"匈牙利语",
    "sn":"修纳语",
    "hy":"亚美尼亚语",
    "ig":"伊博语",
    "it":"意大利语",
    "yi":"意第绪语",
    "hi":"印地语",
    "su":"印尼巽他语",
    "id":"印尼语",
    "jw":"印尼爪哇语",
    "en":"英语",
    "yo":"约鲁巴语",
    "vi":"越南语",
    "zh-CN":"中文"
},
"target_code_name":{
    "sq":"阿尔巴尼亚语",
    "ar":"阿拉伯语",
    "am":"阿姆哈拉语",
    "az":"阿塞拜疆语",
    "ga":"爱尔兰语",
    "et":"爱沙尼亚语",
    "eu":"巴斯克语",
    "be":"白俄罗斯语",
    "bg":"保加利亚语",
    "is":"冰岛语",
    "pl":"波兰语",
    "bs":"波斯尼亚语",
    "fa":"波斯语",
    "af":"布尔语(南非荷兰语)",
    "da":"丹麦语",
    "de":"德语",
    "ru":"俄语",
    "fr":"法语",
    "tl":"菲律宾语",
    "fi":"芬兰语",
    "fy":"弗里西语",
    "km":"高棉语",
    "ka":"格鲁吉亚语",
    "gu":"古吉拉特语",
    "kk":"哈萨克语",
    "ht":"海地克里奥尔语",
    "ko":"韩语",
    "ha":"豪萨语",
    "nl":"荷兰语",
    "ky":"吉尔吉斯语",
    "gl":"加利西亚语",
    "ca":"加泰罗尼亚语",
    "cs":"捷克语",
    "kn":"卡纳达语",
    "co":"科西嘉语",
    "hr":"克罗地亚语",
    "ku":"库尔德语",
    "la":"拉丁语",
    "lv":"拉脱维亚语",
    "lo":"老挝语",
    "lt":"立陶宛语",
    "lb":"卢森堡语",
    "ro":"罗马尼亚语",
    "mg":"马尔加什语",
    "mt":"马耳他语",
    "mr":"马拉地语",
    "ml":"马拉雅拉姆语",
    "ms":"马来语",
    "mk":"马其顿语",
    "mi":"毛利语",
    "mn":"蒙古语",
    "bn":"孟加拉语",
    "my":"缅甸语",
    "hmn":"苗语",
    "xh":"南非科萨语",
    "zu":"南非祖鲁语",
    "ne":"尼泊尔语",
    "no":"挪威语",
    "pa":"旁遮普语",
    "pt":"葡萄牙语",
    "ps":"普什图语",
    "ny":"齐切瓦语",
    "ja":"日语",
    "sv":"瑞典语",
    "sm":"萨摩亚语",
    "sr":"塞尔维亚语",
    "st":"塞索托语",
    "si":"僧伽罗语",
    "eo":"世界语",
    "sk":"斯洛伐克语",
    "sl":"斯洛文尼亚语",
    "sw":"斯瓦希里语",
    "gd":"苏格兰盖尔语",
    "ceb":"宿务语",
    "so":"索马里语",
    "tg":"塔吉克语",
    "te":"泰卢固语",
    "ta":"泰米尔语",
    "th":"泰语",
    "tr":"土耳其语",
    "cy":"威尔士语",
    "ur":"乌尔都语",
    "uk":"乌克兰语",
    "uz":"乌兹别克语",
    "es":"西班牙语",
    "iw":"希伯来语",
    "el":"希腊语",
    "haw":"夏威夷语",
    "sd":"信德语",
    "hu":"匈牙利语",
    "sn":"修纳语",
    "hy":"亚美尼亚语",
    "ig":"伊博语",
    "it":"意大利语",
    "yi":"意第绪语",
    "hi":"印地语",
    "su":"印尼巽他语",
    "id":"印尼语",
    "jw":"印尼爪哇语",
    "en":"英语",
    "yo":"约鲁巴语",
    "vi":"越南语",
    "zh-TW":"中文(繁体)",
    "zh-CN":"中文(简体)"
}
}

class googleTranslator():
    def __init__(self):
        ctx = execjs.compile("""
    function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;

        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";

        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };

    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
    """)
        def getTk(text):
            return ctx.call("TL", text)
        
        self.getTk = getTk

    def translate(self, text, source_code_name = 'en', target_code_name= 'zh-CN'):
        assert source_code_name in lang_dict['source_code_name']
        assert target_code_name in lang_dict['target_code_name']
        assert len(text) <= 4891
        
        url = "https://translate.google.cn/translate_a/single?client=webapp&" \
          "sl=%s&tl=%s&hl=en&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&clearbtn=1&otf=1&" \
          "pc=1&ssel=3&tsel=3&kc=2&tk=%s&%s" % (source_code_name, target_code_name, self.getTk(text), urllib.parse.urlencode({'q': text}))
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        response = requests.get(url, headers = headers)
        if response.status_code != 200:
            return None
        
        response_json = response.json()
        
        result = ''
        for lt in response_json[0]:
            if type(lt[0]) == str:
                result += lt[0]
        return result
        

def isChinese(text):
    """
        基本汉字的 UNICODE 编码在区间 4E00-9FA5 内，
        如果在这个区间的字符数超过1/3，则认为是中文
    """
    zh_n = 0
    for c in text:
        i = ord(c)
        if i >= 0x4E00 and i <= 0x9FA5:
            zh_n += 1
    return zh_n * 3 > len(text)


if __name__ == '__main__':
    import sys
    
    # 检查参数长度
    if len(sys.argv) < 2:
        exit(1)

    text = ' '.join(sys.argv[1:])
    if isChinese(text):
        print(googleTranslator().translate(text, 'zh-CN', 'en'))
    else:
        print(googleTranslator().translate(text, 'auto', 'zh-CN'))









