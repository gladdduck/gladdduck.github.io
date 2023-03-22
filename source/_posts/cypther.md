---
title: Cypher学习笔记
categories:
  - 学习笔记
tags:
  - Cypher学习笔记
toc: true# 是否启用内容索引
---

```python
# CQL:C-ypher Q-uery L-nguage
```


```python
# 中文:http://neo4j.com.cn/public/cypher/default.html
# ★英文:https://neo4j.com/docs/cypher-manual/current/introduction/
# 中文:https://www.w3cschool.cn/neo4j/
```

# 表达式



```python
%%cypher
MATCH (n:Person)
RETURN
CASE 
  WHEN n.born>1980  THEN 1
  WHEN n.born<1980 THEN 2
  ELSE 3
END AS result
limit 5
```




    [{'result': 2}, {'result': 2}, {'result': 2}, {'result': 2}, {'result': 2}]



### list


```python
%%cypher
RETURN range(0, 10)[0..-5]
//[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]左闭右开
```




    [{'range(0, 10)': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}]




```python
%%cypher
RETURN [x IN range(0,10) WHERE x % 2 = 0 ] AS result
```


```python
%%cypher
RETURN [x IN range(0,10) | x^3 ] AS result
```


```python
%%cypher
MATCH (a:Person {name: 'Keanu Reeves'})
RETURN [(a)-->(b:Movie) WHERE b.title CONTAINS 'Matrix' | b.released] AS years
```




    [{'years': [1999, 2003, 2003]}]




```python
%%cypher
MATCH (a:Person {name: 'Keanu Reeves'})
WITH [(a)-->(b:Movie) | b.released] AS years
UNWIND years AS year
WITH year ORDER BY year
RETURN COLLECT(year) AS sorted_years
```




    [{'sorted_years': [1995, 1997, 1999, 2000, 2003, 2003, 2003]}]



### map


```python
%%cypher
MATCH (actor:Person)-[:ACTED_IN]->(movie:Movie)
WITH actor, count(movie) AS nbrOfMovies
RETURN actor{.name, nbrOfMovies}
limit 5
```




    [{'actor': {'nbrOfMovies': 1, 'name': 'Emil Eifrem'}},
     {'actor': {'nbrOfMovies': 7, 'name': 'Keanu Reeves'}},
     {'actor': {'nbrOfMovies': 3, 'name': 'Laurence Fishburne'}},
     {'actor': {'nbrOfMovies': 5, 'name': 'Hugo Weaving'}},
     {'actor': {'nbrOfMovies': 3, 'name': 'Carrie-Anne Moss'}}]



### null

# 基础语法

[官网](https://neo4j.com/docs/cypher-manual/current/clauses/)

|  命令   | 作用  |
|  ----  | ----  |
|  CREATE  | 创建节点\关系\属性 |
|  MATCH  | 检索节点\关系\属性 |
|  RETURN  | 返回查询结果 |
|  WHERE  | 提供过滤条件 |
|  DELETE  | 删除节点\关系 |
|  REMOVE  | 删除节点\关系的属性\标签 |
|  ORDER BY  | 排序检索数据 |
|  SET  | 添加或更新标签 |


```python
%load_ext icypher
%cypher http://neo4j:111222@localhost:7474/db/data
```

## CREATE
- 创建没有属性的节点
- 使用属性创建节点
- 在没有属性的节点之间创建关系
- 使用属性创建节点之间的关系
- 为节点或关系创建单个或多个标签


```python
%%cypher
CREATE (dept:Dept { deptno:10,dname:'Accounting',location:'苏州',isperson:true })
//一个节点多个属性一个标签
```




    []




```python
%%cypher
create (m:MOVIE:Cinema:Film:Picture{labels:true})
//一个节点多个标签
```




    []




```python
%%cypher
match (n:MOVIE:Cinema)
return n
//区分大小写
```




    [{'n': Node('Cinema', 'Film', 'MOVIE', 'Picture')},
     {'n': Node('Cinema', 'Film', 'MOVIE', 'Picture', labels=True)}]




```python
# 配合json使用
# {
#   'props' : [ {
#     'name' : 'Andy',
#     'position' : 'Developer'
#   }, {
#     'name' : 'Michael',
#     'position' : 'Developer'
#   } ]
# }
# UNWIND $props AS map
# CREATE (n)
# SET n = map
```

## MATCH
- 从数据库获取有关节点和属性的数据
- 从数据库获取有关节点，关系和属性的数据
- **需要和别的语句搭配使用**


```python
%%cypher
MATCH (p:Dept {location:'苏州'}) RETURN p.location
//这是注释 不能放上面
```




    [{'p.location': '苏州'}]




```python
%%cypher
MATCH (p:Dept)
WHERE p.location = '苏州'
RETURN p
//等价上面的
```




    [{'p': Node('Dept', deptno=10, dname='Accounting', isperson=True, location='苏州')}]




```python
%%cypher
MATCH (director:Movie)--(movie)
RETURN movie
limit 5
//--表示关系 不考虑方向(-->)和属性
```




    [{'movie': Node('Person', born=1978, name='Emil Eifrem')},
     {'movie': Node('Person', born=1952, name='Joel Silver')},
     {'movie': Node('Person', born=1965, name='Lana Wachowski')},
     {'movie': Node('Person', born=1967, name='Lilly Wachowski')},
     {'movie': Node('Person', born=1960, name='Hugo Weaving')}]




```python
%%cypher
MATCH (wallstreet {title: 'Joe Versus the Volcano'})<-[:ACTED_IN|DIRECTED]-(person)
RETURN person.name
limit 5
//查询多个关系
//如果关系名字里面有空格 用反引号``
//[:TYPE*minHops..maxHops] 代表关系的长度
//shortestPath((martin)-[*..15]-(oliver)) 最短路径,最大长度为15
```




    [{'person.name': 'Meg Ryan'},
     {'person.name': 'Tom Hanks'},
     {'person.name': 'John Patrick Stanley'},
     {'person.name': 'Nathan Lane'},
     {'person.name': 'Meg Ryan'}]




```python
%%cypher
MATCH (charlie {name: 'Tom Hanks'})-[:ACTED_IN]->(movie)<-[:DIRECTED]-(director)
RETURN movie.title, director.name
limit 5
```




    [{'movie.title': "You've Got Mail", 'director.name': 'Nora Ephron'},
     {'movie.title': 'Sleepless in Seattle', 'director.name': 'Nora Ephron'},
     {'movie.title': 'Joe Versus the Volcano',
      'director.name': 'John Patrick Stanley'},
     {'movie.title': 'That Thing You Do', 'director.name': 'Tom Hanks'},
     {'movie.title': 'Cloud Atlas', 'director.name': 'Tom Tykwer'}]




```python
# OPTIONAL MATCH 
# using nulls for missing parts 
```

## RETURN
- 检索节点的某些属性
- 检索节点的所有属性
- 检索节点和关联关系的某些属性
- 检索节点和关联关系的所有属性
- **需要和别的语句搭配使用**


```python
# return * return 所有出现过的变量
```


```python
%%cypher
MATCH (`This isn\'t a common variable`)
WHERE `This isn\'t a common variable`.name = 'Kiefer Sutherland'
RETURN `This isn\'t a common variable`.born  as othername
//DISTINCT 返回不重复的值
```




    [{'othername': 1966}, {'othername': 1966}]



##  CREATE+MATCH+RETURN


```python
%%cypher
CREATE (e:Customer{id:'1001',name:'Abc',dob:'01/10/1982'})
```




    []




```python
%%cypher
CREATE (cc:CreditCard{id:'5001',number:'1234567890',cvv:'888',expiredate:'20/17'})
```




    []




```python
# 1. 使用现有节点创建没有属性的关系
```


```python

%%cypher
match (e:Customer),(cc:CreditCard)
create (e)-[r:DO_SHOPPING_WITH]->(cc)
RETURN r
//不加return 也可以
//只能创建有向关系,查询的时候可以查双向关系
```




    [{'r': DO_SHOPPING_WITH(Node('Customer', dob='01/10/1982', id='1001', name='Abc'), Node('CreditCard', cvv='888', expiredate='20/17', id='5001', number='1234567890'))}]




```python
%%cypher
MATCH (e:Customer)-[r ]->(cc) 
RETURN r
```




    [{'r': second_relation(Node('Customer', dob='01/10/1982', id='1001', name='Abc'), Node('CreditCard', cvv='888', expiredate='20/17', id='5001', number='1234567890'))},
     {'r': DO_SHOPPING_WITH(Node('Customer', dob='01/10/1982', id='1001', name='Abc'), Node('CreditCard', cvv='888', expiredate='20/17', id='5001', number='1234567890'))}]




```python
%%cypher
MATCH whole=(e)-[r ]->(cc:Movie) 
RETURN whole
limit 5
```




    [{'whole': Path(Node('Person', born=1978, name='Emil Eifrem'), ACTED_IN(Node('Person', born=1978, name='Emil Eifrem'), Node('Movie', released=1999, tagline='Welcome to the Real World', title='The Matrix')))},
     {'whole': Path(Node('Person', born=1952, name='Joel Silver'), PRODUCED(Node('Person', born=1952, name='Joel Silver'), Node('Movie', released=1999, tagline='Welcome to the Real World', title='The Matrix')))},
     {'whole': Path(Node('Person', born=1965, name='Lana Wachowski'), DIRECTED(Node('Person', born=1965, name='Lana Wachowski'), Node('Movie', released=1999, tagline='Welcome to the Real World', title='The Matrix')))},
     {'whole': Path(Node('Person', born=1967, name='Lilly Wachowski'), DIRECTED(Node('Person', born=1967, name='Lilly Wachowski'), Node('Movie', released=1999, tagline='Welcome to the Real World', title='The Matrix')))},
     {'whole': Path(Node('Person', born=1960, name='Hugo Weaving'), ACTED_IN(Node('Person', born=1960, name='Hugo Weaving'), Node('Movie', released=1999, tagline='Welcome to the Real World', title='The Matrix')))}]




```python
# 2. 使用现有节点创建有属性的关系
```


```python
%%cypher
match (e:Customer),(cc:CreditCard)
create (e)-[r:DO_SHOPPING_WITH{shopdata:'12/12/2014',price:5500}]->(cc)
RETURN r
```




    [{'r': DO_SHOPPING_WITH(Node('Customer', dob='01/10/1982', id='1001', name='Abc'), Node('CreditCard', cvv='888', expiredate='20/17', id='5001', number='1234567890'), price=5500, shopdata='12/12/2014')}]




```python
# 3.使用新节点创建有/无属性的关系
# 和1.2.的区别是 1.2.需要先match
```


```python
%%cypher
create (fb1:FaceBookProfile)-[like:LIKES]->(fb2:FaceBookProfile)
//创建了两个新节点喝一个新关系
```




    []




```python
%%cypher
create (video1:YoutubeVideo{title:'Action Movie1',update_by:'Abc',uploaded_data:'10/10/2010'})
-[movie:ACTION_MOVIES{rating:1}]->
(video2:YoutubeVideo{title:'Action Movie2',update_by:'Xyz',uploaded_data:'12/12/2012'})
```




    []




```python
%%cypher
match (cust)-[r:DO_SHOPPING_WITH]->(cc)
return cust,r,cc
```




    [{'cust': Node('Customer', dob='01/10/1982', id='1001', name='Abc'),
      'r': DO_SHOPPING_WITH(Node('Customer', dob='01/10/1982', id='1001', name='Abc'), Node('CreditCard', cvv='888', expiredate='20/17', id='5001', number='1234567890')),
      'cc': Node('CreditCard', cvv='888', expiredate='20/17', id='5001', number='1234567890')},
     {'cust': Node('Customer', dob='01/10/1982', id='1001', name='Abc'),
      'r': DO_SHOPPING_WITH(Node('Customer', dob='01/10/1982', id='1001', name='Abc'), Node('CreditCard', cvv='888', expiredate='20/17', id='5001', number='1234567890')),
      'cc': Node('CreditCard', cvv='888', expiredate='20/17', id='5001', number='1234567890')},
     {'cust': Node('Customer', dob='01/10/1982', id='1001', name='Abc'),
      'r': DO_SHOPPING_WITH(Node('Customer', dob='01/10/1982', id='1001', name='Abc'), Node('CreditCard', cvv='888', expiredate='20/17', id='5001', number='1234567890'), price=5500, shopdata='12/12/2014'),
      'cc': Node('CreditCard', cvv='888', expiredate='20/17', id='5001', number='1234567890')}]



## WHERE

```
WHERE <condition> <boolean-operator> <condition> 
<condition>:            <property-name> <comparison-operator> <value>  
<comparison-operator>:  =/<>/</>/<=/>=/=~(正则)
<boolean-operator>:     AND/OR/NOT/XOR
```


```python
%%cypher
MATCH (emp:YoutubeVideo) 
WHERE emp.aaaaa = 'Xyz'
RETURN id(emp)
//没有的属性认为False
```




    []




```python
%%cypher
MATCH (emp:YoutubeVideo) 
WHERE emp.update_by = 'Abc' OR emp.update_by = 'Xyz'
RETURN id(emp)
//查询
```




    [{'id(emp)': 231}, {'id(emp)': 232}]




```python
%%cypher
match (n:Dept),(c:CreditCard)
where n.location='苏州' and c.cvv='888'
create (n)-[r:no_relations{prop:'随机创建的'}]->(c)
return r

//创建 数字也要用'',直接888查不到,创建的时候用''了
```




    [{'r': no_relations(Node('Dept', deptno=10, dname='Accounting', isperson=True, location='苏州'), Node('CreditCard', cvv='888', expiredate='20/17', id='5001', number='1234567890'), prop='随机创建的')}]




```python
%%cypher
MATCH (n:Person)
WHERE n['born'] > 1980
RETURN n.name, n.born
limit 5
//n.name CONTAINS 'ete'
//n.name ENDS WITH 'ter'
//WHERE n.name STARTS WITH 'Pet'
```




    [{'n.name': 'Jonathan Lipnicki', 'n.born': 1996},
     {'n.name': 'Natalie Portman', 'n.born': 1981},
     {'n.name': 'Emile Hirsch', 'n.born': 1985},
     {'n.name': 'Rain', 'n.born': 1982},
     {'n.name': 'Jonathan Lipnicki', 'n.born': 1996}]




```python
%%cypher
MATCH (n:Person)-[r]->()
WHERE n.name='Angela Scope' AND type(r) =~ 'F.*'
RETURN type(r), r
limit 5
//A开头的关系
```




    [{'type(r)': 'FOLLOWS',
      'r': FOLLOWS(Node('Person', name='Angela Scope'), Node('Person', name='Jessica Thompson'))},
     {'type(r)': 'FOLLOWS',
      'r': FOLLOWS(Node('Person', name='Angela Scope'), Node('Person', name='Jessica Thompson'))}]




```python
%%cypher
MATCH (person:Person),(f:Person)
WHERE EXISTS {
  MATCH (person)-[:FOLLOWS]->(f)
  WHERE person.name = 'Paul Blythe' 
}
RETURN f.name AS name
//嵌套查询 内层可用外层变量
```




    [{'name': 'Angela Scope'}, {'name': 'Angela Scope'}]



## DELETE
- 删除节点
- 删除关系


```python
%%cypher
MATCH (e:Film) delete  e
```




    []




```python
%%cypher
match (n:Customer)-[r]-(c:CreditCard) delete n,c,r
//删除节点时必要保证节点没有其他的关系相连
```




    []




```python
%%cypher
MATCH (n:Movie)
DETACH DELETE n
//删除节点和相连的关系
```




    []




```python
%%cypher
match (n)-[r]-(c:Dept) return r
```




    []



## REMOVW
- 删除节点或关系的标签
- 删除节点或关系的属性
- keys(n) 查看n的所有属性
- labels(n) 查看n的所有标签


```python
%%cypher
create (book:Book {id:122,title:'Neo4j TUtorial',pages:333,price:250})
return book

```




    [{'book': Node('Book', id=122, pages=333, price=250, title='Neo4j TUtorial')}]




```python
%%cypher
match (book:Book{id:122})
remove book.noattr
return book
//没有这个属性也可以
```




    [{'book': Node('Book', id=122, pages=333, title='Neo4j TUtorial')}]




```python
%%cypher
match (n:label1)
remove n:label1
return n
```




    [{'n': Node('label2', 'label3', 'label4', labels=True)}]



## SET
- 向现有节点或关系添加新属性
- 添加或更新属性值


```python
%%cypher
match (n:Dept)
set n.dname='帅哥' ,n.type='666'
return n
//有就修改 没有添加
```




    [{'n': Node('Dept', deptno=10, dname='帅哥', location='Hyderabad', type='666')},
     {'n': Node('Dept', deptno=10, dname='帅哥', isperson=True, location='苏州', type='666')}]




```python
%%cypher
MATCH (book:Book{}) 
SET book+={title:'neo4j tutorial'}
return book
//book={offline:True}会把原有是属性值全部删掉 book+={offline:True} 不会删除原有属性 新增一个属性
```




    [{'book': Node('Book', offline=True, title='neo4j tutorial')}]




```python
%%cypher
MATCH (book:Book{})  SET book:Knowledge RETURN book
//新增一个标签
```




    [{'book': Node('Book', 'Knowledge', offline=True, title='neo4j tutorial')}]




```python
%%cypher
MATCH (book:Book{}) 
SET book.addtitle=book.title
remove book.title
return book
```




    [{'book': Node('Book', 'Knowledge', addtitle='neo4j tutorial', offline=True)},
     {'book': Node('Book')},
     {'book': Node('Book', addtitle='neo4j start', offline=True)},
     {'book': Node('Book', addtitle='neo4j end', offline=False)}]




```python
%%cypher
MATCH (n {dname: '帅哥'})
SET (CASE WHEN n.type = 666 THEN n END).worksIn = 'Malmo'
RETURN n
//只有n.type = 666 才设置
```




    [{'n': Node('Dept', deptno=10, dname='帅哥', location='Hyderabad', type='666')},
     {'n': Node('Dept', deptno=10, dname='帅哥', isperson=True, location='苏州', type='666')}]




```python
# {
#   'props' : {
#     'name' : 'Andy',
#     'position' : 'Developer'
#   }
# }
# MATCH (n {name: 'Andy'})
# SET n = $props
# RETURN n.name, n.position, n.age, n.hungry
```

## ORDER BY
- 默认是升序排列 DESC改为降序


```python
%%cypher
match (movie:Movie)
return movie.released,movie.title
order by movie.released DESC , movie.title
limit 15
//多个属性排列
```




    [{'movie.released': None, 'movie.title': 'The Matrix'},
     {'movie.released': None, 'movie.title': 'The Matrix'},
     {'movie.released': None, 'movie.title': 'The Matrix Reloaded'},
     {'movie.released': None, 'movie.title': 'The Matrix Reloaded'},
     {'movie.released': None, 'movie.title': 'The Matrix Revolutions'},
     {'movie.released': None, 'movie.title': 'The Matrix Revolutions'}]



## UNION [ALL]
- 将两个不同的结果合并


```python
%%cypher
create (n:CreditCard{id:1,name:'ABX XYZ',number:'1234567890',cvv:1230,valid_from:'6/14',valid_to:'6/24'})
,(n1:CreditCard{id:2,name:'ABX1 XYZ1',number:'1234567891',cvv:1231,valid_from:'6/141',valid_to:'6/241'})
,(n2:CreditCard{id:3,name:'ABX2 XYZ2',number:'1234567892',cvv:1232,valid_from:'6/142',valid_to:'6/242'})
,(n3:CreditCard{id:4,name:'ABX3 XYZ3',number:'1234567893',cvv:1233,valid_from:'6/143',valid_to:'6/243'})
,(n4:CreditCard{id:5,name:'ABX XYZ',number:'1234567890',cvv:123,valid_from:'6/14',valid_to:'6/24'})
```


```python
%%cypher
create (n:DebitCard{id:1,name:'ABX XYZ',number:'1234567890',cvv:1230,valid_from:'6/14',valid_to:'6/24'})
,(n1:CreditCard{id:11,name:'ABX1 XYZ1',number:'1234567891',cvv:1231,valid_from:'6/141',valid_to:'6/241'})
,(n2:CreditCard{id:12,name:'ABX2 XYZ2',number:'1234567892',cvv:1232,valid_from:'6/142',valid_to:'6/242'})
,(n3:CreditCard{id:13,name:'ABX3 XYZ3',number:'1234567893',cvv:1233,valid_from:'6/143',valid_to:'6/243'})
,(n4:CreditCard{id:14,name:'ABX XYZ',number:'1234567890',cvv:123,valid_from:'6/14',valid_to:'6/24'})
```


```python
%%cypher
match (cc:CreditCard) return cc.id as id ,cc.number as number
UNION 
match (dc:DebitCard) return dc.id  as id ,dc.number as number
//自动去掉重复从行 不用as
//这里既有信用卡式和借记卡具有相同的属性名：身份证和号码，但他们有不同的节点名称前缀。
//这就是为什么UNION命令显示此错误消息。为了避免这种错误，Neo4j的CQL提供“AS”子句。
```




    [{'id': '5001', 'number': '1234567890'},
     {'id': 1, 'number': '1234567890'},
     {'id': 2, 'number': '1234567891'},
     {'id': 3, 'number': '1234567892'},
     {'id': 4, 'number': '1234567893'},
     {'id': 5, 'number': '1234567890'},
     {'id': 11, 'number': '1234567891'},
     {'id': 12, 'number': '1234567892'},
     {'id': 13, 'number': '1234567893'},
     {'id': 14, 'number': '1234567890'}]




```python
%%cypher
match (cc:CreditCard) return cc.id as id ,cc.number as number
UNION  ALL
match (dc:DebitCard) return dc.id  as id ,dc.number as number
//显示所有的行
```




    [{'id': '5001', 'number': '1234567890'},
     {'id': 1, 'number': '1234567890'},
     {'id': 2, 'number': '1234567891'},
     {'id': 3, 'number': '1234567892'},
     {'id': 4, 'number': '1234567893'},
     {'id': 5, 'number': '1234567890'},
     {'id': 11, 'number': '1234567891'},
     {'id': 12, 'number': '1234567892'},
     {'id': 13, 'number': '1234567893'},
     {'id': 14, 'number': '1234567890'},
     {'id': 1, 'number': '1234567890'}]



## LIMIT & SKIP
- limit n 只取结果的前n行
- skip n 跳过结果的前n行
- 可以放在一起用
-  limit/skip 1 + toInteger(3 * rand())

## MERGE
- MERGE命令在图中搜索给定模式
- 如果存在，则返回结果
- 如果它不存在于图中，则它创建新的节点/关系并返回结果。


```python
%%cypher
match (gp:GoogleProfile{ Id: 201402,Name:'Nokia'})
return  id(gp)
```




    []




```python
%%cypher
MERGE (gp:GoogleProfile{ Id: 201402,Name:'Nokia'})
return id(gp)
```




    [{'id(gp)': 248}]




```python
%%cypher
merge (gp:GoogleProfile{Id:201402,Name:'Nokia'})
return id(gp)
```




    [{'id(gp)': 248}]




```python
%%cypher
MERGE (keanu:Person {name: 'mergecreated'})
ON CREATE
  SET keanu.created = timestamp()
RETURN keanu.name, keanu.created
//如果没有就会创建 并添加一个timestamp
```




    [{'keanu.name': 'mergecreated', 'keanu.created': 1667637911668}]




```python
%%cypher
MERGE (person:Person{name: 'mergecreatedfound'})
ON MATCH
  SET person.found = true
RETURN person.name, person.found
limit 5
//如果找到了就添加  没找到就不添加found
```




    [{'person.name': 'mergecreatedfound', 'person.found': True}]




```python
%%cypher
MERGE (keanu:Person {name: 'Keanu Reeves'})
ON CREATE
  SET keanu.created = timestamp()
ON MATCH
  SET keanu.lastSeen = timestamp()
RETURN keanu.name, keanu.created, keanu.lastSeen
//有就是lastSeen,没有就是created
```




    [{'keanu.name': 'Keanu Reeves',
      'keanu.created': None,
      'keanu.lastSeen': 1667638041825}]




```python
%%cypher
MATCH (person:Person)
MERGE (city:City {name: person.bornIn})
MERGE (person)-[r:BORN_IN]->(city)
RETURN person.name, person.bornIn, city
```


```python
# CREATE CONSTRAINT ON (n:Person) ASSERT n.name IS UNIQUE;
# CREATE CONSTRAINT ON (n:Person) ASSERT n.role IS UNIQUE;
# For example, given two unique constraints on :Person(id) and :Person(ssn), 
# a query such as MERGE (n:Person {id: 12, ssn: 437}) will fail, 
# if there are two different nodes (one with id 12 and one with ssn 437) 
# or if there is only one node with only one of the properties. 
# In other words, there must be exactly one node that matches the pattern, or no matching nodes.
```

## NULL值


```python
%%cypher
create (n:Book)
```




    []




```python
%%cypher
MATCH (e:Book) 
RETURN e.offline,e.title,e.sal
// None 就是NULL
```




    [{'e.offline': True, 'e.title': 'neo4j tutorial', 'e.sal': None},
     {'e.offline': None, 'e.title': None, 'e.sal': None}]




```python
%%cypher
match (book:Book)
where book.offline is not null
return book
//where book.offline is null
```




    [{'book': Node('Book', 'Knowledge', offline=True, title='neo4j tutorial')}]



## IN
- 同 python IN


```python
%%cypher
MATCH (e:Book) 
WHERE e.offline IN [true]
RETURN e
```




    [{'e': Node('Book', 'Knowledge', offline=True, title='neo4j tutorial')},
     {'e': Node('Book', offline=True, title='neo4j start')}]



# CQL函数
[官网](https://neo4j.com/docs/cypher-manual/current/clauses/listing-functions/)


```python
%%cypher
return datetime()
```




    [{'datetime()': '2022-11-04T07:36:17.068Z'}]




```python
%%cypher
SHOW FUNCTIONS yield name,category,description
limit 5
```


```python
%%cypher
MATCH (a)-[movie:ACTED_IN]->(b) 
RETURN STARTNODE(movie),ENDNODE(movie)
limit 5
```




    [{'STARTNODE(movie)': Node('Person', born=1964, name='Keanu Reeves'),
      'ENDNODE(movie)': Node('Movie', released=2003, title="Something's Gotta Give")},
     {'STARTNODE(movie)': Node('Person', born=1964, name='Keanu Reeves'),
      'ENDNODE(movie)': Node('Movie', released=2000, tagline='Pain heals, Chicks dig scars... Glory lasts forever', title='The Replacements')},
     {'STARTNODE(movie)': Node('Person', born=1964, name='Keanu Reeves'),
      'ENDNODE(movie)': Node('Movie', released=1995, tagline='The hottest data on earth. In the coolest head in town', title='Johnny Mnemonic')},
     {'STARTNODE(movie)': Node('Person', born=1964, name='Keanu Reeves'),
      'ENDNODE(movie)': Node('Movie', released=1997, tagline='Evil has its winning ways', title="The Devil's Advocate")},
     {'STARTNODE(movie)': Node('Person', born=1964, name='Keanu Reeves'),
      'ENDNODE(movie)': Node('Movie', released=2003, tagline='Everything that has a beginning has an end', title='The Matrix Revolutions')}]




```python
%%cypher
MATCH (a)-[movie:ACTED_IN]->(b) 
RETURN ID(movie),TYPE(movie)
limit 5
//type 只能看relation
```




    [{'ID(movie)': 221, 'TYPE(movie)': 'ACTED_IN'},
     {'ID(movie)': 114, 'TYPE(movie)': 'ACTED_IN'},
     {'ID(movie)': 132, 'TYPE(movie)': 'ACTED_IN'},
     {'ID(movie)': 22, 'TYPE(movie)': 'ACTED_IN'},
     {'ID(movie)': 15, 'TYPE(movie)': 'ACTED_IN'}]



### 创建索引


```python
%%cypher
CREATE INDEX ON :Movie (title)
```




    []




```python
%%cypher
DROP INDEX ON :Movie (title)
```




    []



### 创建约束


```python
%%cypher
MATCH (cc:CreditCard) 
RETURN cc.id,cc.number,cc.name,cc.expiredate,cc.cvv
limit 5
```


```python
%%cypher
CREATE CONSTRAINT ON (cc:CreditCard)
ASSERT cc.id IS UNIQUE
//如果已经存在重复的就不能创建,把重复的删除
```




    []




```python
%%cypher
create (cc:CreditCard{id:666})
//Node(246) already exists with label `CreditCard` and property `id` = 14
```




    []




```python
%%cypher
DROP CONSTRAINT ON (cc:CreditCard)
ASSERT cc.id IS UNIQUE
```




    []




```python
%%cypher
create (cc:CreditCard{id:666})
```




    []



# 补充

## WITH
- allows query parts to be chained together


```python
%%cypher
MATCH (david {name: 'Jessica Thompson'})--(otherPerson)--()
WITH otherPerson, count(*) AS foaf
WHERE foaf > 0
RETURN otherPerson.name
```




    [{'otherPerson.name': 'Angela Scope'}, {'otherPerson.name': 'Angela Scope'}]



## UNWIND
- expands a list into a sequence of rows.


```python
%%cypher
UNWIND [1, 2, 3, null] AS x
RETURN x, 'val' AS y
```




    [{'x': 1, 'y': 'val'},
     {'x': 2, 'y': 'val'},
     {'x': 3, 'y': 'val'},
     {'x': None, 'y': 'val'}]




```python
%%cypher
WITH [1, 1, 2, 2] AS coll
UNWIND coll AS x
WITH DISTINCT x
RETURN collect(x) AS setOfVals
//列表去重
```




    [{'setOfVals': [1, 2]}]




```python
%%cypher
WITH
  [1, 2] AS a,
  [3, 4] AS b
UNWIND (a + b) AS x
RETURN x
```




    [{'x': 1}, {'x': 2}, {'x': 3}, {'x': 4}]




```python
%%cypher
WITH [[1, 2], [3, 4], 5] AS nested
UNWIND nested AS x
UNWIND x AS y
RETURN y
//两重循环
```




    [{'y': 1}, {'y': 2}, {'y': 3}, {'y': 4}, {'y': 5}]




```python
%%cypher
WITH [] AS list
UNWIND
  CASE
    WHEN list = [] THEN [null]
    ELSE list
  END AS emptylist
RETURN emptylist
//避免列表为空
```




    [{'emptylist': None}]



## FOREACH


```python
%%cypher
MATCH p=(start)-[*]->(finish)
WHERE start.name = 'Tom Hanks' AND finish.title starts with 'C'
FOREACH (n IN nodes(p) | SET n.marked = true)
```


```python
%%cypher
MATCH (a {name: 'Tom Hanks' })
FOREACH (name IN ['Mike', 'Carl', 'Bruce'] |
CREATE (a)-[:FRIEND]->(:Person {name: name}))
```




    []



## CALL
- CALL {}
- CALL procedure



```python
%%cypher
UNWIND [0, 1, 2] AS x
CALL {
  WITH x
  RETURN x * 10 AS y
}
RETURN x, y
```




    [{'x': 0, 'y': 0}, {'x': 1, 'y': 10}, {'x': 2, 'y': 20}]



LOAD　CSV
- LOAD CSV FROM 'file:///artists.csv' AS line -正常数据
- USING PERIODIC COMMIT 1000 LOAD CSV FROM 'file:///artists.csv' AS line -大数据,1000提交一次事物


```python
# SHOW PROCEDURES YIELD *.
# SHOW FUNCTIONS YIELD *.
```
