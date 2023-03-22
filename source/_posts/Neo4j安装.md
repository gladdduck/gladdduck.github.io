---
title: Neo4j&JDK安装踩坑
categories:
  - 杂七杂八配置 
tags:
  - neo4j安装
toc: true# 是否启用内容索引
---
# 前言

最近要开始打工了
😟 😟 😟 😟
创建一个知识图谱(可视化)嵌入到一个系统里面,当作子系统.

期待的效果是[百度百科影视图谱](https://baike.baidu.com/lemmagraph/graphview?lemmaId=56059649&featureId=06a4e94ff6154c81ede88422&classify=teleplay&fromModule=lemma_graph-tree),任务太艰巨了.
😔 😔 😔 😔
如果你看到了这篇博客,有好的解决方案都可以帮帮我.
😘 😘 😘 😘

# 正文

## 踩坑

😭😭😭😭

### 问题:

```
想创建多个数据库用,刚开始默认有两个,一个neo4j,一个system.
希望创建别的数据库.
比如:
```

![](https://image.yayan.xyz/20221103175926.png)

网上搜索了很多办法,最坑的一个:

```
创建:create database name
删除:drop database name
```

看着挺好,试了很多遍报错

![](https://image.yayan.xyz/20221103180045.png)


看了[文档](https://neo4j.com/docs/cypher-manual/4.2/administration/databases/)才知道,**这是企业版专属命令,社区版用不了...**

![](https://image.yayan.xyz/20221103183512.png)
---

### 解决:

[neo4j官网](https://neo4j.com/docs/operations-manual/4.3/manage-databases/configuration/)

**新建数据库**
在 ``neo4j\conf\neo4j.conf``中,
找到 ``dbms.default_database=defaultdatabase``
修改后面的名字

> 如果数据库不存在,就会创建一个新的
> 如果存在,启动之后就会设为默认的数据库

但是有一个弊端:
![](https://image.yayan.xyz/20221103175926.png)
这种方式还是切换不了数据库

cypher命令 ``use databasename``也不能用

上面两种方法都会报错
![](https://image.yayan.xyz/20221103180846.png)

因为**社区版只能开启一个用户数据库...**
![](https://image.yayan.xyz/20221103183313.png)
如果想切换数据库只能修改配置文件,然后重启(neo4j restart)或者开一个新的进程(neo4j start).

---

**删除数据库**

把 ``neo4j\data\``文件夹下面的
![](https://image.yayan.xyz/20221103181021.png)
对应的数据库名字删除,即可.

## 配置前须知

neo4j现在已经到5.x了,
neo4j 3.x版本需要jdk8
neo4j 4.x版本需要jdk11

安装之前需要把jdk安装好,我用的neo4j4.3.19,
jdk11.2

## JDK安装

jdk有很多资料,建议找一个时间最近的,不要找好几年前的.

1. 下载jdk安装包
   [官网下载](https://www.oracle.com/java/technologies/downloads/)需要注册,可以用[其他镜像](https://repo.huaweicloud.com/java/jdk/)
2. 如果需要,更改路径,但是要记住
   ![](https://image.yayan.xyz/20221103174240.png)
   (没图了,网上找的图)
3. 一路next之后,如果jdk目录里没有jre

> 命令:
> bin\jlink.exe --module-path jmods --add-modules java desktop --output jre
> 就多了一个jre文件夹

4. 配置环境变量
   ![](https://image.yayan.xyz/20221103174641.png)

```
%JAVA_HOME%\bin
%JAVA_HOME%\jre\bin
```

![](https://image.yayan.xyz/20221103174753.png)

```
.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar
```

![](https://image.yayan.xyz/20221103174829.png)

[解释每个变量的作用](https://www.cnblogs.com/zll-wyf/p/15095664.html)

```bash
JAVA_HOME
    变量名：JAVA_HOME
    变量值：C:\develop\Java\jdk1.8.0_191
    用途：定义一个变量，供其他地方使用

Path
    变量名：Path
    变量值：%JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;
    用途：让系统在任何路径下都可以识别java、javac、javap等命令

CLASSPATH
    变量名：CLASSPATH
    变量值：.;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar
    用途：告诉jvm要使用或执行的class放在什么路径上，便于JVM加载class文件，.;表示当前路径，tools.jar和dt.jar为类库路径

CLASSPATH详解
    - tools.jar
    工具类库(编译和运行等)，它跟我们程序中用到的基础类库没有关系。我们注意到在Path中变量值bin目录下的各个exe工具的大小都很小，一般都在27KB左右，这是因为它们实际上仅仅相当于是一层代码的包装，这些工具的实现所要用到的类库都在tools.jar中，用压缩软件打开tools.jar，你会发现有很多文件是和bin目录下的exe工具相对性的。当然，如果tools.jar的功能只有这些的话，那么我们根本不用把它加入到CLASSPATH变量中，因为bin目录下的工具自己可以完成对这些类库的调用，因此tools.jar应该还有其他的功能。在里面还可以看到有Applet和RMI等相关的文件，因此tools.jar应该还是远程调用等必须的jar包。tools.jar的其他作用可以查看其他资料。

    - dt.jar
    运行环境类库，主要是Swing包，这一点通过用压缩软件打开dt.jar也可以看到。如果在开发时候没有用到Swing包，那么可以不用将dt.jar添加到CLASSPATH变量中。
    CLASSPATH中的类库是由Application ClassLoader或者我们自定义的类加载器来加载的，这里当然不能包括基础类库，如果包括基础类库的话，并用两个不同的自定义类加载器去加载该基础类，那它得到的该基础类就不是唯一的了，这样便不能保证Java类的安全性。

    - 基本类库和扩展类库rt.jar
    基本类库是所有的 import java.* 开头的类，在 %JAVA_HOME%\jre\lib 目录下（如其中的 rt.jar、resource.jar ），类加载机制提到，该目录下的类会由 Bootstrap ClassLoader 自动加载，并通过亲委派模型保证了基础类库只会被Bootstrap ClassLoader加载，这也就保证了基础类的唯一性。

    - 扩展类库是所有的 import javax.* 开头的类，在 %JAVA_HOME%\jre\lib\ext 目录下，该目录下的类是由Extension ClassLoader 自动加载，不需要我们指定。

    - rt.jar 默认就在根ClassLoader的加载路径里面，放在CLASSPATH也是多此一举。

```

5. 验证

```
cmd里输入:
java -version
javac -version
```

## neo4j安装

```bash
neo4j有三个版本
一个是社区版:和桌面版基本上没区别,桌面版就是一个应用程序,社区版需要用命令行启动
一个是企业版:收费,没用过,功能很多,上面有体会
一个是桌面版:有可以操作的页面,方便,但是会有点慢
```

1. [官网下载](https://neo4j.com/download-center/),找对应的安装zip(社区版)
2. 下载解压
3. 配置环境变量
   ![](https://image.yayan.xyz/20221103175408.png)
   ![](https://image.yayan.xyz/20221103175425.png)
4. cmd中输入:neo4j start 就可以启动了,浏览器输入访问

```
http://localhost:7474/browser/
```

5. 默认用户名密码都是**neo4j**
