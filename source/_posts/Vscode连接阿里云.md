---
title: Vscode连接阿里云服务器
categories:
  - 杂七杂八配置
tags:
  - Vscode连接阿里云服务器
toc: true# 是否启用内容索引
---

有个阿里云ECS服务器，之前一直用宝塔面板连接，方便时方便，但是有时候太占内容了。
本来服务器就小，一个宝塔占的差不多了。
后期改成Vscode。
其他能远程连接的软件很多，但是vscode是个神器，很推荐。

## 方法1：密钥对
用密钥对个人觉得有点，类似**hexo博客搭建里面连接github**.

1. 在阿里云控制台，找到密钥对，点进去创建密钥对
![](https://image.yayan.xyz/20221026144912.png)

2. 创建一个新的，名字随便起

![](https://image.yayan.xyz/20221026145018.png)

3. 绑定到实例中，然后重启
![](https://image.yayan.xyz/20221026145102.png)

**绑定完会自动下载一个.pem文件，尽量存到C:\user\username**里面的一个问价夹

如果直接放桌面或者公共文件夹，后期会报一个too open的错误

4. 打开vscode，下载remote-ssh插件，打开ssh的配置文件

![](https://image.yayan.xyz/20221026145352.png)
应该是**C:\Users\username\\.ssh\config**
在配置文件中添加
```bash
Host 起个名字
  HostName 服务器的ip(192.168.1.1)
  IdentityFile pem的路径\xxx.pem
  User 用户名(root)
```
或者点击”+“号，输入命令：
```bash
ssh -i "pem路径" root@服务器ip
```

5. 配置完成，打开就行了,后面会选操作系统，选个continue，忘记要不要输密码了

> 目前单台云服务器只支持绑定单个密钥对。若您选择已经绑定过其他密钥对的云服务器，新绑定的密钥对将会覆盖以前绑定的密钥对。绑定/解绑密钥对需要在控制台重启ECS实例才能生效

>太麻烦了，而且我自己用的时候很多次显示Permission denied (publickey).无解，
强烈推荐下面一种方式

## 方法2：用户名密码连接

先贴一个[阿里云官网文档](https://help.aliyun.com/document_detail/71529.html)，通过密码或密钥认证登录Linux实例-为Linux实例开启root用户远程登录

1. 先用VNC连接一下，修改配置文件
![](https://image.yayan.xyz/20221026150342.png)
输入用户名密码。
如果密码忘了，在菜单栏的实例中，修改密码
![](https://image.yayan.xyz/20221026150532.png)

2. 终端中，输入
```bash
vi /etc/ssh/sshd_config
# 如果不是root，就输入
sudo vi /etc/ssh/sshd_config
```

3. 往下翻，基本上在最后

```bash
# PermitRootLogin no修改为PermitRootLogin yes。
# PasswordAuthentication no修改为PasswordAuthentication yes。
# 修改方法：
# 1. 找到要修改的位置，点击"i",就进入编辑模式了
# 2. 修改改完之后按Esc键，输入:wq保存修改。
# 如果不是root，输入:wq!保存
```

4. 重启sshd服务
```bash
service sshd restart
```

5. 在vscode的远程连接中，修改配置文件或者直接输入

```bash
Host 起个名字
  HostName 服务器的ip(192.168.1.1)
  User 用户名(root)
# 或者输入 ssh root@服务器ip
```
输入实例密码就连接成功了！


👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍👍
