#!/bin/python3
#-*- encoding:utf-8 -*-

import math

func_list = [ f for f in dir(math) if not f.startswith('_')]

func_list.extend(['abs'])
constant_list = ['pi', 'e', 'tau', 'inf', 'nan', 'true', 'false', 'True', 'False']

func_list = list(set(func_list) - set(constant_list))
func_list.sort()

_help = '''支持的运算符
1. 基本运算
   加减乘除  + - * /
   乘方      **
   括号      ( )
   取余      %
   整除      //
2. 位运算
   按位与    |
   按位或    &
   按位异或  ^
   按位取反  ~
   左移      <<
   右移      >>
3. 逻辑运算
   真        true
   假        false
   与        and
   或        or
   非        not
4. 比较运算符
   相等      ==
   不等      !=
   大于      >
   小于      <
   大于等于  >=
   小于等于  <=
5. 集合
   集合表示  {1,2,3,...}
   空集      {}
   求交集    &
   求并集    |
   求差集    -
   对称差集  ^
6. 数学常量
   圆周率  pi
   自然对数的底 e
   圆周常数 tau
   浮点无穷大 inf
   浮点非数字 nan
7. 函数支持
   若干个函数，回复“函数”我告诉你支持那些。

除了支持十进制以外，以下表示都可以的
   十六进制数 0x开头
   八进制数  0o开头
   二进制数  0b开头

发任意数字我可以帮你转换成二进制、八进制、十进制、十六进制

发算式，我就可以帮你算算
1+1=2我还是能算出来哒～/:,@P

只能发算式哦，要是发别的我就给你反过来念
'''


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
    
def getFuncHelp():
    return '目前暂时支持以下函数\n' + ' '.join(func_list)

def isValid(exp_str):
    r = r'^(('+'|'.join(im)+r')|[-+*/(){}%\|&~^!<>=,\. ]|and|or|not|' + '|'.join(constant_list) + '|' + '|'.join(func_list) +')+$'
    return re.match(r, exp_str) is not None

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
            '十六进制    ' + hex(i)[ic:].upper() + '\n' + \
            '　十进制    ' + str(i) + '\n' + \
            '　八进制    ' + oct(i)[ic:] + '\n' + \
            '　二进制    ' + bin(i)[ic:]
    try:
        exp_str = exp_str.replace('{}', 'set()')
        exp_str = exp_str.replace('true', 'True')
        exp_str = exp_str.replace('false', 'False')
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
            '别整我，求你'
        ]
        ret = msg_list[random.randint(0,len(msg_list)-1)]
    except NameError:
        ret = '你不能这样子，我不知道这是什么。'
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
    exp_str = sys.argv[1]
    if not isValid(exp_str):
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



