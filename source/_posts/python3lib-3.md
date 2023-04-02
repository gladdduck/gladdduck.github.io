---
title: python标准库-3
categories:
  - 学习笔记
tags:
  - python3 标准库
toc: true# 是否启用内容索引

---


## 网络通信

### ipaddress


```python
import ipaddress
# ipaddress:解析ip地址
```

### socket


```python
import socket
# 网络通信
# 多线程网络服务

'''服务器端'''

from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread
def main():
    # 自定义线程类
    class FileTransferHandler(Thread):
        def __init__(self, cclient):
            super().__init__()
            self.cclient = cclient
        def run(self):
            my_dict = {}
            my_dict['filename'] = 'guido.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata'] = 'data'
            # 通过dumps函数将字典处理成JSON字符串
            json_str = dumps(my_dict)
            # 发送JSON字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1.创建套接字对象并指定使用哪种传输服务
    server = socket()
    # 2.绑定IP地址和端口(区分不同的服务)
    server.bind(('localhost', 5566))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    while True:
        client, addr = server.accept()
        # 启动一个线程来处理客户端的请求
        FileTransferHandler(client).start()
if __name__ == '__main__':
    main()

'''客户端'''

from socket import socket
from json import loads
from base64 import b64decode
def main():
    client = socket()
    client.connect(('localhost', 5566))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024字节
    data = client.recv(1024)
    while data:
        # 将收到的数据拼接起来
        in_data += data
        data = client.recv(1024)
    # 将收到的二进制数据解码成JSON字符串并转换成字典
    # loads函数的作用就是将JSON字符串转成字典对象
    my_dict = loads(in_data.decode('utf-8'))
    print(my_dict)
    print('图片已保存.')
if __name__ == '__main__':
    main()
```

### selectors


```python
import selectors

# io多路复用抽象
```

### select


```python
import select
# 高效等待IO
```

### socketserver


```python
import socketserver
# 创建网络服务器
```

## 互联网

###  urllib.parase


```python
from urllib import parase

# 分解url
```

### urllib.request


```python
from urllib import request

# 根据url获取web资源
# get/post/参数/头文件/
```

### urllib.robotparser


```python
from urllib import robotparser

# 获得网页的robots.txt文件,测试是否允许爬取页面
from urllib import parse
from urllib import robotparser

AGENT_NAME = 'Googlebot'
URL_BASE = 'https://zhuanlan.zhihu.com/'
parser = robotparser.RobotFileParser()
parser.set_url(parse.urljoin(URL_BASE, 'robots.txt'))
parser.read()

PATHS = [
    '/',
    '/search-special',
    '/login',
    '/s',
]

for path in PATHS:
    print('{!r:>6} : {}'.format(
        parser.can_fetch(AGENT_NAME, path), path))
    url = parse.urljoin(URL_BASE, path)
    print('{!r:>6} : {}'.format(
        parser.can_fetch(AGENT_NAME, url), url))
    print()

```

      True : /
      True : https://zhuanlan.zhihu.com/
    
     False : /search-special
     False : https://zhuanlan.zhihu.com/search-special
    
     False : /login
     False : https://zhuanlan.zhihu.com/login
    
      True : /s
      True : https://zhuanlan.zhihu.com/s
    
    

### base64


```python
import base64
# 将二进制数据转换为适合使用文本协议传输的ASCII的一个子集
initial_data='Copyright (c) 2008 Doug Hellmann All rights reserved.'
print(f'initial_data:{initial_data}')
byte_string = initial_data.encode('utf-8')
encoded_data = base64.b64encode(byte_string)
print(f'base64 data:{encoded_data}')


encoded_data = b'VGhpcyBpcyB0aGUgZGF0YSwgaW4gdGhlIGNsZWFyLg=='
decoded_data = base64.b64decode(encoded_data)
print('Encoded :', encoded_data)
print('Decoded :', decoded_data)
```

    initial_data:Copyright (c) 2008 Doug Hellmann All rights reserved.
    base64 data:b'Q29weXJpZ2h0IChjKSAyMDA4IERvdWcgSGVsbG1hbm4gQWxsIHJpZ2h0cyByZXNlcnZlZC4='
    Encoded : b'VGhpcyBpcyB0aGUgZGF0YSwgaW4gdGhlIGNsZWFyLg=='
    Decoded : b'This is the data, in the clear.'
    

### http.server


```python
from http import server

# 自己实现do_GET(),do_POST()方法的web服务器
```

### http.cookie


```python
from http import cookie

# 
```

### webbrowser


```python
import webbrowser
# 浏览器打开界面
webbrowser.open_new_tab(
    'https://docs.python.org/3/library/webbrowser.html'
)

```




    True



### uuid


```python
import uuid

print(uuid.getnode())
print(uuid.uuid1())
```

    4943745048992
    1e4a5d1c-cc80-11ed-8e72-047f0e2ae1a0
    

### json


```python
import json
# 键必须是字符串类型
# tuple会转成list

# 文件
json.load()
json.dump()
# 字符串
json.loads()
json.dumps()
```

## email


```python

from smtplib import SMTP,SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def main():
    # 创建一个带附件的邮件消息对象
    message = MIMEMultipart()
    
    # 创建文本内容
    text_content = MIMEText('附件中有本月数据请查收', 'plain', 'utf-8')
    message['From'] = Header('gladdduck', 'utf-8')
    message['To'] = Header('亚哥', 'utf-8')
    message['Subject'] = Header('本月数据', 'utf-8')
    # 将文本内容添加到邮件消息对象中
    message.attach(text_content)

    # 读取文件并将文件作为附件添加到邮件消息对象中
    with open('words.txt', 'rb') as f:
        txt = MIMEText(f.read(), 'base64', 'utf-8')
        txt['Content-Type'] = 'text/plain'
        txt['Content-Disposition'] = 'attachment; filename=hello.txt'
        message.attach(txt)
    
    # 创建SMTP对象
    smtper = SMTP_SSL('smtp.qq.com')
    # 开启安全连接
    # smtper.starttls()
    sender = '703214452@qq.com'
    receivers = ['syxue@stu.suda.edu.cn']
    # 登录到SMTP服务器
    # 请注意此处不是使用密码而是邮件客户端授权码进行登录
    # 对此有疑问的读者可以联系自己使用的邮件服务器客服
    smtper.login(sender, '*****')
    # 发送邮件
    smtper.sendmail(sender, receivers, message.as_string())
    # 与邮件服务器断开连接
    smtper.quit()
    print('发送完成!')


if __name__ == '__main__':
    main()

```

## 应用构建模块

### argparse


```python
import argparse
# 声明
# parents参数,合并其他解析器
parser = argparse.ArgumentParser(description='test')

# 位置参数,必填
parser.add_argument("echo")
# 可选参数,一个简称,一个全称,不给默认为None
parser.add_argument("-v", "--verbose")

'''
add_argument()参数

action:默认是store,存储参数
    store_const:表示只能赋值为const
    append:把参数存储成列表
    append_const:把const的值存储为列表
    count:统计参数出现的次数
    store_true/store_false:保存布尔值,出现就是true or false
    
default:默认值
type:参数类型
choice:只能从里面选
required:可以省略 (仅针对可选参数)。
help:打印的时候的帮助信息
dest:解析后的参数名称
nargs:表示后面要跟几个参数

group=parser.add_mutually_exclusive_group()互斥选项,

'''


# 解析,默认解析的sys.argv[1:]
parser.parse_args()
```

### getopt


```python
import getopt

# 命令行选项解析
```

### readline

### getpass


```python
import getpass

p=getpass.getpass(prompt='输入密码')
print(p,p)
```

### cmd


```python
import cmd

# 面向行的命令处理器
```

### shlex


```python
import shlex
# 解析shell语法
```

### configparser


```python
import configparser

'''
[DEFAULT]
serveraliveinterval = 45
compression = yes
compressionlevel = 9

[bitbucket]
user = kk

[topsecrect]
port = 22
'''

import configparser

config = configparser.ConfigParser()

# 不存在忽略,可以多个配置文件合并
config.read('example.ini')

# sections就是[]中的配置,has_section()
# options是[]下面的选项,has_option()
for section_name in config.sections():
    print('Section:', section_name)
    print('  Options:', config.options(section_name))
    for name, value in config.items(section_name):
        print('  {} = {}'.format(name, value))
    print()
    
config.add_section('bug_tracker')
config.set('bug_tracker', 'url', 'http://localhost:8080/bugs')
config.set('bug_tracker', 'username', 'dhellmann')
config.set('bug_tracker', 'password', 'secret')
config.remove_option('bug_tracker', 'password')
config.remove_section('wiki')


# parser.write(f)
```

### logging

![](http://image.yayan.xyz/20230328215242.png)


```python
import logging

logging.basicConfig(level=logging.WARNING)

# 不同模块的日志

logger1 = logging.getLogger('package1.module1')
logger2 = logging.getLogger('package2.module2')

logger1.warning('This message comes from one module')
logger2.warning('This comes from another module')

```

    WARNING:package1.module1:This message comes from one module
    WARNING:package2.module2:This comes from another module
    


```python
import logging
# 格式化

# LOG_FILENAME = 'logging_example.out'
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    # filename=LOG_FILENAME,
                    )

logging.debug('debug 信息')
logging.info('info 信息')
logging.warning('warning 信息')
logging.error('error 信息')
logging.critical('critial 信息')
'''
级别  数值

CRITICAL 50

ERROR  40

WARNING  30

INFO  20

DEBUG  10

NOTSET  0
'''

```

    2023-03-28 21:44:07,434 - C:\Users\22627\AppData\Local\Temp\ipykernel_2380\2094327826.py[line:8] - DEBUG: debug 信息
    2023-03-28 21:44:07,436 - C:\Users\22627\AppData\Local\Temp\ipykernel_2380\2094327826.py[line:9] - INFO: info 信息
    2023-03-28 21:44:07,438 - C:\Users\22627\AppData\Local\Temp\ipykernel_2380\2094327826.py[line:10] - WARNING: warning 信息
    2023-03-28 21:44:07,440 - C:\Users\22627\AppData\Local\Temp\ipykernel_2380\2094327826.py[line:11] - ERROR: error 信息
    2023-03-28 21:44:07,443 - C:\Users\22627\AppData\Local\Temp\ipykernel_2380\2094327826.py[line:12] - CRITICAL: critial 信息
    


```python
# 写不同文件
import glob
import logging
import logging.handlers

LOG_FILENAME = 'logging_rotatingfile_example.out'

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)

handler = logging.handlers.RotatingFileHandler(
    LOG_FILENAME,
    maxBytes=20,
    backupCount=5,
)
my_logger.addHandler(handler)

for i in range(20):
    my_logger.debug('i = %d' % i)

logfiles = glob.glob('%s*' % LOG_FILENAME)
for filename in sorted(logfiles):
    print(filename)
```

### fileinput



```python
import fileinput

# 命令行过滤器框架
```

### atexit



```python
import atexit

# 程序关闭回调
def my_cleanup(name):
    print('my_cleanup({})'.format(name))

atexit.register(my_cleanup, 'first')
atexit.register(my_cleanup, 'second')
atexit.register(my_cleanup, 'third')


# 因为信号终止
# os._exit()
# 致命错误
@atexit.register
def all_done():
    print('all_done()')


print('starting main program')
```

    starting main program
    

### sched


```python
import sched

# 在指定时刻运行任务

import sched
import time

scheduler = sched.scheduler(time.time, time.sleep)


def long_event(name):
    print('BEGIN EVENT :', time.ctime(time.time()), name)
    time.sleep(2)
    print('FINISH EVENT:', time.ctime(time.time()), name)


print('START:', time.ctime(time.time()))
# 时间,优先级,函数,参数
scheduler.enter(2, 1, long_event, ('first',))
# run是阻塞的,但是这个是到了就执行,要在不同线程内取消
scheduler.enter(3, 1, long_event, ('second',))

scheduler.run()

```

    START: Tue Mar 28 21:57:03 2023
    BEGIN EVENT : Tue Mar 28 21:57:05 2023 first
    FINISH EVENT: Tue Mar 28 21:57:07 2023 first
    BEGIN EVENT : Tue Mar 28 21:57:07 2023 second
    FINISH EVENT: Tue Mar 28 21:57:09 2023 second
    


```python
price=0
age=int(input())
if age<12:
    price=0
elif age<=65:
    price=40
elif age>65:
    price=20
print(f'Your price is {price} yuan')
```

    Your price is 40 yuan
    

## 国际化和本地化

## 开发工具

### pydoc


```python
import pydoc
import atexit
# 运行时生成帮助文本
pydoc.doc(atexit)
```

### doctest


```python
import doctest

# 运行嵌入文档中的例子，验证是否生成期望的结果
def my_function(a, b):
    """Returns a * b.

    Works with numbers:

    >>> my_function(2, 3)
    6

    and strings:

    >>> my_function('a', 3)
    'aaa'
    
    # 忽略可能会变化的部分
    >>> unpredictable(MyClass()) #doctest: +ELLIPSIS
    [<doctest_ellipsis.MyClass object at 0x...>]
    """
    return a * b
if __name__=="__main__":
    doctest.testmod()
# !python3 -m doctest -v xxx.py
```

### unittest


```python
import unittest
# 自动测试框架

class SimplisticTest(unittest.TestCase):

    def test(self):
        a = 'a'
        b = 'a'
        self.assertEqual(a, b)
        self.assertFalse()
        self.assertTrue()
        self.assertNotEqual()
        self.assertNotEqual()
        # ...
    
```

### trace


```python
import trace

# 监视所执行的语句，生成报告，查看互相调用的函数之间的关系

# 会生成函数之间的调用关系
def recurse(level):
    print('recurse({})'.format(level))
    if level:
        recurse(level - 1)


def not_called():
    print('This function is never called.')
def main():
    print('This is the main program.')
    recurse(2)

tracer = trace.Trace(count=False, trace=True)
tracer.run('recurse(2)')
```

### traceback


```python
import traceback

# 调用栈来生成错误消息


```

### cgitb


```python
import cgitb

# cgitb把sys.excepthook 换成一个函数,格式化输出，更详细

```

### pdb


```python
import pdb

# 暂停程序，逐步监视执行
# debug
```

### profile & pstats


```python
import profile
import pstats
# profile收集消耗处理器资源的统计信息
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq


# profile.run('print(fib_seq(20)); print()')
profile.runctx(
    'print(fib_seq(n)); print()',
    globals(),
    {'n': 20},
)
# pstats与profile结合

```

    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    
             57409 function calls (119 primitive calls) in 0.156 seconds
    
       Ordered by: standard name
    
       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
         21/1    0.000    0.000    0.156    0.156 1066040024.py:12(fib_seq)
     57291/21    0.156    0.000    0.156    0.007 1066040024.py:4(fib)
            4    0.000    0.000    0.000    0.000 :0(acquire)
           25    0.000    0.000    0.000    0.000 :0(append)
            1    0.000    0.000    0.156    0.156 :0(exec)
           20    0.000    0.000    0.000    0.000 :0(extend)
            3    0.000    0.000    0.000    0.000 :0(getpid)
            3    0.000    0.000    0.000    0.000 :0(isinstance)
            3    0.000    0.000    0.000    0.000 :0(len)
            2    0.000    0.000    0.000    0.000 :0(print)
            1    0.000    0.000    0.000    0.000 :0(setprofile)
            1    0.000    0.000    0.156    0.156 <string>:1(<module>)
            4    0.000    0.000    0.000    0.000 iostream.py:206(schedule)
            3    0.000    0.000    0.000    0.000 iostream.py:418(_is_master_process)
            3    0.000    0.000    0.000    0.000 iostream.py:437(_schedule_flush)
            3    0.000    0.000    0.000    0.000 iostream.py:500(write)
            4    0.000    0.000    0.000    0.000 iostream.py:96(_event_pipe)
            1    0.000    0.000    0.156    0.156 profile:0(print(fib_seq(n)); print())
            0    0.000             0.000          profile:0(profiler)
            4    0.000    0.000    0.000    0.000 socket.py:543(send)
            4    0.000    0.000    0.000    0.000 threading.py:1066(_wait_for_tstate_lock)
            4    0.000    0.000    0.000    0.000 threading.py:1133(is_alive)
            4    0.000    0.000    0.000    0.000 threading.py:536(is_set)
    
    
    

### timeit


```python
import timeit
# 测量小代码时间
t = timeit.Timer("print('main statement')", "print('setup')")

print('TIMEIT:')
print(t.timeit(2))

print('REPEAT:')
print(t.repeat(3, 2))

```

    TIMEIT:
    setup
    main statement
    main statement
    1.2299999980314169e-05
    REPEAT:
    setup
    main statement
    main statement
    setup
    main statement
    main statement
    setup
    main statement
    main statement
    [0.00017259999958696426, 2.790000007735216e-05, 1.540000039312872e-05]
    


```python
import contextlib
import time
# Yolov5时间记录

class Profile(contextlib.ContextDecorator):
    # YOLOv5 Profile class. Usage: @Profile() decorator or 'with Profile():' context manager
    def __init__(self, t=0.0):
        self.t = t
        # self.cuda = torch.cuda.is_available()

    def __enter__(self):
        self.start = self.time()
        return self

    def __exit__(self, type, value, traceback):
        self.dt = self.time() - self.start  # delta-time
        self.t += self.dt  # accumulate dt

    def time(self):
        # if self.cuda:
        #     torch.cuda.synchronize()
        return time.time()
    
ttt=Profile()
with ttt:
    [_ for _ in range(int(1e7))]
print(ttt.t)
```

    0.534808874130249
    

### tabnanny


```python
import tabnanny
# 缩进验证工具
```

### compileall


```python
import compileall
```

### venv


```python
import venv
# 创建虚拟环境
```

## 运行时特性

### site


```python
import site

# 站点特定的配置,导入路径
```

### sys


```python
import sys
# 系统特定配置
print('Version info:')
print()
print('sys.version      =', repr(sys.version))
print('sys.version_info =', sys.version_info)
print('sys.hexversion   =', hex(sys.hexversion))
print('sys.api_version  =', sys.api_version)
print('This interpreter was built for:', sys.platform)
# 获取运行时参数
print('Arguments:', sys.argv)
# 退出
# sys.exit(1)
print('Name:', sys.implementation.name)
print('Version:', sys.implementation.version)
print('Cache tag:', sys.implementation.cache_tag)

# print('STATUS: Reading from stdin')

# data = sys.stdin.read()

# print('STATUS: Writing data to stdout')

# sys.stdout.write(data)
# sys.stdout.flush()

# print('STATUS: Done')
# 参数的引用计数
one = []
print('At start         :', sys.getrefcount(one))
two = one
print('Second reference :', sys.getrefcount(one))
del two
print('After del        :', sys.getrefcount(one))


# 参数大小
class MyClass:
    pass
objects = [
    [], (), {}, 'c', 'string', b'bytes', 1, 2.3,
    MyClass, MyClass(),
]
# 不统计类的属性大小
for obj in objects:
    print('{:>10} : {}'.format(type(obj).__name__,sys.getsizeof(obj)))

```

    Version info:
    
    sys.version      = '3.9.13 (main, Aug 25 2022, 23:51:50) [MSC v.1916 64 bit (AMD64)]'
    sys.version_info = sys.version_info(major=3, minor=9, micro=13, releaselevel='final', serial=0)
    sys.hexversion   = 0x3090df0
    sys.api_version  = 1013
    This interpreter was built for: win32
    Arguments: ['C:\\Users\\Ada\\AppData\\Roaming\\Python\\Python39\\site-packages\\ipykernel_launcher.py', '--ip=127.0.0.1', '--stdin=9008', '--control=9006', '--hb=9005', '--Session.signature_scheme="hmac-sha256"', '--Session.key=b"fb322aac-cfd4-4a49-87ab-e11c0e6aea3e"', '--shell=9007', '--transport="tcp"', '--iopub=9009', '--f=c:\\Users\\Ada\\AppData\\Roaming\\jupyter\\runtime\\kernel-v2-100766YwHlokYHZ1d.json']
    Name: cpython
    Version: sys.version_info(major=3, minor=9, micro=13, releaselevel='final', serial=0)
    Cache tag: cpython-39
    At start         : 2
    Second reference : 3
    After del        : 2
          list : 56
         tuple : 40
          dict : 64
           str : 50
           str : 55
         bytes : 38
           int : 28
         float : 24
          type : 1064
       MyClass : 48
    


```python
class WithAttributes:
    def __init__(self):
        self.a = 'a'
        self.b = 'b'
        return

    def __sizeof__(self):
        return object.__sizeof__(self) + \
            sum(sys.getsizeof(v) for v in self.__dict__.values())

# 统计带参数的类大小
my_inst = WithAttributes()
print(sys.getsizeof(my_inst))


# getrecursionlimit()  setrecursionlimit() 查看设置最大递归深度
# getswitchinterval()  setswitchinterval() 查看设置线程获取的cpu运行时间
# 列表字典串的最大大小
print('maxsize   :', sys.maxsize)
print('maxunicode:', sys.maxunicode)

# 数的信息
# sys.float_info
# sys.int_info
```

    148
    maxsize   : 9223372036854775807
    maxunicode: 1114111
    


```python
# 处理错误信息
def my_excepthook(type, value, traceback):
    print('Unhandled error:', type, value)


sys.excepthook = my_excepthook

print('Before exception')

raise RuntimeError('This is the error message')

print('After exception')
# Before exception
# Unhandled error: <class 'RuntimeError'> This is the error 
# message
```


```python
import sys
import threading
import time


def do_something_with_exception():
    exc_type, exc_value = sys.exc_info()[:2]
    print('Handling {} exception with message "{}" in {}'.format(
        exc_type.__name__, exc_value,
        threading.current_thread().name))


def cause_exception(delay):
    time.sleep(delay)
    raise RuntimeError('This is the error message')


def thread_target(delay):
    try:
        cause_exception(delay)
    except RuntimeError:
        do_something_with_exception()


threads = [
    threading.Thread(target=thread_target, args=(0.3,)),
    threading.Thread(target=thread_target, args=(0.1,)),
]

for t in threads:
    t.start()
for t in threads:
    t.join()

```

    Handling RuntimeError exception with message "This is the error message" in Thread-7
    Handling RuntimeError exception with message "This is the error message" in Thread-6
    


```python
import sys

names = sorted(sys.modules.keys())
name_text = ', '.join(names)
# print(name_text)

for d in sys.path:
    print(d)

# sys.path 加入路径,
```

    d:\BaiduSyncdisk\Blog\source\_posts
    e:\Anaconda3\envs\AAA\python39.zip
    e:\Anaconda3\envs\AAA\DLLs
    e:\Anaconda3\envs\AAA\lib
    e:\Anaconda3\envs\AAA
    
    C:\Users\Ada\AppData\Roaming\Python\Python39\site-packages
    e:\Anaconda3\envs\AAA\lib\site-packages
    e:\Anaconda3\envs\AAA\lib\site-packages\openea-1.0-py3.9.egg
    e:\Anaconda3\envs\AAA\lib\site-packages\python_levenshtein-0.20.7-py3.9.egg
    e:\Anaconda3\envs\AAA\lib\site-packages\gensim-4.2.0-py3.9-win-amd64.egg
    e:\Anaconda3\envs\AAA\lib\site-packages\matching-0.1.1-py3.9.egg
    e:\Anaconda3\envs\AAA\lib\site-packages\win32
    e:\Anaconda3\envs\AAA\lib\site-packages\win32\lib
    e:\Anaconda3\envs\AAA\lib\site-packages\Pythonwin
    C:\Users\Ada\AppData\Roaming\Python\Python39\site-packages\IPython\extensions
    C:\Users\Ada\.ipython
    

### os


```python
import os
import sys

sys.path.append(r'D:\BaiduSyncdisk\Blog\source')
# os.listdir()
root='D:\BaiduSyncdisk\Blog\source'
for dir_name, sub_dirs, files in os.walk(root):
    print(dir_name,sub_dirs,files)
```


```python
for entry in os.scandir(root):
    if entry.is_dir():
        typ = 'dir'
    elif entry.is_file():
        typ = 'file'
    elif entry.is_symlink():
        typ = 'link'
    else:
        typ = 'unknown'
    print('{name} {typ}'.format(
        name=entry.name,
        typ=typ,
    ))
# stat()查看详细信息
# chmod()修改权限
# access()测试进程权限
# mkdir() 前面的路径必须存在
# makedirs() 创建不存在的父路径
# rmdir() 只会删除子目录
# removedirs() 删除为空的所有父目录
# replace() 
# rename()重命名
# environ() 环境变量
# getenv()
```


```python
# 当前工作目录
print(os.getcwd())
# 更改工作目录
os.chdir('d:\\BaiduSyncdisk\\Blog\\source')
print(os.getcwd())
# 运行外部命令
print(os.system('pwd'))
# 创建进程
# os.fork()
```

    d:\BaiduSyncdisk\Blog\source
    d:\BaiduSyncdisk\Blog\source
    1
    

### platform


```python
import platform

print('uname:', platform.uname())

print()
print('system   :', platform.system())
print('node     :', platform.node())
print('release  :', platform.release())
print('version  :', platform.version())
print('machine  :', platform.machine())
print('processor:', platform.processor())
print('interpreter:', platform.architecture())
print('/bin/ls    :', platform.architecture('/bin/ls'))
print('Normal :', platform.platform())
print('Aliased:', platform.platform(aliased=True))
print('Terse  :', platform.platform(terse=True))
print('Version      :', platform.python_version())
print('Version tuple:', platform.python_version_tuple())
print('Compiler     :', platform.python_compiler())
print('Build        :', platform.python_build())


```

    uname: uname_result(system='Windows', node='DESKTOP-SFFEKV7', release='10', version='10.0.19041', machine='AMD64')
    
    system   : Windows
    node     : DESKTOP-SFFEKV7
    release  : 10
    version  : 10.0.19041
    machine  : AMD64
    processor: Intel64 Family 6 Model 158 Stepping 10, GenuineIntel
    interpreter: ('64bit', 'WindowsPE')
    /bin/ls    : ('64bit', '')
    Normal : Windows-10-10.0.19041-SP0
    Aliased: Windows-10-10.0.19041-SP0
    Terse  : Windows-10
    Version      : 3.9.13
    Version tuple: ('3', '9', '13')
    Compiler     : MSC v.1916 64 bit (AMD64)
    Build        : ('main', 'Aug 25 2022 23:51:50')
    

### resource


```python
import resource
# 系统资源管理
RESOURCES = [
    ('ru_utime', 'User time'),
    ('ru_stime', 'System time'),
    ('ru_maxrss', 'Max. Resident Set Size'),
    ('ru_ixrss', 'Shared Memory Size'),
    ('ru_idrss', 'Unshared Memory Size'),
    ('ru_isrss', 'Stack Size'),
    ('ru_inblock', 'Block inputs'),
    ('ru_oublock', 'Block outputs'),
]

usage = resource.getrusage(resource.RUSAGE_SELF)

for name, desc in RESOURCES:
    print('{:<25} ({:<10}) = {}'.format(
        desc, name, getattr(usage, name)))

```

### gc


```python
import gc
# 垃圾回收

'''
enable()             --启用自动垃圾回收。
disable()            --禁用自动垃圾回收。
isenabled()          --如果启用了自动收集，则返回true。
collect()            --立即执行完全收集。
get_count()          --返回当前集合计数。
get_stats()          --返回包含每代统计信息的词典列表。
set_debug()          --设置调试标志。
get_debug()          --获取调试标志。
set_threshold()      --设置收集阈值。
get_threshold()      --返回集合阈值的当前值。
get_objects()        --返回收集器跟踪的所有对象的列表。
is_tracked()         --如果跟踪给定对象，则返回true。
is_finalized()       --如果给定对象已定稿，则返回true。
get_referrers()      --返回引用对象的对象列表。
get_referents()      --返回对象引用的对象列表。
freeze()             --冻结所有跟踪对象，并在将来的收集中忽略它们。
unfreeze()           --解冻永久生成中的所有对象。
get_freeze_count()   --返回永久生成中的对象数。
'''
import sys
class Test():
  def __init__(self):
    pass

t = Test()
k = Test()
t._self = t
# 会多一个 因为gc会用一个
print(sys.getrefcount(t))    #sys.getrefcount函数用来查看一个对象有几个引用
print(sys.getrefcount(k))
# del语句可以消除一个引用关系
# 引用计数为主，标记-清除+分代回收为辅的回收策略
# 专门用来处理这些循环引用
# gc.collect()

#  gc.get_threshold()
# python中默认把所有对象分成三代。
# 第0代包含了最新的对象，第2代则是最早的一些对象。
# 在一次垃圾回收中，所有未被回收的对象会被移到高一代的地方。

# 这个方法返回的是(700,10,10)，这也是gc的默认值。
# 这个值的意思是说，在第0代对象数量达到700个之前，不把未被回收的对象放入第一代；
# 而在第一代对象数量达到10个之前也不把未被回收的对象移到第二代。
# 可以是使用gc.set_threshold(threashold0,threshold1,threshold2)来手动设置这组阈值。
```

### sysconfig


```python
import sysconfig
# 解释器编译时配置
```

## 语言工具

## warnings

![](https://image.yayan.xyz/20230330103900.png)


```python
import warnings


# 报告非致命条件或可修复错误
# error把警告变成错误,simplefilter是filterwarnings简化版
warnings.simplefilter('ignore', UserWarning)
# 发出一个warnings
print('Before the warning')
warnings.warn('This is a warning message')
print('After the warning')
# filterwarnings() 根据规则过滤信息


warnings.filterwarnings('ignore', '.*do not.*',)

warnings.warn('Show this message')
warnings.warn('Do not show this message')

```

    Before the warning
    After the warning
    


```python
import warnings
warnings.simplefilter('once', UserWarning)
def warning_on_one_line(message, category, filename, lineno,
                        file=None, line=None):
    return '-> {}:{}: {}:{}\n'.format(
        filename, lineno, category.__name__, message)


warnings.warn('Warning message, before')
warnings.formatwarning = warning_on_one_line
warnings.warn('Warning message, after')

warnings.warn('This is a warning!')
warnings.warn('This is a warning!')
warnings.warn('This is a warning!')
```

    C:\Users\Ada\AppData\Local\Temp/ipykernel_9460/3571311107.py:9: UserWarning: Warning message, before
      warnings.warn('Warning message, before')
    -> C:\Users\Ada\AppData\Local\Temp/ipykernel_9460/3571311107.py:11: UserWarning:Warning message, after
    -> C:\Users\Ada\AppData\Local\Temp/ipykernel_9460/3571311107.py:13: UserWarning:This is a warning!
    

### abc

### dis


```python
import dis

# 字节码反汇编工具

def f(*args):
    nargs = len(args)
    print(nargs, args)


if __name__ == '__main__':
    import dis
    dis.dis(f)
    dis.show_code(f)


```

      6           0 LOAD_GLOBAL              0 (len)
                  2 LOAD_FAST                0 (args)
                  4 CALL_FUNCTION            1
                  6 STORE_FAST               1 (nargs)
    
      7           8 LOAD_GLOBAL              1 (print)
                 10 LOAD_FAST                1 (nargs)
                 12 LOAD_FAST                0 (args)
                 14 CALL_FUNCTION            2
                 16 POP_TOP
                 18 LOAD_CONST               0 (None)
                 20 RETURN_VALUE
    Name:              f
    Filename:          C:\Users\Ada\AppData\Local\Temp/ipykernel_9460/3862671634.py
    Argument count:    0
    Positional-only arguments: 0
    Kw-only arguments: 0
    Number of locals:  2
    Stack size:        3
    Flags:             OPTIMIZED, NEWLOCALS, VARARGS, NOFREE
    Constants:
       0: None
    Names:
       0: len
       1: print
    Variable names:
       0: args
       1: nargs
    

### inspect


```python
import inspect

# 检查现场对象,获取一个文件内的类,函数,示例,等等

# getnumbers() 发现对象的成员属性,,example是py文件

import example

for name, data in inspect.getmembers(example):
    if name.startswith('__'):
        continue
    print('{} : {!r}'.format(name, data))

```

## 模块和包

### importlib


```python
import importlib

# 运行时import

'''
├── clazz
│   ├── __init__.py
│   ├── a.py
│   └── b.py
└── main.py
a.py
def show():
    print("show A")
b.py
def show():
    print("show B")
'''

import os
import importlib

def get_modules(package="."):
    """
    获取包名下所有非__init__的模块名
    """
    modules = []
    files = os.listdir(package)
    for file in files:
        if not file.startswith("__"):
            name, ext = os.path.splitext(file)
            modules.append("." + name)
    return modules


if __name__ == '__main__':
    package = "clazz"
    modules = get_modules(package)
    # 将包下的所有模块，逐个导入，并调用其中的函数
    for module in modules:
        module = importlib.import_module(module, package)
        for attr in dir(module):
            if not attr.startswith("__"):
                func = getattr(module, attr)
                func()
    """
    show A
    show B
    """

```

### pkgutil


```python
import pkgutil

# 包扩展工具
# 一个.py文件就是一个python模块（module），如果一个目录下面有一个__init__.py文件，那么这个目录就是一个python包（package）
# 实际上包是一种特殊的模块，而任何定义了__path__属性的模块都被当做包。

iter_modules(path=None, prefix='')
# path是包的目录路径，prefix是输出时，所有包的名字的前缀。用来获取该path下的子模块或子包。
walk_packages(path=None, prefix='', onerror=None)
# 同上，但是这个方法是递归获取路径下的所有模块。

for _, name, ispkg in pkgutil.walk_packages(test.__path__, test.__name__ + "."):
    print "name: {0:12}, is_sub_package: {1}".format(name, ispkg)
```

### zipimport


```python
import zipimport

# 从zip文档中导入包
```


```python

```
