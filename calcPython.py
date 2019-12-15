#!/bin/python3
#-*- encoding:utf-8 -*-

import math
constant_list = [
    'pi',
    'tau',
    'inf',
    'nan',
    'true',
    'false'
]

func_list = [
    'sin', 'cos', 'tan',
    'asin', 'acos', 'atan', 'atan2',
    'sinh', 'cosh', 'tanh',
    'asinh', 'acosh', 'atanh',
    'abs', 'ceil', 'floor',
    'exp', 'pow', 'sqrt',
    'log', 'log2', 'log10', 'lg',
    'fact'
]

_detail_help = '''【详细介绍】
可以进行乘方三角函数对数等等计算
两个特殊常数 pi 和 e 可以用
用函数一定要加括号例如：sin(pi/2) log(e**3)
pow(x,y) 表示x的y次方
pow(x,1/y) 表示把x开y次方
sqrt(x) 可以开平方
甚至可以复数计算哦，用 j 表示虚数单位
例如 3+4j 表示实数部分为3，虚数部分为4的数

【进制】
除了支持十进制以外，以下表示都可以的
 十六进制数 0x开头
 八进制数  0o开头
 二进制数  0b开头
单独发任意形式的数字我可以帮你转换成二进制、八进制、十进制、十六进制

【运算符】
1. 基本运算符
 + - * / ** ( )
 取余  %
 整除  //
2. 位运算
 | & ~ ^ << >>
3. 逻辑运算
 真假  true false
 与或非  and or not
（以上单词前后记得加空格）
4. 比较运算符
 相等和不等  == !=
 大于和小于  > <
 大于等于  >=
 小于等于  <=
5. 集合
 集合表示 {1,2,3,...}
 空集  {}
 求交集  &
 求并集  |
 求差集  -
 对称差集  ^

【函数支持】
（反）三角函数 sin cos tan
asin acos atan atan2(x,y)
（反）双曲函数
sinh cosh tanh
asinh acosh atanh
取模或绝对值 abs
向上取整 ceil
向下取整 floor
乘方开方 exp pow(x,y) sqrt
对数 log log2 log10 lg'''


_help = '''基本的加减乘除计算，只要是整数的话无论数字多大多少位只要在我承受范围内都可以
加减乘除分别用符号表示：  + - * /
四则运算还是乘除优先，改变优先级记得加括号，可以套若干个层的小括号，多复杂都可以
记住：乘号*不能省略，不然我会看不懂
举例： 138*(43+31222)-1

乘方用两个*表示，例如 2**8 表示2的8次方
阶乘用 fact(4) 表示 4 的阶乘，当然 4! 也可以
可以科学计数法，例如 3.4e4 表示3.4万；3.4e-4 表示 0.00034

以上是基本的数学计算，还支持一些更高级的数学运算，感兴趣的话，可以发送“详细”。

只能发算式哦，要是发别的我就给你反过来念'''


import re
import random
import subprocess
import os
import sys
from math import *

im = [
    '[+-]?0[Bb][01]+',
    '[+-]?0[Oo][01234567]+',
    '[0123456789]+',
    '[+-]?0[Xx][0123456789abcdefABCDEF]+'
]
imk = {
    2:0,
    8:1,
    10:2,
    16:3
}

def getHelp():
    return _help
    
def getDetailHelp():
    return _detail_help
    
def getFuncHelp():
    return '目前暂时支持以下函数\n' + ' '.join(func_list)

def convValid(exp_str):
    # 处理替换中文字符
    exp_str = exp_str.translate(str.maketrans(
        '！｜÷，～＋－—（）｛｝＜＞＝％＆＾＊×　ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ',
        '!|/,~+--(){}<>=%&^** abcdefghijklmnopqrstuvwxyz'
        ))
    
    # 全部转换成小写
    exp_str = exp_str.lower()
    
    # 替换一些特殊符号
    exp_str = re.sub('(π|pai)', ' pi ', exp_str)
    exp_str = re.sub('(Ø|∅|Φ)', '{}', exp_str)
    exp_str = re.sub('(≠)', '!=', exp_str)
    
    # 初步正则匹配
    r = r'^(('+'|'.join(im)+r')|[-+*/(){}%\|&~^!<>=,\. ej]|and|or|not|' + '|'.join(constant_list) + '|' + '|'.join(func_list) +')+$'
    if re.match(r, exp_str) is None:
        return None
    
    # 逻辑运算符和常数前后确保有空格
    exp_str = re.sub('([^ ])(and|or|not' + '|'.join(constant_list) + ')', r'\1 \2', exp_str)
    exp_str = re.sub('(and|or|not' + '|'.join(constant_list) + ')([^ ])', r'\1 \2', exp_str)
    
    # 科学计数法 1 省略的补上
    exp_str = re.sub('([\W]|^)(e[\d]+)', r'\1 1\2', exp_str)
    
    # 虚数单位 j 前面的 1 省略的补上
    exp_str = re.sub('([\W]|^)j([\W]|$)', r'\1 1j\2', exp_str)
    
    # 函数调用前面确保有空格
    #exp_str = re.sub('([^ ])(' + '|'.join(constant_list) + ')', r'\1 \2', exp_str)
    
    # 函数调用后面确保有括号
    exp_str = re.sub('(' + '|'.join(func_list) + ') +([^(].*)', r'\1(\2)', exp_str)
    
    # 阶乘
    exp_str = re.sub('([\d]+)!([^=]|$)', r'fact(\1)\2', exp_str)
    
    # 空格合并
    exp_str = re.sub(' +', ' ', exp_str)
    
    return exp_str

def tryInt(num_str):
    if re.match('^'+im[imk[10]]+'$', num_str) is not None:
        return int(num_str, 10)
    if re.match('^'+im[imk[16]]+'$', num_str) is not None:
        return int(num_str, 16)
    if re.match('^'+im[imk[2]]+'$', num_str) is not None:
        return int(num_str, 2)
    if re.match('^'+im[imk[8]]+'$', num_str) is not None:
        return int(num_str, 8)
    return None

def calc(exp_str):
    tuple_err_list = [
        '你这括号我就不懂了...',
        '括号不是这么玩的。',
        '你家括号这样用的啊？'
    ]
    
    # 如果是数字直接进制转换
    i = tryInt(exp_str)
    if i is not None:
        ic = 3 if i < 0 else 2
        return \
            '十六进制' + '\n' + hex(i)[ic:].upper() + '\n' + '\n' + \
            '十进制' + '\n' + str(i) + '\n' + '\n' + \
            '八进制' + '\n' + oct(i)[ic:] + '\n' + '\n' + \
            '二进制' + '\n' + bin(i)[ic:]
    try:
        exp_str = exp_str.replace('{}', 'set()')
        exp_str = exp_str.replace('true', 'True')
        exp_str = exp_str.replace('false', 'False')
        fact = factorial
        lg = log10
        ret = eval(exp_str)
        if type(ret) == tuple:
            ret = tuple_err_list[random.randint(0, len(tuple_err_list)-1)]
        ret = str(ret)
    except SyntaxError as err:
        msg_list = [
            '语法好像有问题耶，我理解不了这里',
            '你逗我',
            '这里是不是要改一下，不然我看不懂哦',
            '这是什么鬼'
        ]
        pd = ' ' * (err.offset - 1)
        ret = exp_str + '\n' + \
            pd + '^' + '\n' + \
            msg_list[random.randint(0,len(msg_list)-1)]
    except ZeroDivisionError:
        msg_list = [
            '除以零，我做不到...',
            '除数为零，开心就好 ～',
            '除以零的话，结果应该是无穷大吧，你觉得呢？',
            '别再让我除以零了，我受不了啦'
        ]
        ret = msg_list[random.randint(0,len(msg_list)-1)]
    except ValueError:
        msg_list = [
            'emmmm.....我算不出这个，我也不知道怎么了。',
            '我傻了',
            '对不起，我算不出/::<',
            '看到这个式子，我凌乱了...',
            '你继续，我默默地看着你自嗨',
            '别整我，求你',
            '定义域是不是有问题？想想看'
        ]
        ret = msg_list[random.randint(0,len(msg_list)-1)]
    except NameError as err:
        ret = err.args[0]
        ret = re.sub(r"name '(.+)' is not defined", r'用函数的话把括号加上吧，不然我以为 “\1” 是个函数。', ret)
    except TypeError as err:
        ret = err.args[0]
        ret = re.sub(".*tuple.*", tuple_err_list[random.randint(0,len(tuple_err_list)-1)], ret)
        ret = re.sub(r'takes exactly one argument \((\d+) given\)', r'需要一个参数，您给了 \1 个', ret)
        ret = re.sub(r'expected (\d) arguments, got (\d)', r'需要 \1 个参数，您给了 \2 个', ret)
        ret = re.sub(r"'(.+)' object is not callable", r'\1不能当函数用的...', ret)
        ret = re.sub(r"unsupported operand type\(s\) for (.+): '(.+)' and '(.+)'", r'\2和\3之间不能用 \1 运算的哦～', ret)
        ret = re.sub(r"'(.+)' not supported between instances of '(.+)' and '(.+)'", r'\2和\3之间不能用 \1 运算的哦～', ret)
        ret = re.sub(r"bad operand type for (.+): '(.+)'", r'\1 不能对\2进行计算', ret)
        ret = re.sub(r"must be (.+), not (.+)", r'这里参数只能是\1，是\2的话我也不知道怎么算', ret)
        ret = ret.replace("unary", '一元运算符')
        ret = ret.replace('real number', '实数')
        ret = ret.replace("float", '浮点数')
        ret = ret.replace("int", '整数')
        ret = ret.replace("set", '集合')
        ret = ret.replace("bool", '逻辑值')
        ret = ret.replace('builtin_function_or_method', '函数')
        ret = ret.replace(', ', '，')
    ret = ret.replace('built-in function', '这是函数')
    ret = ret.replace('set()', '{}')
    return ret


def popen_t(cmd, timeout):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    try:
        p.wait(timeout = timeout)
    except subprocess.TimeoutExpired:
        p.terminate()
    ret = p.stdout.read()
    if len(ret) == 0:
        return None
    return ret

def calc_t(exp_str, timeout):
    '''
        定时计算函数
        只能用子进程实现，线程实现会卡住
    '''
    ret = popen_t(['env', 'PYTHONIOENCODING=utf-8', 'python3', os.path.abspath(__file__), exp_str], timeout)
    if ret is None:
        return None
    return ret.decode('utf-8')

def main():
    # 检查参数长度
    if len(sys.argv) < 2:
        sys.stderr.write(getHelp())
        return 1
    
    # 检查表达式合法
    exp_str = convValid(sys.argv[1])
    if exp_str is None:
        sys.stderr.write('不正确的表达式\n')
        return 2
    
    # 获取超时时间
    timeout = None
    if len(sys.argv) > 2:
        try:
            timeout = float(sys.argv[2])
        except ValueError:
            sys.stderr.write('超时时间参数错误\n')
            return 3
    
    if timeout is None:
        sys.stdout.write(calc(exp_str))
    else:
        ret = calc_t(exp_str, timeout)
        if ret is None:
            sys.stderr.write('计算超时\n')
            return 4
        sys.stdout.write(ret)

if __name__ == '__main__':
    exit(main())



