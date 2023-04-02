---
title: python标准库-1
categories:
  - 学习笔记
tags:
  - python3 标准库
toc: true# 是否启用内容索引

---


```python
# help()函数查看
# https://learnku.com/docs/pymotw/date-and-time/3380
```

## 文本处理

### string


```python
import string
# 文本常量,格式化,模板
print(string.ascii_letters)
print(string.printable )
print(string.hexdigits)
print(string.octdigits)
print('{:<30}'.format('left aligned'))
print('{:0>30}'.format('right aligned'))
print('{:^30}'.format('centered'))
print('{:*^30}'.format('centered'))
print(f'{"centered":*^30}')
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
print(f"int: {42:d};  hex: {42:#x};  oct: {42:#o};  bin: {42:#b}")
 # 总是显示它符号
formatstr = '{:+f}; {:+f}'.format(3.14, -3.14) 
print(formatstr)   
# 正数前显示空格
formatstr = '{: f}; {: f}'.format(3.14, -3.14)  
print(formatstr)   
# 只显示负号 同 '{:f}; {:f}'
formatstr = '{:-f}; {:-f}'.format(3.14, -3.14)  
print(formatstr)   
```

    abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ 	
    
    0123456789abcdefABCDEF
    01234567
    left aligned                  
    00000000000000000right aligned
               centered           
    ***********centered***********
    ***********centered***********
    int: 42;  hex: 2a;  oct: 52;  bin: 101010
    int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010
    int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010
    +3.140000; -3.140000
     3.140000; -3.140000
    3.140000; -3.140000
    

### textwrap


```python
import textwrap
# 多行文本处理,格式化文本段落(缩进)
sample_text = '''
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    '''
dedented_text = textwrap.dedent(sample_text).strip()
print(dedented_text)
print()
for width in [45, 60]:
    print('{} Columns:\n'.format(width))
    print(textwrap.fill(dedented_text, width=width))
    print()


dedented_text = textwrap.dedent(sample_text).strip()
print(textwrap.fill(dedented_text,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=50,
                    ))
```

    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    
    45 Columns:
    
    The textwrap module can be used to format
    text for output in situations where pretty-
    printing is desired.  It offers programmatic
    functionality similar to the paragraph
    wrapping or filling features found in many
    text editors.
    
    60 Columns:
    
    The textwrap module can be used to format text for output in
    situations where pretty-printing is desired.  It offers
    programmatic functionality similar to the paragraph wrapping
    or filling features found in many text editors.
    
    The textwrap module can be used to format text for
        output in situations where pretty-printing is
        desired.  It offers programmatic functionality
        similar to the paragraph wrapping or filling
        features found in many text editors.
    

### re


```python
import re
# **正则表达式**

# 1.直接用re模块的函数搜索
# 2.先用compile编译，然后用编译过的搜索
# 匹配
pattern = 'this'
text = 'Does this text match the pattern?'

match = re.search(pattern, text)

s = match.start()
e = match.end()

print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(
    match.re.pattern, match.string, s, e, text[s:e]))

# 查询所有
text = 'abbaaabbbbaaaaa'

pattern = 'ab'

for match in re.findall(pattern, text):
    print('Found {!r}'.format(match))
    
text = 'This is some text -- with punctuation.'

print(text)
print()
# 组匹配
patterns = [
    (r'^(\w+)', 'word at start of string'),
    (r'(\w+)\S*$', 'word at end, with optional punctuation'),
    (r'(\bt\w+)\W+(\w+)', 'word starting with t, another word'),
    (r'(\w+t)\b', 'word ending with t'),
]

for pattern, desc in patterns:
    regex = re.compile(pattern)
    match = regex.search(text)
    print("'{}' ({})\n".format(pattern, desc))
    print('  ', match.groups())
    print()
    
# 替换
re.sub()
# 拆分
re.split()
```

    Found "this"
    in "Does this text match the pattern?"
    from 5 to 9 ("this")
    Found 'ab'
    Found 'ab'
    This is some text -- with punctuation.
    
    '^(\w+)' (word at start of string)
    
       ('This',)
    
    '(\w+)\S*$' (word at end, with optional punctuation)
    
       ('punctuation',)
    
    '(\bt\w+)\W+(\w+)' (word starting with t, another word)
    
       ('text', 'with')
    
    '(\w+t)\b' (word ending with t)
    
       ('text',)
    
    


```python
'''
*:0次或多次
+:一次或多次
?:零次或一次
{a,b}:指定出现次数
?:在重复指令后面,取消贪心模式
[ab]:匹配a或b
[^ab]:不匹配a和b
.:任意单个字符
\d:数字
\D:非数字
\s:空白符(制表符,空格,换行)
\S:非空白符
\w:字母数字
\W:非字母数字
(?<=pattern):匹配pattern开头的 (?<=exp2)exp1:查找 exp2 后面的 exp1。
(?<!pattern):不匹配pattern开头的 (?<!exp2)exp1:查找前面不是 exp2 的 exp1。
'''
```

### difflib


```python
import difflib
# 字符串比较序列
text1 = """Lorem ipsum dolor sit amet, consectetuer adipiscing
elit. Integer eu lacus accumsan arcu fermentum euismod. Donec
pulvinar porttitor tellus. Aliquam venenatis. Donec facilisis
pharetra tortor.  In nec mauris eget magna consequat
convalis. Nam sed sem vitae odio pellentesque interdum. Sed
consequat viverra nisl. Suspendisse arcu metus, blandit quis,
rhoncus ac, pharetra eget, velit. Mauris urna. Morbi nonummy
molestie orci. Praesent nisi elit, fringilla ac, suscipit non,
tristique vel, mauris. Curabitur vel lorem id nisl porta
adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate
tristique enim. Donec quis lectus a justo imperdiet tempus."""

text1_lines = text1.splitlines()

text2 = """Lorem ipsum dolor sit amet, consectetuer adipiscing
elit. Integer eu lacus accumsan arcu fermentum euismod. Donec
pulvinar, porttitor tellus. Aliquam venenatis. Donec facilisis
pharetra tortor. In nec mauris eget magna consequat
convalis. Nam cras vitae mi vitae odio pellentesque interdum. Sed
consequat viverra nisl. Suspendisse arcu metus, blandit quis,
rhoncus ac, pharetra eget, velit. Mauris urna. Morbi nonummy
molestie orci. Praesent nisi elit, fringilla ac, suscipit non,
tristique vel, mauris. Curabitur vel lorem id nisl porta
adipiscing. Duis vulputate tristique enim. Donec quis lectus a
justo imperdiet tempus.  Suspendisse eu lectus. In nunc."""

text2_lines = text2.splitlines()
d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print('\n'.join(diff))

'''
- 只在第一个文件有
+ 只在第二个文件有
  两个文件中都有
? 没有出现在两个文件中

'''
```

      Lorem ipsum dolor sit amet, consectetuer adipiscing
      elit. Integer eu lacus accumsan arcu fermentum euismod. Donec
    - pulvinar porttitor tellus. Aliquam venenatis. Donec facilisis
    + pulvinar, porttitor tellus. Aliquam venenatis. Donec facilisis
    ?         +
    
    - pharetra tortor.  In nec mauris eget magna consequat
    ?                 -
    
    + pharetra tortor. In nec mauris eget magna consequat
    - convalis. Nam sed sem vitae odio pellentesque interdum. Sed
    ?                 - --
    
    + convalis. Nam cras vitae mi vitae odio pellentesque interdum. Sed
    ?               +++ +++++   +
    
      consequat viverra nisl. Suspendisse arcu metus, blandit quis,
      rhoncus ac, pharetra eget, velit. Mauris urna. Morbi nonummy
      molestie orci. Praesent nisi elit, fringilla ac, suscipit non,
      tristique vel, mauris. Curabitur vel lorem id nisl porta
    - adipiscing. Suspendisse eu lectus. In nunc. Duis vulputate
    - tristique enim. Donec quis lectus a justo imperdiet tempus.
    + adipiscing. Duis vulputate tristique enim. Donec quis lectus a
    + justo imperdiet tempus.  Suspendisse eu lectus. In nunc.
    

## 数据结构


### enum


```python
import enum
# IntEnum支持大小比较
class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    by_design = 4
    closed = 1

# 每个东西都有一个name一个value
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))
# 如果存在多个值，下面出现的就是别名，不想出现多个值，使用@unique
print('\nSame: by_design is wont_fix: ',
      BugStatus.by_design is BugStatus.wont_fix)
print('Same: closed is fix_released: ',
      BugStatus.closed is BugStatus.fix_released)


# 空格分开，从1开始，也可以使用元组列表
BugStatus = enum.Enum(
    value='BugStatus',
    names=('fix_released fix_committed in_progress '
           'wont_fix invalid incomplete new'),
)

print('Member: {}'.format(BugStatus.new))

print('\nAll members:')
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))
```

    new             = 7
    incomplete      = 6
    invalid         = 5
    wont_fix        = 4
    in_progress     = 3
    fix_committed   = 2
    fix_released    = 1
    
    Same: by_design is wont_fix:  True
    Same: closed is fix_released:  True
    


```python
# 用元组作为值
class BugStatus(enum.Enum):
    new = (7, ['incomplete',
               'invalid',
               'wont_fix',
               'in_progress'])
    incomplete = (6, ['new', 'wont_fix'])
    invalid = (5, ['new'])
    wont_fix = (4, ['new'])
    in_progress = (3, ['new', 'fix_committed'])
    fix_committed = (2, ['in_progress', 'fix_released'])
    fix_released = (1, ['new'])

    def __init__(self, num, transitions):
        self.num = num
        self.transitions = transitions

    def can_transition(self, new_state):
        return new_state.name in self.transitions


print('Name:', BugStatus.in_progress)
print('Value:', BugStatus.in_progress.value)
print('Custom attribute:', BugStatus.in_progress.transitions)
print('Using attribute:',
      BugStatus.in_progress.can_transition(BugStatus.new))
```

    Name: BugStatus.in_progress
    Value: (3, ['new', 'fix_committed'])
    Custom attribute: ['new', 'fix_committed']
    Using attribute: True
    

### collection

#### ChainMap


```python
# ChainMap
import collections

# 相当于把几个字典装入一个列表，会按照进入列表的顺序覆盖相同值
# 修改任一个，会修改到原来的数据


a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}
# 合并多个字典
m = collections.ChainMap(a, b)

print(m.maps)
#当多个字典中有相同的key值是，默认取第一个key对应的value
print('Before: {}'.format(m['c']))
a['c'] = 'E'
print('After : {}'.format(m['c']))
print('a:', a)
# reverse the list
m.maps = list(reversed(m.maps))

print(m.maps)
print('c = {}'.format(m['c']))

```

    [{'a': 'A', 'c': 'C'}, {'b': 'B', 'c': 'D'}]
    Before: C
    After : E
    a: {'a': 'A', 'c': 'E'}
    [{'b': 'B', 'c': 'D'}, {'a': 'A', 'c': 'E'}]
    c = D
    


```python
# 搜索查询底层映射，直到一个键被找到。不同的是，写，更新和删除只操作第一个映射。
dict1= {"a":"zhangsan","b":"lisi"}
dict2= {"c":"wangwu"}

new_dict = collections.ChainMap(dict1,dict2)
print(new_dict)

new_dict1 = new_dict.new_child()
print(new_dict1)
new_dict1["x"]=0
new_dict1["y"] = 100.0
new_dict1["a"] = 666
print(new_dict1)
```

    ChainMap({'a': 'zhangsan', 'b': 'lisi'}, {'c': 'wangwu'})
    ChainMap({}, {'a': 'zhangsan', 'b': 'lisi'}, {'c': 'wangwu'})
    ChainMap({'x': 0, 'y': 100.0, 'a': 666}, {'a': 'zhangsan', 'b': 'lisi'}, {'c': 'wangwu'})
    

#### Counter


```python
import collections

# 三种构建方式1.一个元素序列，一个键值字典，关键字传参import collections

print(collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
print(collections.Counter({'a': 2, 'b': 3, 'c': 1}))
print(collections.Counter(a=2, b=3, c=1))

# 计数只会根据新数据增加，替换数据不会改变计数

c = collections.Counter()
print('Initial :', c)

c.update('abcdaab')
print('Sequence:', c)

c.update({'a': 1, 'd': 5})
print('Dict    :', c)

# 可以用字典API获取值,如果没有返回0

print(c['a'],c['666'])

# elements返回所有元素,most_common()返回前n个最多的

# 算数操作
c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
c2 = collections.Counter('alphabet')

print('C1:', c1)
print('C2:', c2)

# 计数相加
print('\nCombined counts:')
print(c1 + c2)
# 计数相减,小于0自动删除
print('\nSubtraction:')
print(c1 - c2)
# 取最小值
print('\nIntersection (taking positive minimums):')
print(c1 & c2)
# 取最大值
print('\nUnion (taking maximums):')
print(c1 | c2)
```

    Counter({'b': 3, 'a': 2, 'c': 1})
    Counter({'b': 3, 'a': 2, 'c': 1})
    Counter({'b': 3, 'a': 2, 'c': 1})
    Initial : Counter()
    Sequence: Counter({'a': 3, 'b': 2, 'c': 1, 'd': 1})
    Dict    : Counter({'d': 6, 'a': 4, 'b': 2, 'c': 1})
    4 0
    C1: Counter({'b': 3, 'a': 2, 'c': 1})
    C2: Counter({'a': 2, 'l': 1, 'p': 1, 'h': 1, 'b': 1, 'e': 1, 't': 1})
    
    Combined counts:
    Counter({'a': 4, 'b': 4, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})
    
    Subtraction:
    Counter({'b': 2, 'c': 1})
    
    Intersection (taking positive minimums):
    Counter({'a': 2, 'b': 1})
    
    Union (taking maximums):
    Counter({'b': 3, 'a': 2, 'c': 1, 'l': 1, 'p': 1, 'h': 1, 'e': 1, 't': 1})
    

#### defaultdict


```python
# 没有键时,返回函数默认值
def default_factory():
    return 'default value'


d = collections.defaultdict(default_factory, foo='bar')
print('d:', d)
print('foo =>', d['foo'])
print('bar =>', d['bar'])
```

    d: defaultdict(<function default_factory at 0x000001AA941D3DC0>, {'foo': 'bar'})
    foo => bar
    bar => default value
    

#### deque


```python
import collections
import random
# 双端队列
# list常用函数+线程安全
# append(),appendleft(),pop(),popleft()

# 可以设置最大长度,队列达到指定长度时会删除之前(队头)的元素
d1 = collections.deque(maxlen=3)
d2 = collections.deque(maxlen=3)
for i in range(5):
    n = random.randint(0, 100)
    print('n =', n)
    d1.append(n)
    d2.appendleft(n)
    print('D1:', d1)
    print('D2:', d2)

# 旋转
d = collections.deque(range(10))
print('Normal        :', d)

d = collections.deque(range(10))
d.rotate(2)
print('Right rotation:', d)

d = collections.deque(range(10))
d.rotate(-2)
print('Left rotation :', d)

```

    n = 7
    D1: deque([7], maxlen=3)
    D2: deque([7], maxlen=3)
    n = 73
    D1: deque([7, 73], maxlen=3)
    D2: deque([73, 7], maxlen=3)
    n = 34
    D1: deque([7, 73, 34], maxlen=3)
    D2: deque([34, 73, 7], maxlen=3)
    n = 56
    D1: deque([73, 34, 56], maxlen=3)
    D2: deque([56, 34, 73], maxlen=3)
    n = 79
    D1: deque([34, 56, 79], maxlen=3)
    D2: deque([79, 56, 34], maxlen=3)
    Normal        : deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    Right rotation: deque([8, 9, 0, 1, 2, 3, 4, 5, 6, 7])
    Left rotation : deque([2, 3, 4, 5, 6, 7, 8, 9, 0, 1])
    

#### namedtuple


```python
import collections

# 带有名字的元组,会返回一个有指定属性的类
# 属性名字不能是关键字,属性不能修改
Person = collections.namedtuple('Person', 'name age')

bob = Person(name='Bob', age=30)
print('Representation:', bob)
# 转为OrderedDict
print('As Dictionary:', bob._asdict())

print('\nBefore:', bob)
bob2 = bob._replace(name='Robert')
print('After:', bob2)
# 不是同一个实例
print('Same?:', bob is bob2)
```

    Representation: Person(name='Bob', age=30)
    As Dictionary: {'name': 'Bob', 'age': 30}
    
    Before: Person(name='Bob', age=30)
    After: Person(name='Robert', age=30)
    Same?: False
    

#### OrderedDict


```python
import collections
# 会记住往字典里添加的顺序import collections
# 进行比较时,不仅比较值是否相同,也比较加入顺序
d = collections.OrderedDict(
    [('a', 'A'), ('b', 'B'), ('c', 'C')]
)

print('Before:')
for k, v in d.items():
    print(k, v)

d.move_to_end('b')

print('\nmove_to_end():')
for k, v in d.items():
    print(k, v)

d.move_to_end('b', last=False)

print('\nmove_to_end(last=False):')
for k, v in d.items():
    print(k, v)
```

    Before:
    a A
    b B
    c C
    
    move_to_end():
    a A
    c C
    b B
    
    move_to_end(last=False):
    b B
    a A
    c C
    

#### collections.abc

### array数组


```python
import array


import binascii
# 返回二进制数据 data 的十六进制表示形式。 data 的每个字节都被转换为相应的2位十六进制表示形式。

a = array.array('i', range(3))
print('Initial :', a)

s = b'This is the array.'
a = array.array('b', s)
print('As byte string:', s)
print('As array      :', a)
print('As hex        :', binascii.hexlify(a))
# 与序列类似的函数
print(chr(a[0]))

```

    Initial : array('i', [0, 1, 2])
    As byte string: b'This is the array.'
    As array      : array('b', [84, 104, 105, 115, 32, 105, 115, 32, 116, 104, 101, 32, 97, 114, 114, 97, 121, 46])
    As hex        : b'54686973206973207468652061727261792e'
    T
    


```python
# 二进制转换
import array
import binascii

a = array.array('i', range(5))
print('A1:', a)

as_bytes = a.tobytes()
print(f'Byets: {as_bytes}')
print('Bytes:', binascii.hexlify(as_bytes))

a2 = array.array('i')
a2.frombytes(as_bytes)
print('A2:', a2)
```

    A1: array('i', [0, 1, 2, 3, 4])
    Byets: b'\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04\x00\x00\x00'
    Bytes: b'0000000001000000020000000300000004000000'
    A2: array('i', [0, 1, 2, 3, 4])
    


```python
# array文件转换
import array
import binascii
import tempfile

a = array.array('i', range(5))
print('A1:', a)

# Write the array of numbers to a temporary file
output = tempfile.NamedTemporaryFile()
a.tofile(output.file)  # must pass an *actual* file
output.flush()

# Read the raw data
with open(output.name, 'rb') as input:
    raw_data = input.read()
    print('Raw Contents:', binascii.hexlify(raw_data))

    # Read the data into an array
    input.seek(0)
    a2 = array.array('i')
    a2.fromfile(input, len(a))
    print('A2:', a2)
```

### heapq


```python
import heapq
# 堆排序,只有小项堆
# 用数组的形式表示堆,N的子元素位于2*N+1和2*N+2
data=[19, 9, 4, 10, 11]
print(f'original data: {data}')
# 把原数组转为堆结构数组
# 可以之间转换堆,也可以一个个往里面添加元素heappush
heapq.heapify(data)
print(f'heapify data: {data}')

# heapreplace 删除最小元素并加入一个
for n in [0, 13]:
    smallest = heapq.heapreplace(data, n)
    print('replace {:>2} with {:>2}:'.format(smallest, n))

print(f'replaced data: {data}')


# nlargest nsmallest返回前几个大/小的

# heapq.merge()合并几个有序列表
```

    original data: [19, 9, 4, 10, 11]
    heapify data: [4, 9, 19, 10, 11]
    replace  4 with  0:
    replace  0 with 13:
    replaced data: [9, 10, 19, 13, 11]
    

### bisect


```python
import bisect

values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

print('---  ---  --------')

l = []
for i in values:
    # 默认右插
    position = bisect.bisect(l, i)
    bisect.insort(l, i)    
    # position = bisect.bisect_left(l, i)
    # bisect.insort_left(l, i)
    print('{:3}  {:3}'.format(i, position), l)

```

    ---  ---  --------
     14    0 [14]
     85    1 [14, 85]
     77    1 [14, 77, 85]
     26    1 [14, 26, 77, 85]
     50    2 [14, 26, 50, 77, 85]
     45    2 [14, 26, 45, 50, 77, 85]
     66    4 [14, 26, 45, 50, 66, 77, 85]
     79    6 [14, 26, 45, 50, 66, 77, 79, 85]
     10    0 [10, 14, 26, 45, 50, 66, 77, 79, 85]
      3    0 [3, 10, 14, 26, 45, 50, 66, 77, 79, 85]
     84    9 [3, 10, 14, 26, 45, 50, 66, 77, 79, 84, 85]
     77    8 [3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]
      1    0 [1, 3, 10, 14, 26, 45, 50, 66, 77, 77, 79, 84, 85]
    

### queue


```python
import queue
# 线程安全的队列
# maxsize 是个整数，用于设置可以放入队列中的项目数的上限。
# 当达到这个大小的时候，插入操作将阻塞至队列中的项目被消费掉
# FIFO队列,普通队列
queue.Queue()
# LIFO栈
queue.LifoQueue()
# 优先队列
queue.PriorityQueue()

q = queue.PriorityQueue()

# 队列的变体，按优先级顺序（最低优先）检索打开的条目。
# 条目通常是以下格式的元组：
# 插入格式：q.put((priority number, data))

# 自定义类,实现比较方法,__eq__,__lt__
q=queue.PriorityQueue()
q.put((2, "Lisa"))
q.put((1, "Lucy"))
q.put((0, "Tom"))
while not q.empty():
    print(q.get())
```

    (0, 'Tom')
    (1, 'Lucy')
    (2, 'Lisa')
    

### struct:二进制数据结构


```python
import struct
# 将字节串解读为打包的二进制数据

# struct的pack函数把任意数据类型变成bytes
p=struct.pack('>I', 66666)
print(f'type->bytes:{p}')
# unpack把bytes变成相应的数据类型
p=struct.unpack(">I", b"\x00\x01\x04j")
print(f'bytes->type:{p}')
```

    type->bytes:b'\x00\x01\x04j'
    bytes->type:(66666,)
    

### weakref:对象的非永久引用


```python
import weakref
# 弱引用不会增加对象的引用数量。因此，弱引用不会妨碍所指对象被当作垃圾回收。
class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))
    def __str__(self) -> str:
         return 'ExpensiveObject'

def callback(reference):
    """Invoked when referenced object is deleted"""
    print('callback({!r})'.format(reference))


obj = ExpensiveObject()
r = weakref.ref(obj, callback)
# 会在finalize中提供一个对象的引用,永远不会被回收
# f = weakref.finalize(obj, on_finalize, obj)

print('obj:', obj)
print('ref:', r)
print('r():', r())

print('deleting obj')
del obj
print('r():', r())


# WeakValueDictionary： 实现的是一种可变映射，里面的值是对象的弱引用。
# 被引用的对象在程序中的其他地方被当作垃圾回收后，对应的键会自动从 WeakValueDictionary 中删除。因此，WeakValueDictionary 经常用于缓存。
# WeakValueDictionary 示例：
# WeakValueDictionary 示例：
class Cheese:
 
    def __init__(self, kind):
        self.kind = kind
 
    def __repr__(self):
        return 'Cheese(%r)' % self.kind
 
# 执行：
 
stock = weakref.WeakValueDictionary()  # 创建弱引用字典实例。
 
catalog = [Cheese('Read Leicester'), Cheese('Tilsit'),Cheese('Brie'), Cheese('Parmesan')]
 
for cheese in catalog:
   stock[cheese.kind] = cheese  # 名称映射到实例. [弱引用]
print(sorted(stock.keys()))
 
del catalog
 
print(sorted(stock.keys()) ) # 为什么还剩一个？ 因为临时变量。
 
del cheese
 
print(sorted(stock.keys()) ) # 临时变量删除后，为空.


import weakref
class C:                            # 这里新建一个类，因为WeakValueDictionary()
     def __init__(self, value):      # 要求value是一个obj
             self.value = value

def test_weak_value_dict():
     d= weakref.WeakValueDictionary() #如果d是普通字典,那么还是会print(test1)
     k1 = 'test1'                    
     v1 = C(1)                       # 这时候C(1)是有一个强引用的：v1
     d[k1] = v1                      # 这个语句也就是字典赋值，但是由于我们用的
     print(d[k1])                    # WeakValueDictionary()，所以字典里的是弱引用
     del v1                          # 这时候删除了C(1)唯一的强引用 v1，因此
     print(d[k1])                   # 会报错
```

    instance ExpensiveObject
    obj: ExpensiveObject
    ref: <weakref at 0x000001AA94201360; to 'ExpensiveObject' at 0x000001AA94117AF0>
    r(): ExpensiveObject
    deleting obj
    r(): ExpensiveObject
    ['Brie', 'Parmesan', 'Read Leicester', 'Tilsit']
    ['Parmesan']
    []
    

### copy


```python
# 浅拷贝深拷贝
import copy
import functools

# 当重载比较运算符时，可以只实现其中一两种，其他的会自动生成
@functools.total_ordering
class MyClass:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.name > other.name


a = MyClass('a')
my_list = [a]
dup = copy.copy(my_list)

print('             my_list:', my_list)
print('                 dup:', dup)
print('      dup is my_list:', (dup is my_list))
print('      dup == my_list:', (dup == my_list))
print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))


a = MyClass('a')
my_list = [a]
dup = copy.deepcopy(my_list)

print('             my_list:', my_list)
print('                 dup:', dup)
print('      dup is my_list:', (dup is my_list))
print('      dup == my_list:', (dup == my_list))
print('dup[0] is my_list[0]:', (dup[0] is my_list[0]))
print('dup[0] == my_list[0]:', (dup[0] == my_list[0]))

# 类实现,控制建立副本
# __copy()__
# __deepcopy()__
```

                 my_list: [<__main__.MyClass object at 0x000001AA940FF340>]
                     dup: [<__main__.MyClass object at 0x000001AA940FF340>]
          dup is my_list: False
          dup == my_list: True
    dup[0] is my_list[0]: True
    dup[0] == my_list[0]: True
                 my_list: [<__main__.MyClass object at 0x000001AA94208A90>]
                     dup: [<__main__.MyClass object at 0x000001AA941FFFD0>]
          dup is my_list: False
          dup == my_list: True
    dup[0] is my_list[0]: False
    dup[0] == my_list[0]: True
    


```python

class Graph:

    def __init__(self, name, connections):
        self.name = name
        self.connections = connections

    def add_connection(self, other):
        self.connections.append(other)

    def __repr__(self):
        return 'Graph(name={}, id={})'.format(
            self.name, id(self))

    def __deepcopy__(self, memo):
        print('\nCalling __deepcopy__ for {!r}'.format(self))
        if self in memo:
            existing = memo.get(self)
            print('  Already copied to {!r}'.format(existing))
            return existing
        print('  Memo dictionary:')
        if memo:
            for k, v in memo.items():
                print('    {}: {}'.format(k, v))
        else:
            print('    (empty)')
        dup = Graph(copy.deepcopy(self.name, memo), [])
        print('  Copying to new object {}'.format(dup))
        memo[self] = dup
        for c in self.connections:
            dup.add_connection(copy.deepcopy(c, memo))
        return dup

# memo字典跟踪已复制的对象避免递归
root = Graph('root', [])
a = Graph('a', [root])
b = Graph('b', [a, root])
root.add_connection(a)
root.add_connection(b)

dup = copy.deepcopy(root)

```

### pprint


```python
import pprint
# 美观打印
data = [
    (1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
    (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
         'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}),
    (3, ['m', 'n']),
    (4, ['o', 'p', 'q']),
    (5, ['r', 's', 't''u', 'v', 'x', 'y', 'z']),
]

print(data)
# depth可以控制打印深度,width控制打印宽度,compact会尝试更加紧凑
pprint.pprint(data,compact=True)
```

    [(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}), (2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}), (3, ['m', 'n']), (4, ['o', 'p', 'q']), (5, ['r', 's', 'tu', 'v', 'x', 'y', 'z'])]
    [(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
     (2,
      {'e': 'E',
       'f': 'F',
       'g': 'G',
       'h': 'H',
       'i': 'I',
       'j': 'J',
       'k': 'K',
       'l': 'L'}),
     (3, ['m', 'n']), (4, ['o', 'p', 'q']),
     (5, ['r', 's', 'tu', 'v', 'x', 'y', 'z'])]
    


```python
import logging
from pprint import pformat

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s %(message)s',
)

logging.debug('Logging pformatted data')
# 格式化转成字符串
formatted = pformat(data)
for line in formatted.splitlines():
    logging.debug(line.rstrip())
    # print(line.rstrip())

# 递归打印
local_data = ['a', 'b', 1, 2]
local_data.append(local_data)

print('id(local_data) =>', id(local_data))
pprint.pprint(local_data)
print(local_data)
```

    DEBUG    Logging pformatted data
    DEBUG    [(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
    DEBUG     (2,
    DEBUG      {'e': 'E',
    DEBUG       'f': 'F',
    DEBUG       'g': 'G',
    DEBUG       'h': 'H',
    DEBUG       'i': 'I',
    DEBUG       'j': 'J',
    DEBUG       'k': 'K',
    DEBUG       'l': 'L'}),
    DEBUG     (3, ['m', 'n']),
    DEBUG     (4, ['o', 'p', 'q']),
    DEBUG     (5, ['r', 's', 'tu', 'v', 'x', 'y', 'z'])]
    

    id(local_data) => 1832127417216
    ['a', 'b', 1, 2, <Recursion on list with id=1832127417216>]
    ['a', 'b', 1, 2, [...]]
    

## 算法

### functools:管理函数的工具

#### partial


```python
from functools import partial
# 将一个函数的部分参数预先绑定为某些值，从而得到一个新的具有较少可变参数的函数


# 普通函数
def add(a,b,*args, **kwargs):
    print(f'a:{a},  b:{b}')
    # 打印位置参数
    for n in args:
        print(n)
    print("-"*20)
    # 打印关键字参数
    for k, v in kwargs.items():
       print('%s:%s' % (k, v))
    print("-"*20)

# 普通调用
add(1, 2, 3, v1=10, v2=20)


# partial的参数会先占用函数前面的参数,后面传的会依次当作后面的形参
add_partial = partial(add, 10, k1=10, k2=20)
add_partial(1, 2, 3, k3=20)
add_partial(1, 2, 3, k1=20)
```

    a:1,  b:2
    3
    --------------------
    v1:10
    v2:20
    --------------------
    a:10,  b:1
    2
    3
    --------------------
    k1:10
    k2:20
    k3:20
    --------------------
    a:10,  b:1
    2
    3
    --------------------
    k1:20
    k2:20
    --------------------
    


```python
# partialmethod和partial实现相同的功能，只是 partial在类方法中使用会报错，而此函数用在类方法中；
from functools import partialmethod

class Cell(object):
    def __init__(self):
        self._alive = False
    @property
    def alive(self):
        return self._alive
    def set_state(self, state):
        self._alive = bool(state)
    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)
 
c = Cell()
c.alive # 结果为:False
 
c.set_alive()
c.alive # 结果为:True



def standalone(self, a=1, b=2):
    print('  called standalone with:', (self, a, b))
    if self is not None:
        print('  self.attr =', self.attr)


class MyClass:
    def __init__(self):
        self.attr = 'instance attribute'

    method1 = partialmethod(standalone)
    method2 = partial(standalone)


o = MyClass()

print('standalone')
standalone(None)
print()
# 可以把对象传进去
print('method1 as partialmethod')
o.method1()
print()
# 穿不进去对象
print('method2 as partial')
try:
    o.method2()
except TypeError as err:
    print('ERROR: {}'.format(err))
```

    standalone
      called standalone with: (None, 1, 2)
    
    method1 as partialmethod
      called standalone with: (<__main__.MyClass object at 0x0000021B97BA8B80>, 1, 2)
      self.attr = instance attribute
    
    method2 as partial
    ERROR: standalone() missing 1 required positional argument: 'self'
    

#### 富比较


```python
import functools
import inspect
from pprint import pprint
'''
大于 >  __gt__()
大于等于 >=  __ge__()
等于 ==  __eq__()
小于 <  __lt__()
小于等于 <=  __le__()
不等于 != __ne()__
'''



@functools.total_ordering
class MyObject:

    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        print('  testing __eq__({}, {})'.format(
            self.val, other.val))
        return self.val == other.val

    def __gt__(self, other):
        print('  testing __gt__({}, {})'.format(
            self.val, other.val))
        return self.val > other.val


print('Methods:\n')
pprint(inspect.getmembers(MyObject, inspect.isfunction))

a = MyObject(1)
b = MyObject(2)

print('\nComparisons:')
for expr in ['a < b', 'a <= b', 'a == b', 'a >= b', 'a > b']:
    print('\n{:<6}:'.format(expr))
    result = eval(expr)
    print('  result of {}: {}'.format(expr, result))
    

```

    Methods:
    
    [('__eq__', <function MyObject.__eq__ at 0x0000021B998A7940>),
     ('__ge__', <function _ge_from_gt at 0x0000021B932024C0>),
     ('__gt__', <function MyObject.__gt__ at 0x0000021B998A70D0>),
     ('__init__', <function MyObject.__init__ at 0x0000021B998A79D0>),
     ('__le__', <function _le_from_gt at 0x0000021B93202550>),
     ('__lt__', <function _lt_from_gt at 0x0000021B93202430>)]
    
    Comparisons:
    
    a < b :
      testing __gt__(1, 2)
      testing __eq__(1, 2)
      result of a < b: True
    
    a <= b:
      testing __gt__(1, 2)
      result of a <= b: True
    
    a == b:
      testing __eq__(1, 2)
      result of a == b: False
    
    a >= b:
      testing __gt__(1, 2)
      testing __eq__(1, 2)
      result of a >= b: False
    
    a > b :
      testing __gt__(1, 2)
      result of a > b: False
    


```python
# cmp_to_key将 Python 2 程序转换至新版的转换工具，以保持对比较函数的兼容。
'''
key 参数：Python 3 支持，接受的函数（入参为每个元素）返回值（对这个元素的计算），表示此元素的权值，sorted 将按照权值大小进行排序
cmp 参数：Python 2 支持，接受的函数是元素中的所有需要对比的两个元素，这个函数定义大于（一般返回1）、小于（-1）、等于逻辑（1），最后根据这些比较逻辑排序

'''

from functools import cmp_to_key

def mycmp(a, b):
    # 提取字符中的数字
    a = int(''.join([i for i in a if i.isdigit()]))
    b = int(''.join([i for i in b if i.isdigit()]))

    if a > b:
        print(a, "vs", b, '=' , 1)
        return 1
    elif a < b:
        print(a, "vs", b, '=' , -1)
        return -1
    else:
        print(a, "vs", b, '=' , 0)
        return 0

print(sorted(['b29s', 'c2s20', 'a1-1', '88d'], key=cmp_to_key(mycmp)))
print(sorted(['b29s', 'c2s20', 'a1-1', '88d'], key=lambda x: int(''.join([i for i in x if i.isdigit()]))))
```

    220 vs 29 = 1
    11 vs 220 = -1
    11 vs 220 = -1
    11 vs 29 = -1
    88 vs 29 = 1
    88 vs 220 = -1
    ['a1-1', 'b29s', '88d', 'c2s20']
    ['a1-1', 'b29s', '88d', 'c2s20']
    

#### 缓存


```python
import functools

# maxsize 设置最大缓存量
# 最近最少使用
@functools.lru_cache()
# @functools.cache()
# cache不需要移出旧值，缓存大小没有限制
# return lru_cache(maxsize=None)(user_function)
def expensive(a, b):
    # 参数必须是可散列的
    print('expensive({}, {})'.format(a, b))
    return a * b

MAX = 2

print('First set of calls:')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())
print('\nSecond set of calls:')
for i in range(MAX + 1):
    for j in range(MAX + 1):
        expensive(i, j)
print(expensive.cache_info())
print('\nClearing cache:')
expensive.cache_clear()
print(expensive.cache_info())
print('\nThird set of calls:')
for i in range(MAX):
    for j in range(MAX):
        expensive(i, j)
print(expensive.cache_info())
```

    First set of calls:
    expensive(0, 0)
    expensive(0, 1)
    expensive(1, 0)
    expensive(1, 1)
    CacheInfo(hits=0, misses=4, maxsize=128, currsize=4)
    
    Second set of calls:
    expensive(0, 2)
    expensive(1, 2)
    expensive(2, 0)
    expensive(2, 1)
    expensive(2, 2)
    CacheInfo(hits=4, misses=9, maxsize=128, currsize=9)
    
    Clearing cache:
    CacheInfo(hits=0, misses=0, maxsize=128, currsize=0)
    
    Third set of calls:
    expensive(0, 0)
    expensive(0, 1)
    expensive(1, 0)
    expensive(1, 1)
    CacheInfo(hits=0, misses=4, maxsize=128, currsize=4)
    

#### 缩减


```python
import functools
from functools import reduce
# def reduce(function, iterable, initializer=None):
#     it = iter(iterable)
#     if initializer is None:
#         value = next(it)
#     else:
#         value = initializer
#     for element in it:
#         value = function(value, element)
#     return value


# 是计算 ((((1+2)+3)+4)+5) 的值,前缀和
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) )

# 默认参数放第一个initializer
def do_reduce(a, b):
    print('do_reduce({}, {})'.format(a, b))
    return a + b

data = range(1, 5)
print(data)
result = functools.reduce(do_reduce, data, 999)
print('result: {}'.format(result))
```

    15
    range(1, 5)
    do_reduce(999, 1)
    do_reduce(1000, 2)
    do_reduce(1002, 3)
    do_reduce(1005, 4)
    result: 1009
    

#### 泛型函数


```python
import functools
# 不同的类型进不同的函数,根据参数的第一个参数切换函数

@functools.singledispatch
def myfunc(arg):
    print('default myfunc({!r})'.format(arg))


@myfunc.register(int)
def myfunc_int(arg):
    print('myfunc_int({})'.format(arg))


@myfunc.register(list)
def myfunc_list(arg):
    print('myfunc_list()')
    for item in arg:
        print('  {}'.format(item))

@myfunc.register
def myfunc_list(arg: float):
    print('myfunc_float({})'.format(arg))


# 找不到匹配的类型会计算继承顺序,匹配最近的父类
myfunc('string argument')
myfunc(1)
myfunc(2.3)
myfunc(['a', 'b', 'c'])
```

    default myfunc('string argument')
    myfunc_int(1)
    myfunc_float(2.3)
    myfunc_list()
      a
      b
      c
    

### itertools:迭代器函数

#### chain


```python
# 在消费数据之前不从迭代器生成数据
from itertools import chain


for i in chain([1, 2, 3], ['a', 'b', 'c']):
    print(i, end=' ')
print()

def make_iterables_to_chain():
    yield [1, 2, 3]
    yield ['a', 'b', 'c']


for i in chain.from_iterable(make_iterables_to_chain()):
    print(i, end=' ')
print()
```

    1 2 3 a b c 
    1 2 3 a b c 
    

#### zip_longest


```python
from itertools import zip_longest

r1 = range(3)
r2 = range(2)

print('zip stops early:')
print(list(zip(r1, r2)))

r1 = range(3)
r2 = range(2)

print('\nzip_longest processes all of the values:')
print(list(zip_longest(r1, r2)))

print(list(zip_longest(r1, r2,fillvalue=6666)))
```

    zip stops early:
    [(0, 0), (1, 1)]
    
    zip_longest processes all of the values:
    [(0, 0), (1, 1), (2, None)]
    [(0, 0), (1, 1), (2, 6666)]
    

#### islice


```python
from itertools import islice
print('Stop at 5:')
for i in islice(range(100), 5):
    print(i, end=' ')
print('\n')

print('Start at 5, Stop at 10:')
for i in islice(range(100), 5, 10):
    print(i, end=' ')
print('\n')

print('By tens to 100:')
for i in islice(range(100), 0, 100, 10):
    print(i, end=' ')
print('\n')
```

    Stop at 5:
    0 1 2 3 4 
    
    Start at 5, Stop at 10:
    5 6 7 8 9 
    
    By tens to 100:
    0 10 20 30 40 50 60 70 80 90 
    
    

#### tee

#### map,starmap


```python
def times_two(x):
    return 2 * x


def multiply(x, y):
    return (x, y, x * y)


print('Doubles:')
for i in map(times_two, range(5)):
    print(i,end=' ')

print('\nMultiples:')
r1 = range(5)
r2 = range(5, 10)
for i in map(multiply, r1, r2):
    print('{:d} * {:d} = {:d}'.format(*i))
# 只运行完最短的
print('\nStopping:')
r1 = range(5)
r2 = range(2)
for i in map(multiply, r1, r2):
    print(i)

from itertools import starmap
# map 传入的函数为f(x,y) starmap传入的函数为f(*x)
values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]

for i in starmap(lambda x,y: (x*y,x,y), values):
    print('{} * {} = {}'.format(*i))
```

    Doubles:
    0 2 4 6 8 
    Multiples:
    0 * 5 = 0
    1 * 6 = 6
    2 * 7 = 14
    3 * 8 = 24
    4 * 9 = 36
    
    Stopping:
    (0, 0, 0)
    (1, 1, 1)
    0 * 0 = 5
    6 * 1 = 6
    14 * 2 = 7
    24 * 3 = 8
    36 * 4 = 9
    

#### count,cycle,repear


```python
from itertools import count,repeat,cycle

# count无限产生值
for i in zip(count(start=1, step=10), ['a', 'b', 'c']):
    print('{}: {}'.format(*i))

# cycle无限重复值 
for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)

# repear重复n次值,不提供就是无限 
for i in repeat([1,2,3,4], 5):
    print(i)
    
# 组合
for i, s in zip(count(), repeat('over-and-over', 5)):
    print(i, s)
    
for i in map(lambda x, y: (x, y, x * y), repeat(2), range(5)):
    print('{:d} * {:d} = {:d}'.format(*i))
```

    1: a
    11: b
    21: c
    (0, 'a')
    (1, 'b')
    (2, 'c')
    (3, 'a')
    (4, 'b')
    (5, 'c')
    (6, 'a')
    [1, 2, 3, 4]
    [1, 2, 3, 4]
    [1, 2, 3, 4]
    [1, 2, 3, 4]
    [1, 2, 3, 4]
    0 over-and-over
    1 over-and-over
    2 over-and-over
    3 over-and-over
    4 over-and-over
    2 * 0 = 0
    2 * 1 = 2
    2 * 2 = 4
    2 * 3 = 6
    2 * 4 = 8
    

#### dropwhile,takewhile,filter,filterfalse,compress


```python
from itertools import dropwhile,takewhile,filterfalse,compress
def should_drop(x):
    print('Testing:', x)
    return x < 1
# 第一次为false之后的元素都会返回
for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)
print('------------------------')


def should_take(x):
    print('Testing:', x)
    return x < 2
# 第一次为false之前的元素都会返回,遇见false就不返回了
for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)
print('------------------------')

# 只返回true的元素,每一个都会计算
def check_item(x):
    print('Testing:', x)
    return x < 1
for i in filter(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)
print('------------------------')


# 相反
def check_item(x):
    print('Testing:', x)
    return x < 1
for i in filterfalse(check_item, [-1, 0, 1, 2, -2]):
    print('Yielding:', i)
print('------------------------')

# 根据true和false选择数据
every_third = cycle([False, False, True])
data = range(1, 10)

for i in compress(data, every_third):
    print(i, end=' ')
print()

```

    Testing: -1
    Testing: 0
    Testing: 1
    Yielding: 1
    Yielding: 2
    Yielding: -2
    ------------------------
    Testing: -1
    Yielding: -1
    Testing: 0
    Yielding: 0
    Testing: 1
    Yielding: 1
    Testing: 2
    ------------------------
    Testing: -1
    Yielding: -1
    Testing: 0
    Yielding: 0
    Testing: 1
    Testing: 2
    Testing: -2
    Yielding: -2
    ------------------------
    Testing: -1
    Testing: 0
    Testing: 1
    Yielding: 1
    Testing: 2
    Yielding: 2
    Testing: -2
    ------------------------
    3 6 9 
    

#### groupby


```python
from itertools import groupby

d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
d = [(1,2),(2,3),(3,4),(4,2)]
di = sorted(d, key=lambda x:x[1])
for k, g in groupby(di, key=lambda x:x[1]):
    print(k, list(map(lambda x:x[1], g)))
```

    2 [2, 2]
    3 [3]
    4 [4]
    

#### accumulate


```python
from itertools import accumulate

# 计算累计和
print(list(accumulate(range(5))))
print(list(accumulate('abcde')))

def f(a, b):
    print(a, b)
    return b + a + b

print(list(accumulate('abcde', f)))
```

    [0, 1, 3, 6, 10]
    ['a', 'ab', 'abc', 'abcd', 'abcde']
    a b
    bab c
    cbabc d
    dcbabcd e
    ['a', 'bab', 'cbabc', 'dcbabcd', 'edcbabcde']
    

#### product


```python
from itertools import product
# 笛卡尔积

FACE_CARDS = ('J', 'Q', 'K', 'A')
SUITS = ('H', 'D', 'C', 'S')

# 顺序由输入顺序决定
DECK = list(
    product(
        chain(range(2, 11), FACE_CARDS),
        SUITS,
    )
)

for card in DECK:
    print('{:>2}{}'.format(*card), end=' ')
    if card[1] == SUITS[-1]:
        print()
        
        
# repear控制几个自身
def show(iterable):
    for i, item in enumerate(iterable, 1):
        print(item, end=' ')
        if (i % 3) == 0:
            print()
    print()


print('Repeat 2:\n')
show(list(product(range(3), repeat=2)))

print('Repeat 3:\n')
show(list(product(range(3), repeat=3)))
```

     2H  2D  2C  2S 
     3H  3D  3C  3S 
     4H  4D  4C  4S 
     5H  5D  5C  5S 
     6H  6D  6C  6S 
     7H  7D  7C  7S 
     8H  8D  8C  8S 
     9H  9D  9C  9S 
    10H 10D 10C 10S 
     JH  JD  JC  JS 
     QH  QD  QC  QS 
     KH  KD  KC  KS 
     AH  AD  AC  AS 
    Repeat 2:
    
    (0, 0) (0, 1) (0, 2) 
    (1, 0) (1, 1) (1, 2) 
    (2, 0) (2, 1) (2, 2) 
    
    Repeat 3:
    
    (0, 0, 0) (0, 0, 1) (0, 0, 2) 
    (0, 1, 0) (0, 1, 1) (0, 1, 2) 
    (0, 2, 0) (0, 2, 1) (0, 2, 2) 
    (1, 0, 0) (1, 0, 1) (1, 0, 2) 
    (1, 1, 0) (1, 1, 1) (1, 1, 2) 
    (1, 2, 0) (1, 2, 1) (1, 2, 2) 
    (2, 0, 0) (2, 0, 1) (2, 0, 2) 
    (2, 1, 0) (2, 1, 1) (2, 1, 2) 
    (2, 2, 0) (2, 2, 1) (2, 2, 2) 
    
    

#### permutations,combinations


```python
from itertools import permutations,combinations,combinations_with_replacement
def show(iterable):
    first = None
    for i, item in enumerate(iterable, 1):
        if first != item[0]:
            if first is not None:
                print()
            first = item[0]
        print(''.join(item), end=' ')
    print()

# 排列
print('All permutations:\n')
show(permutations('abcd'))

print('\nPairs:\n')
show(permutations('abcd', r=2))

# 组合
print('\nUnique pairs:\n')
show(combinations('abcd', r=2))
# 包含自身
print('\nUnique pairs:\n')
show(combinations_with_replacement('abcd', r=2))
```

    All permutations:
    
    abcd abdc acbd acdb adbc adcb 
    bacd badc bcad bcda bdac bdca 
    cabd cadb cbad cbda cdab cdba 
    dabc dacb dbac dbca dcab dcba 
    
    Pairs:
    
    ab ac ad 
    ba bc bd 
    ca cb cd 
    da db dc 
    
    Unique pairs:
    
    ab ac ad 
    bc bd 
    cd 
    
    Unique pairs:
    
    aa ab ac ad 
    bb bc bd 
    cc cd 
    dd 
    

### operator:内置操作符的函数结构


```python
from operator import *

# 关键字的函数实现

a = -1
b = 5

print('a =', a)
print('b =', b)
print()

print('not_(a)     :', not_(a))
print('truth(a)    :', truth(a))
print('is_(a, b)   :', is_(a, b))
print('is_not(a, b):', is_not(a, b))
for func in (lt, le, eq, ne, ge, gt):
    print('{}(a, b): {}'.format(func.__name__, func(a, b)))
```

    a = -1
    b = 5
    
    not_(a)     : False
    truth(a)    : True
    is_(a, b)   : False
    is_not(a, b): True
    lt(a, b): True
    le(a, b): True
    eq(a, b): False
    ne(a, b): True
    ge(a, b): False
    gt(a, b): False
    


```python
class MyObj:
    """example class for attrgetter"""

    def __init__(self, arg):
        super().__init__()
        self.arg = arg

    def __repr__(self):
        return 'MyObj({})'.format(self.arg)


l = [MyObj(i) for i in range(5)]
print('objects   :', l)

# Extract the 'arg' value from each object
g = attrgetter('arg')
vals = [g(i) for i in l]
print('arg values:', vals)

# Sort using arg
l.reverse()
print('reversed  :', l)
print('sorted    :', sorted(l, key=g))
```

    objects   : [MyObj(0), MyObj(1), MyObj(2), MyObj(3), MyObj(4)]
    arg values: [0, 1, 2, 3, 4]
    reversed  : [MyObj(4), MyObj(3), MyObj(2), MyObj(1), MyObj(0)]
    sorted    : [MyObj(0), MyObj(1), MyObj(2), MyObj(3), MyObj(4)]
    

### contextlib:上下文管理器工具


```python
class WithinContext:

    def __init__(self, context):
        print('WithinContext.__init__({})'.format(context))

    def do_something(self):
        print('WithinContext.do_something()')

    def __del__(self):
        print('WithinContext.__del__')

class Context:

    def __init__(self, handle_error):
        print('__init__({})'.format(handle_error))
        self.handle_error = handle_error

    def __enter__(self):
        print('Context.__enter__()')
        # 此处返回作为as使用
        return WithinContext(self)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__()')
        print('  exc_type =', exc_type)
        print('  exc_val  =', exc_val)
        print('  exc_tb   =', exc_tb)
        # 返回true就不继续传递,返回false继续传递
        return self.handle_error


with Context(False) as c:
    c.do_something()
print('---------------')
with Context(True):
    raise RuntimeError('error message handled')
```

    __init__(False)
    Context.__enter__()
    WithinContext.__init__(<__main__.Context object at 0x0000021B997DA3D0>)
    WithinContext.__del__
    WithinContext.do_something()
    __exit__()
      exc_type = None
      exc_val  = None
      exc_tb   = None
    ---------------
    __init__(True)
    Context.__enter__()
    WithinContext.__init__(<__main__.Context object at 0x0000021B997DA3D0>)
    WithinContext.__del__
    __exit__()
      exc_type = <class 'RuntimeError'>
      exc_val  = error message handled
      exc_tb   = <traceback object at 0x0000021B998C7D80>
    


```python
import time
from contextlib import contextmanager

@contextmanager
def timethis(label):
    start = time.time()
    # yield 之前的代码会在上下文管理器中作为 __enter__() 方法执行
    # 所有在 yield 之后的代码会作为 __exit__() 方法执行
    # 如果出现了异常，异常会在yield语句那里抛出。
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))

# Example use
with timethis('counting'):
    n = 10000000
    while n > 0:
        n -= 1
```

    counting: 0.678372859954834
    

## 日期和时间

### time



```python
import time

# 报告系统挂钟时间,返回某一时刻的秒数
print(time.time())

# monotonic()递增函数,time可能因为系统时间后退
# monotonic的起始时间无意义,主要是差值
print(time.monotonic())

# perf_counter高分辨率时钟
print(time.perf_counter())

# process_time处理器处理时间
print(time.process_time())

# ctime 返回人能看懂的时间字符串,默认返回当前时间
print(time.ctime())
print(time.ctime(time.time()+20))


# 返回当前时间的结构化时间
print(time.localtime())

# 返回UTC时区的结构化时间
print(time.gmtime())

# 把结构化时间转化为浮点秒数
print(time.mktime(time.localtime()))

# 处理时区问题

# 字符串时间转为结构化时间
print(time.strptime(time.ctime()))


# 结构化时间转化为指定格式
print(time.strftime(r"%Y-%m-%d %H:%M:%S",time.localtime()))
```

    1678199761.7579758
    951660.75
    644.1160248
    3.59375
    Tue Mar  7 22:36:01 2023
    Tue Mar  7 22:36:21 2023
    time.struct_time(tm_year=2023, tm_mon=3, tm_mday=7, tm_hour=22, tm_min=36, tm_sec=1, tm_wday=1, tm_yday=66, tm_isdst=0)
    time.struct_time(tm_year=2023, tm_mon=3, tm_mday=7, tm_hour=14, tm_min=36, tm_sec=1, tm_wday=1, tm_yday=66, tm_isdst=0)
    1678199761.0
    time.struct_time(tm_year=2023, tm_mon=3, tm_mday=7, tm_hour=22, tm_min=36, tm_sec=1, tm_wday=1, tm_yday=66, tm_isdst=-1)
    2023-03-07 22:36:01
    


```python
import textwrap
import time

available_clocks = [
    ('monotonic', time.monotonic),
    ('perf_counter', time.perf_counter),
    ('process_time', time.process_time),
    ('time', time.time),
]

for clock_name, func in available_clocks:
    print(textwrap.dedent('''\
    {name}:
        adjustable    : {info.adjustable}
        implementation: {info.implementation}
        monotonic     : {info.monotonic}
        resolution    : {info.resolution}
        current       : {current}
    ''').format(
        name=clock_name,
        info=time.get_clock_info(clock_name),
        current=func())
    )
```

    monotonic:
        adjustable    : False
        implementation: GetTickCount64()
        monotonic     : True
        resolution    : 0.015625
        current       : 951073.281
    
    perf_counter:
        adjustable    : False
        implementation: QueryPerformanceCounter()
        monotonic     : True
        resolution    : 1e-07
        current       : 56.6460748
    
    process_time:
        adjustable    : False
        implementation: GetProcessTimes()
        monotonic     : True
        resolution    : 1e-07
        current       : 2.59375
    
    time:
        adjustable    : True
        implementation: GetSystemTimeAsFileTime()
        monotonic     : False
        resolution    : 0.015625
        current       : 1678199174.288961
    
    

### datetime


```python
import datetime
# 获取年月日等
today = datetime.date.today()
print(today)
print('ctime  :', today.ctime())
tt = today.timetuple()
print('tuple  : tm_year  =', tt.tm_year)
print('         tm_mon   =', tt.tm_mon)
print('         tm_mday  =', tt.tm_mday)
print('         tm_hour  =', tt.tm_hour)
print('         tm_min   =', tt.tm_min)
print('         tm_sec   =', tt.tm_sec)
print('         tm_wday  =', tt.tm_wday)
print('         tm_yday  =', tt.tm_yday)
print('         tm_isdst =', tt.tm_isdst)
print('ordinal:', today.toordinal())
print('Year   :', today.year)
print('Mon    :', today.month)
print('Day    :', today.day)
```

    2023-03-07
    ctime  : Tue Mar  7 00:00:00 2023
    tuple  : tm_year  = 2023
             tm_mon   = 3
             tm_mday  = 7
             tm_hour  = 0
             tm_min   = 0
             tm_sec   = 0
             tm_wday  = 1
             tm_yday  = 66
             tm_isdst = -1
    ordinal: 738586
    Year   : 2023
    Mon    : 3
    Day    : 7
    


```python
import datetime
import time
# 根据天数返回日期
o = 733114
print('o               :', o)
print('fromordinal(o)  :', datetime.date.fromordinal(o))

t = time.time()
print('t               :', t)
print('fromtimestamp(t):', datetime.date.fromtimestamp(t))
```

    o               : 733114
    fromordinal(o)  : 2008-03-13
    t               : 1678199846.9677696
    fromtimestamp(t): 2023-03-07
    


```python
import datetime

# 获取时间对应秒数
for delta in [datetime.timedelta(microseconds=1),
              datetime.timedelta(milliseconds=1),
              datetime.timedelta(seconds=1),
              datetime.timedelta(minutes=1),
              datetime.timedelta(hours=1),
              datetime.timedelta(days=1),
              datetime.timedelta(weeks=1),
              ]:
    print('{:15} = {:8} seconds'.format(
        str(delta), delta.total_seconds())
    )
```

    0:00:00.000001  =    1e-06 seconds
    0:00:00.001000  =    0.001 seconds
    0:00:01         =      1.0 seconds
    0:01:00         =     60.0 seconds
    1:00:00         =   3600.0 seconds
    1 day, 0:00:00  =  86400.0 seconds
    7 days, 0:00:00 = 604800.0 seconds
    


```python
import datetime
# 时间的计算
today = datetime.date.today()
print('Today    :', today)

one_day = datetime.timedelta(days=1)
print('One day  :', one_day)

yesterday = today - one_day
print('Yesterday:', yesterday)

tomorrow = today + one_day
print('Tomorrow :', tomorrow)

print()
print('tomorrow - yesterday:', tomorrow - yesterday)
print('yesterday - tomorrow:', yesterday - tomorrow)
```


```python
import datetime
import time
# 时间比较
print('Times:')
t1 = datetime.time(12, 55, 0)
print('  t1:', t1)
t2 = datetime.time(13, 5, 0)
print('  t2:', t2)
print('  t1 < t2:', t1 < t2)

print()
print('Dates:')
d1 = datetime.date.today()
print('  d1:', d1)
d2 = datetime.date.today() + datetime.timedelta(days=1)
print('  d2:', d2)
print('  d1 > d2:', d1 > d2)
```


```python
import datetime
# 时间和日期组合在一起
print('Now    :', datetime.datetime.now())
print('Today  :', datetime.datetime.today())
print('UTC Now:', datetime.datetime.utcnow())
print()

FIELDS = [
    'year', 'month', 'day',
    'hour', 'minute', 'second',
    'microsecond',
]

d = datetime.datetime.now()
for attr in FIELDS:
    print('{:15}: {}'.format(attr, getattr(d, attr)))
```

    Now    : 2023-03-07 22:41:14.718075
    Today  : 2023-03-07 22:41:14.718076
    UTC Now: 2023-03-07 14:41:14.718075
    
    year           : 2023
    month          : 3
    day            : 7
    hour           : 22
    minute         : 41
    second         : 14
    microsecond    : 719073
    


```python
import datetime
# 日期格式化
format = "%a %b %d %H:%M:%S %Y"

today = datetime.datetime.today()
print('ISO     :', today)

s = today.strftime(format)
print('strftime:', s)

d = datetime.datetime.strptime(s, format)
print('strptime:', d.strftime(format))
```

    ISO     : 2023-03-07 22:40:31.254463
    strftime: Tue Mar 07 22:40:31 2023
    strptime: Tue Mar 07 22:40:31 2023
    

### 日期操作


```python
import calendar
# 设置星期一是第一天还是星期天是第一天
c = calendar.TextCalendar(calendar.MONDAY)
c.prmonth(2023, 3)
```

         March 2023
    Mo Tu We Th Fr Sa Su
           1  2  3  4  5
     6  7  8  9 10 11 12
    13 14 15 16 17 18 19
    20 21 22 23 24 25 26
    27 28 29 30 31
    


```python
import calendar
import pprint

pprint.pprint(calendar.monthcalendar(2023, 3))
```

    [[0, 0, 1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10, 11, 12],
     [13, 14, 15, 16, 17, 18, 19],
     [20, 21, 22, 23, 24, 25, 26],
     [27, 28, 29, 30, 31, 0, 0]]
    


```python
# jupyter nbconvert --to markdown ***.ipynb
# ipynb->markdown
```
