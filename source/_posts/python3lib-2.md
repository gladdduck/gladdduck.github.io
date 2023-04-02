---
title: python标准库-2
categories:
  - 学习笔记
tags:
  - python3 标准库
toc: true# 是否启用内容索引

---

## 数学模块

### decimal


```python
import decimal

# 精准的小数计算
# 可以设置精度,取值等
```

### fractions


```python
import fractions

# 分数/有理数  加减乘除正常用
# 创建  小数\字符串\整数 都行
for v in [0.1, 0.5, 1.5, 2.0]:
    print('{} = {}'.format(v, fractions.Fraction(v)))
    
for s in ['1/2', '2/4', '3/6']:
    f = fractions.Fraction(s)
    print('{} = {}'.format(s, f))
    
for s in ['0.5', '1.5', '2.0', '5e-1']:
    f = fractions.Fraction(s)
    print('{0:>4} = {1}'.format(s, f))
for n, d in [(1, 2), (2, 4), (3, 6)]:
    f = fractions.Fraction(n, d)
    print('{}/{} = {}'.format(n, d, f))
    
# 精确度
import fractions
import math

print('PI       =', math.pi)

f_pi = fractions.Fraction(str(math.pi))
print('No limit =', f_pi)

for i in [1, 6, 11, 60, 70, 90, 100]:
    limited = f_pi.limit_denominator(i)
    print('{0:8} = {1}'.format(i, limited))
```

    0.1 = 3602879701896397/36028797018963968
    0.5 = 1/2
    1.5 = 3/2
    2.0 = 2
    1/2 = 1/2
    2/4 = 1/2
    3/6 = 1/2
     0.5 = 1/2
     1.5 = 3/2
     2.0 = 2
    5e-1 = 1/2
    1/2 = 1/2
    2/4 = 1/2
    3/6 = 1/2
    PI       = 3.141592653589793
    No limit = 3141592653589793/1000000000000000
           1 = 3
           6 = 19/6
          11 = 22/7
          60 = 179/57
          70 = 201/64
          90 = 267/85
         100 = 311/99
    

### random


```python
import random

# r1=random.Random()
# r2=random.Random()
# r1r2互不影响
# random 生成一个[0,1)的小数
for i in range(5):
    print('%04.3f' % random.random(), end=' ')
print()

# 指定区间的小数
for i in range(5):
    print('{:04.3f}'.format(random.uniform(1, 100)), end=' ')
print()
```

    0.413 0.516 0.783 0.878 0.469 
    50.379 1.563 83.167 90.209 54.711 
    


```python
# 固定种子，怎么运行都是相同的数
random.seed(1)

for i in range(5):
    print('{:04.3f}'.format(random.random()), end=' ')
print()
```

    0.134 0.847 0.764 0.255 0.495 
    


```python
# 随机整数

print('[1, 100]:', end=' ')

for i in range(3):
    print(random.randint(1, 100), end=' ')

print('\n[-5, 5]:', end=' ')
for i in range(3):
    print(random.randint(-5, 5), end=' ')
print()
```

    [1, 100]: 58 61 84 
    [-5, 5]: 1 -2 -4 
    


```python
# 从序列中随机选择一个

outcomes = {
    'heads': 0,
    'tails': 0,
}
sides = list(outcomes.keys())

for i in range(10000):
    outcomes[random.choice(sides)] += 1

print('Heads:', outcomes['heads'])
print('Tails:', outcomes['tails'])


# 打乱序列

l=[i for i in range(10)]
print(f'l      :{l}')

random.shuffle(l)
print(f'shuffled l:{l}')

# 采样

samplelist=random.sample(l, 5)
print(f'sample l:{samplelist}')
```

    Heads: 4902
    Tails: 5098
    l      :[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    shuffled l:[9, 4, 8, 3, 6, 7, 0, 5, 2, 1]
    sample l:[4, 6, 9, 5, 3]
    


```python
# 非均匀分布
# 高斯分布，正态分布
random.gauss(mu=1,sigma=2)
```




    -0.21029077107544225



### math


```python
import math
# 常见常量
print('  π: {:.30f}'.format(math.pi))
print('  e: {:.30f}'.format(math.e))
print('nan: {:.30f}'.format(math.nan))
print('inf: {:.30f}'.format(math.inf))


# 判断异常值
print(math.isinf(10.0 ** 140))
print(math.isinf((10.0 ** 200)*(10.0 ** 200)))
    
# 比较,根据相对误差和绝对误差
print('='*10)
print(math.isclose(1000,900, rel_tol=0.1))
print(math.isclose(1000,900, abs_tol=0.1))


# 浮点数转整数
# trunc() 直接截断 只留整数部分
# floor() 不大于他的整数
# ceil()  数轴左侧的最小整数
import math
print('='*10)

HEADINGS = ('i', 'int', 'trunk', 'floor', 'ceil')
print('{:^5} {:^5} {:^5} {:^5} {:^5}'.format(*HEADINGS))
print('{:-^5} {:-^5} {:-^5} {:-^5} {:-^5}'.format('', '', '', '', '',))
fmt = '{:5.1f} {:5.1f} {:5.1f} {:5.1f} {:5.1f}'
TEST_VALUES = [-1.5,-0.8,-0.5,-0.2,0,0.2,0.5,0.8,1,]
for i in TEST_VALUES:
    print(fmt.format(i,int(i),math.trunc(i),math.floor(i),math.ceil(i),))
```

      π: 3.141592653589793115997963468544
      e: 2.718281828459045090795598298428
    nan: nan
    inf: inf
    False
    True
    ==========
    True
    False
    ==========
      i    int  trunk floor ceil 
    ----- ----- ----- ----- -----
     -1.5  -1.0  -1.0  -2.0  -1.0
     -0.8   0.0   0.0  -1.0   0.0
     -0.5   0.0   0.0  -1.0   0.0
     -0.2   0.0   0.0  -1.0   0.0
      0.0   0.0   0.0   0.0   0.0
      0.2   0.0   0.0   0.0   1.0
      0.5   0.0   0.0   0.0   1.0
      0.8   0.0   0.0   0.0   1.0
      1.0   1.0   1.0   1.0   1.0
    


```python
# 划分整数和小数
for i in range(6):
    print('{}/2 = {}'.format(i, math.modf(i / 2.0)))

# 排列组合数
print('{:2.0f} {:6.0f}'.format(10, math.factorial(10)))

# 浮点数精确计算
values = [0.1] * 10
print('for-loop    : {:.20f}'.format(sum(values)))
print('math.fsum() : {:.20f}'.format(math.fsum(values)))

# gcd 最大公约数
print(math.gcd(10, 8))
print(math.gcd(10, 0))
print(math.gcd(50, 225))
print(math.gcd(11, 9))
print(math.gcd(0, 0))

# 其他特殊函数
```

    0/2 = (0.0, 0.0)
    1/2 = (0.5, 0.0)
    2/2 = (0.0, 1.0)
    3/2 = (0.5, 1.0)
    4/2 = (0.0, 2.0)
    5/2 = (0.5, 2.0)
    10 3628800
    for-loop    : 0.99999999999999988898
    math.fsum() : 1.00000000000000000000
    2
    10
    25
    1
    0
    

### statistics


```python
from statistics import *

data = [1, 2, 2, 5, 10, 12]
# 均值
print('{:0.2f}'.format(mean(data)))

# 中位数
print('median     : {:0.2f}'.format(median(data)))
print('low        : {:0.2f}'.format(median_low(data)))
print('high       : {:0.2f}'.format(median_high(data)))

# 众数
print(mode(data))

# 标准差,方差
print('  pstdev    : {:6.2f}'.format(pstdev(data)))
print('  pvariance : {:6.2f}'.format(pvariance(data)))

```

    5.33
    median     : 3.50
    low        : 2.00
    high       : 5.00
    2
      pstdev    :   4.23
      pvariance :  17.89
    

## 文件系统

### os.path


```python
import os
import time
# os.path  把路径当作字符串处理
'''
# 相对路劲改为绝对路径
abspath
# 公共路径
commonpath()
# 公共前缀
commonprefix()
# 路径的最后一部分
basename
# 路径的前面的部分
dirname
# 文件是否存在
exists
# 字符串合并路径
join()
# 清除多余分隔符或者相对路径
normpath
# 把环境变量的指示符换成真正的值
expandvars

# 访问时间
getatime
# 修改时间
getmtime
# 创建时间
getctime
# 返回字节大小
getsize

'''
FILENAMES = [
    # os.path.dirname(__file__),
    'D:\BaiduSyncdisk\Blog\source',
]
for file in FILENAMES:
    print('File        : {!r}'.format(file))
    print('Absolute    :', os.path.isabs(file))
    print('Is File?    :', os.path.isfile(file))
    print('Is Dir?     :', os.path.isdir(file))
    print('Is Link?    :', os.path.islink(file))
    print('Mountpoint? :', os.path.ismount(file))
    print('Exists?     :', os.path.exists(file))
    print('Link Exists?:', os.path.lexists(file))
    print()
```

    File        : 'D:\\BaiduSyncdisk\\Blog\\source'
    Absolute    : True
    Is File?    : False
    Is Dir?     : True
    Is Link?    : False
    Mountpoint? : False
    Exists?     : True
    Link Exists?: True
    
    

### pathlib


```python
import pathlib
from pathlib import *
# 把路劲当作对象


p = Path(r'./')
# iterdir目录种的每个生成一个对象
print([x for x in p.iterdir() if x.is_dir()])
# 模式查询所有文本
print(list(p.glob('python3lib*.ipynb')))
print(p.exists())
print(p.is_dir())
# p.mkdir()
# p.rmdir() #空目录
# p.unlink() #文件等其他
# 直接用/拼接字符串
q=p/'python3lib-1.ipynb'
print(q)
# 读文件
with q.open() as f: print(f.readline())
```

    []
    [WindowsPath('python3lib-1.ipynb'), WindowsPath('python3lib-2.ipynb')]
    True
    True
    python3lib-1.ipynb
    {
    
    


```python

# Check the file types
import itertools
p = Path(r'../')
to_scan = itertools.chain(
    p.iterdir(),
)
hfmt = '{:18s}' + ('  {:>5}' * 6)
print(hfmt.format('Name', 'File', 'Dir', 'Link', 'FIFO', 'Block',
                  'Character'))
print()

fmt = '{:20s}  ' + ('{!r:>5}  ' * 6)
for f in to_scan:
    print(fmt.format(
        str(f),
        f.is_file(),
        f.is_dir(),
        f.is_symlink(),
        f.is_fifo(),
        f.is_block_device(),
        f.is_char_device(),
    ))
    
p = pathlib.Path(r'../_post')
print('path  : {}'.format(p))
print('name  : {}'.format(p.name))
print('suffix: {}'.format(p.suffix))
print('stem  : {}'.format(p.stem))
```

    Name                 File    Dir   Link   FIFO  Block  Character
    
    ..\404                False   True  False  False  False  False  
    ..\about              False   True  False  False  False  False  
    ..\books              False   True  False  False  False  False  
    ..\categories         False   True  False  False  False  False  
    ..\links              False   True  False  False  False  False  
    ..\repository         False   True  False  False  False  False  
    ..\tags               False   True  False  False  False  False  
    ..\_data              False   True  False  False  False  False  
    ..\_posts             False   True  False  False  False  False  
    path  : ..\_post
    name  : _post
    suffix: 
    stem  : _post
    


```python
p = pathlib.Path(r'./')
stat_info = p.stat()

print('{}:'.format(r'./'))
print('  Size:', stat_info.st_size)
print('  Permissions:', oct(stat_info.st_mode))
print('  Owner:', stat_info.st_uid)
print('  Device:', stat_info.st_dev)
print('  Created      :', time.ctime(stat_info.st_ctime))
print('  Last modified:', time.ctime(stat_info.st_mtime))
print('  Last accessed:', time.ctime(stat_info.st_atime))

# touch()创建一个文件或者更新修改时间
# chmod()更改权限
```

    ./:
      Size: 4096
      Permissions: 0o40777
      Owner: 0
      Device: 3527538052
      Created      : Sat Oct 22 08:58:30 2022
      Last modified: Thu Mar 16 13:20:36 2023
      Last accessed: Thu Mar 16 13:36:45 2023
    path  : ..\_post
    name  : _post
    suffix: 
    stem  : _post
    

### glob


```python
import glob

# 查找匹配,类似正则

# 只会匹配目中的所有路径,不会递归的搜索到子目录
# *匹配多个 ?匹配一个
for name in sorted(glob.glob('./*.md'))[:5]:
    print(name)


```

    .\LeetCode75.md
    .\LeetCode剑指offer1.md
    .\Linux常用命令.md
    .\Neo4j.md
    .\Neo4j安装.md
    

### fnmatch


```python
import fnmatch
import os
import pprint

pattern = 'python*.ipynb'
print('Pattern :', pattern)

files = list(sorted(os.listdir('.')))

print('\nFiles   :')
pprint.pprint(files[:5])

print('\nMatches :')
pprint.pprint(fnmatch.filter(files, pattern))

# 返回是否匹配
for name in sorted(files)[:3]:
    print('Filename: {:<25} {}'.format(
        name, fnmatch.fnmatchcase(name, pattern)))
```

    Pattern : python*.ipynb
    
    Files   :
    ['LeetCode75.md',
     'LeetCode剑指offer1.md',
     'Linux常用命令.md',
     'Neo4j.md',
     'Neo4j安装.md']
    
    Matches :
    ['python3lib-1.ipynb', 'python3lib-2.ipynb']
    Filename: LeetCode75.md             False
    Filename: LeetCode剑指offer1.md       False
    Filename: Linux常用命令.md              False
    

### linechache


```python
import linecache
# 高效读取文本文件


filename=r'D:\BaiduSyncdisk\Blog\source\_posts\第一篇博客记录.md'

# 超过回返回空字符穿
print('{!r}'.format(linecache.getline(filename, 2)))
# 读取python源文件代码
module_line = linecache.getline('linecache.py', 3)
print('MODULE:')
print(repr(module_line))
```

    'title: 第一篇博客记录\n'
    MODULE:
    'This is intended to read lines from modules imported -- hence if a filename\n'
    

### tempfile


```python
import tempfile

# 临时文件对象

import pathlib
import tempfile

# 默认是在系统的临时文件区创建import tempfile
print('gettempdir():', tempfile.gettempdir())
print('gettempprefix():', tempfile.gettempprefix())
# 关闭文件回删除,默认句柄是w+b
# TemporaryFile()没有文件名
with tempfile.NamedTemporaryFile(mode='w+t',
                                 suffix='_suffix',
                                 prefix='prefix_',
                                 dir='./') as temp:
    temp.write('Some data')
    # 回滚到前面
    temp.seek(0)
    print(temp.read())
    print('temp.name:')
    print('  {!r}'.format(temp.name))
    f = pathlib.Path(temp.name)
print('Exists after close:', f.exists())

# 临时目录

with tempfile.TemporaryDirectory() as directory_name:
    the_dir = pathlib.Path(directory_name)
    print(the_dir)
    a_file = the_dir / 'a_file.txt'
    a_file.write_text('This file is deleted.')
    print(a_file.read_text())

print('Directory exists after?', the_dir.exists())
print('Contents after:', list(the_dir.glob('*')))

```

    gettempdir(): C:\Users\Ada\AppData\Local\Temp
    gettempprefix(): tmp
    Some data
    temp.name:
      'd:\\BaiduSyncdisk\\Blog\\source\\_posts\\prefix_0iyyalif_suffix'
    Exists after close: False
    C:\Users\Ada\AppData\Local\Temp\tmpm9xfa5bw
    This file is deleted.
    Directory exists after? False
    Contents after: []
    


```python
import tempfile
# SpooledTemporaryFile 到一定阈值才写进去文件
with tempfile.SpooledTemporaryFile(max_size=1000,
                                   mode='w+t',
                                   encoding='utf-8') as temp:
    print('temp: {!r}'.format(temp.name))

    for i in range(3):
        temp.write('This line is repeated over and over.\n')
        print(temp._rolled, temp._file)
    print('rolling over')
    # 手动指定
    temp.rollover()
    print(temp._rolled, temp._file)
```

    temp: None
    False <_io.TextIOWrapper encoding='utf-8'>
    False <_io.TextIOWrapper encoding='utf-8'>
    False <_io.TextIOWrapper encoding='utf-8'>
    rolling over
    True <tempfile._TemporaryFileWrapper object at 0x000001E88C4ECE20>
    

### shutil


```python
# 高层文件操作
import glob
import shutil

print('BEFORE:', glob.glob('./doing.*'))
# 复制文件,底层函数copyfileobj()
# shutil.copyfile('./doing.ipynb', './doing.ipynb.copy')
print('AFTER:', glob.glob('./doing.*'))

# copy()如果指定目录,就会用源文件名,copy2会复制文件访问修改时间
# shutil.copy('doing.ipynb', 'example')
# 拷贝权限,和其他元素
# shutil.copymode()
# shutil.copystat()
# 拷贝目录,可以过滤某些
# shutil.copytree()
# 删除目录
# shutil.rmtree()
# 移动,如果在同目录不一样的名字就是复制,否则移动
# shutil.move()


print(shutil.which('virtualenv'))
print(shutil.which('（小区）13幢北侧垃圾亭周边袋装垃圾1处(3).jpg'))
print(shutil.which('no-such-program'))
```

    BEFORE: ['.\\doing.ipynb']
    AFTER: ['.\\doing.ipynb']
    E:\Anaconda3\envs\AAA\Scripts\virtualenv.EXE
    None
    None
    


```python
# # 压缩解压缩文件

# import logging
# import shutil
# import sys
# import tarfile

# logging.basicConfig(
#     format='%(message)s',
#     stream=sys.stdout,
#     level=logging.DEBUG,
# )
# logger = logging.getLogger('pymotw')

# print('Creating archive:')
# shutil.make_archive(
#     'example', 'gztar',
#     root_dir='..',
#     base_dir='./',
#     logger=logger,
# )

# print('\nArchive contents:')
# with tarfile.open('example.tar.gz', 'r') as t:
#     for n in t.getnames():
#         print(n)
```


```python
# import shutil
# # 解压缩文件
# for format, exts, description in shutil.get_unpack_formats('文件名'):
#     print('{:<5}: {}, names ending in {}'.format(
#         format, description, exts))
```


```python
import shutil
# 查看文件系统空间
total_b, used_b, free_b = shutil.disk_usage('.')

gib = 2 ** 30  # GiB == gibibyte
gb = 10 ** 9   # GB == gigabyte

print('Total: {:6.2f} GB  {:6.2f} GiB'.format(
    total_b / gb, total_b / gib))
print('Used : {:6.2f} GB  {:6.2f} GiB'.format(
    used_b / gb, used_b / gib))
print('Free : {:6.2f} GB  {:6.2f} GiB'.format(
    free_b / gb, free_b / gib))

```

    Total: 209.72 GB  195.31 GiB
    Used :  67.00 GB   62.40 GiB
    Free : 142.72 GB  132.92 GiB
    

### filecmp


```python
import filecmp

# shadow 是否比较文件内容
filecmp.cmp('','',shallow=True)

# 只比较当前目录,不比较内容
filecmp.dircmp('','')
```

### mmap


```python
import mmap

# 使用操作系统虚拟内存来访问数据
with open('./doing.ipynb', 'r') as f:
    with mmap.mmap(f.fileno(), 0,
                   access=mmap.ACCESS_READ) as m:
        # 指针向右移动10
        print('First 10 bytes via read :', m.read(10))
        # 分片操作符将指针移回起始位置,分片在向右移动10
        print('First 10 bytes via slice:', m[:10])
        # 再向右移动10
        print('2nd   10 bytes via read :', m.read(10))
        # m.flush() 修改
        # 单独回滚
        #  m.seek(0)  # rewind
        # f.seek(0)  # rewind
        
        
```

    First 10 bytes via read : b'{\n "cells"'
    First 10 bytes via slice: b'{\n "cells"'
    2nd   10 bytes via read : b': [\n  {\n  '
    

### codes


```python
# 编码!
# unicode
# utf-8
# assic
# ...
```

### io


```python
import io

output = io.StringIO()
output.write('This goes into the buffer. ')
# 可以替换成文件
print('And so does this.', file=output)
# Retrieve the value written
print(output.getvalue())
output.close()  # discard buffer memory

# Initialize a read buffer
input = io.StringIO('Inital value for read buffer')
# Read from the buffer
print(input.read())
```

    This goes into the buffer. And so does this.
    
    Inital value for read buffer
    


```python
output = io.BytesIO()
output.write('This goes into the buffer. '.encode('utf-8'))
output.write('ÁÇÊ'.encode('utf-8'))
# Retrieve the value written
print(output.getvalue())
output.close()  # discard buffer memory
# Initialize a read buffer
input = io.BytesIO(b'Inital value for read buffer')
# Read from the buffer
print(input.read())
```

    b'This goes into the buffer. \xc3\x81\xc3\x87\xc3\x8a'
    b'Inital value for read buffer'
    

## 数据持久存储与交换

### pickle


```python
import pickle
# 带s的是字符串
# 不带s的是文件
pickle.loads()
pickle.load()

pickle.dump()
pickle.dumps()

```

### json


```python
import json

# 带s的是字符串
# 不带s的是文件
json.loads()
json.load()

json.dump()
json.dumps()

```

### shelve,dbm


```python
import shelve
import dbm
# 类似于字典,按键访问
```

### sqlite3


```python
import sqlite3

# 进程中的嵌入式关系数据库
```

### xml


```python
from xml.etree import ElementTree
# 必须一次性遍历全部文档

# 按顺序访问所有子节点iter()

f='''<?xml version="1.0"?>
<PurchaseOrder PurchaseOrderNumber="99503" OrderDate="1999-10-20">
  <Address Type="Shipping">
    <Name>Ellen Adams</Name>
    <Street>123 Maple Street</Street>
    <City>Mill Valley</City>
    <State>CA</State>
    <Zip>10999</Zip>
    <Country>USA</Country>
  </Address>
  <Address Type="Billing">
    <Name>Tai Yee</Name>
    <Street>8 Oak Avenue</Street>
    <City>Old Town</City>
    <State>PA</State>
    <Zip>95819</Zip>
    <Country>USA</Country>
  </Address>
  <DeliveryNotes>Please leave packages in shed by driveway.</DeliveryNotes>
  <Items>
    <Item PartNumber="872-AA">
      <ProductName>Lawnmower</ProductName>
      <Quantity>1</Quantity>
      <USPrice>148.95</USPrice>
      <Comment>Confirm this is electric</Comment>
    </Item>
    <Item PartNumber="926-AA">
      <ProductName>Baby Monitor</ProductName>
      <Quantity>2</Quantity>
      <USPrice>39.98</USPrice>
      <ShipDate>1999-05-21</ShipDate>
    </Item>
  </Items>
</PurchaseOrder>'''
tree=ElementTree.fromstring(f)
# 
for item in tree.iter():
    print(item.tag)
    print(item.text)
    break
# 使用attrib.get()获取属性
for item in tree.iter('PurchaseOrder'):
    print(item.attrib.get('OrderDate'))
    print(item.attrib.items())
# findall获取所有节点
for item in tree.findall('./PurchaseOrder/Items/Item'):
    print(item.attrib.get('PartNumber'))
```

    PurchaseOrder
    
      
    1999-10-20
    dict_items([('PurchaseOrderNumber', '99503'), ('OrderDate', '1999-10-20')])
    

### csv

##  数据压缩于归档


```python
import zlib
import gzip
import bz2
import tarfile
import zipfile

```

## 加密


```python
import hashlib
# 可用加密算法
print('Guaranteed:\n{}\n'.format(
    ', '.join(sorted(hashlib.algorithms_guaranteed))))
print('Available:\n{}'.format(
    ', '.join(sorted(hashlib.algorithms_available))))

```

    Guaranteed:
    blake2b, blake2s, md5, sha1, sha224, sha256, sha384, sha3_224, sha3_256, sha3_384, sha3_512, sha512, shake_128, shake_256
    
    Available:
    blake2b, blake2s, md4, md5, md5-sha1, mdc2, ripemd160, sha1, sha224, sha256, sha384, sha3_224, sha3_256, sha3_384, sha3_512, sha512, sha512_224, sha512_256, shake_128, shake_256, sm3, whirlpool
    


```python
import hmac
```

## 使用进程、线程和协程提供并发性


```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
