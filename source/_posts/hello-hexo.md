---
title: print(Hello hexo) & github connected error
categories:
  - hexo博客配置
tags:
  - hexo博客配置pure
toc: true# 是否启用内容索引
---
中间过程可能会出现链接不上github的情况，这个因人而异。
不是操作问题，是墙的问题。
自己尝试解决办法。

# 配置简单博客

## 安装前配置

- git安装(下一步者)，测试：git -v
- nodejs安装(下一步者)，测试：node -v
- npm安装(装完node就有)，测试：npm -v
- hexo安装(npm install hexo -g)，测试：hexo -v
- 其他需要安装的依赖如下(主题部分会用到)(npm install depandence)，测试：npm init

```bash
+-- hexo-deployer-git@3.0.0
+-- hexo-generator-archive@1.0.0
+-- hexo-generator-baidu-sitemap@0.1.9
+-- hexo-generator-category@1.0.0
+-- hexo-generator-feed@3.0.0
+-- hexo-generator-index@2.0.0
+-- hexo-generator-json-content@4.2.3
+-- hexo-generator-sitemap@3.0.1
+-- hexo-generator-tag@1.0.0
+-- hexo-renderer-ejs@1.0.0
+-- hexo-renderer-markdown-it-plus@1.0.6
+-- hexo-renderer-stylus@2.1.0
+-- hexo-server@2.0.0
+-- hexo-theme-landscape@0.0.3
+-- hexo-wordcount@6.0.1
+-- hexo@5.4.2
```

## github上的操作

1. 新建一个仓库(repository)
   ![](https://image.yayan.xyz/1666186035942.png)
   **仓库名字一定是自己的用户名**
   **xxxxx.github.io**
2. git命令板链接仓库生成公钥

```python
#如果第一次下git应该要设置一下，我没设置后面报错了
git config --global user.name "username"
git config --global user.email "email"
# 生成公钥
ssh-keygen -t rsa  -C "email"
# 会在C:\Users\你的用户名\.ssh下生成id_rsa和id_rsa.pub
# 复制id_rsa.pub内容
```

![](https://image.yayan.xyz/1666186511107.png)
在setting中
![](https://image.yayan.xyz/1666186551655.png)
![](https://image.yayan.xyz/1666186590011.png)
![](https://image.yayan.xyz/1666186600564.png)
title可以随便填，key就是id_rsa.pub中的内容

然后在git命令版中测试：

```
ssh -T git@gitbuh.com
```

中间可能会输个yes
看见successfully就成功了

## 本地hexo的操作

1. 本地建一个空文件夹---暂且叫他dir方便后面说，这个就是博客全部内容
2. 执行完下面命令，文件夹内会多出东西，

```bash
# 如果执行失败，去github找到hexo-starter的库，下载解压，记得改名字
hexo init
```

3.如果不需要额外的hexo主题，执行下面命令就可以了完成了

```bash
# hexo 把本地的东西，生成静态文件(html,css这些)
hexo g
# hexo s在本地运行，可以进自己的浏览器看看
hexo s 
# hexo d 部署文件到github
hexo d

# hexo d -g可以直接生成并部署
# 访问xxxxx.github.io 就能看见自己的博客了
```

## 配置自己的信息

修改dir文件夹内的_config.yml配置文件
把链接什么的改成自己的链接就OK了

### 网站的配置

即dir文件夹下面的_config.yml

```python
# 1. 配置主题的文字，不然主题都是英文，这个必须在dir中配置，在主题中配置没有用
language: zh-CN

# 2. 如果用主题，主题的配置，不是hexo-theme-pure，就是pure
theme: pure
```

# hexo 配置自己喜欢的主题

**如果不是自己特别喜欢的主题，建议找一个大众的用的人多的主题，
因为用的人多，出现的问题解决办法就多**

以pure为例，更多的主题访问:
[hexo官网](https://hexo.io/themes/)

在配置主题过程中，建议参考pure官方文档:[hhexo-theme-pure](https://github.com/cofess/hexo-theme-pure)

1. 先把主题下载下来，除了git命令，其他的都建议在windows的cmd中使用

```bash
# 如果失败了，同样可以去github，hexo-theme-pure 下载解压，注意改文件夹名字
git clone https://github.com/cofess/hexo-theme-pure.git themes/pure
# 然后把官方文档建议的一大堆依赖下下来
# 第一部分下过的可以省略
npm install hexo-wordcount --save
npm install hexo-generator-json-content --save
npm install hexo-generator-feed --save
npm install hexo-generator-sitemap --save
npm install hexo-generator-baidu-sitemap --save
```

2. 修改dir文件夹内的_config.yml中的theme

如果没有自己添加

```
theme: pure
```

## 文章增删改查

增删改文件，直接在_post里修改md文件，上传即可。

## 踩坑

下面说几个自己踩过的坑，网站配置还好，
主题的配置一堆，而且pure用的人不多，问题全靠自己解决
以下的修改都在theme/pure/_cofig.yml文件中

### 网站的配置

1. 网站的名字和logo

```
site:
  logo:
    enabled: true
    width: 40
    height: 40
    url: ../images/logo.png
  title: Gladdduck # 页面title
  favicon: /favicon.png
  board: <p>分享所思所见所想,欢迎留言交流!6666</p> # 站点公告
  copyright: false # 底部版权信息
# 修改logo一定不要修改logo.url里面的图片路径
# 要修改favicon的路径，修改logo.url的路径没用，反而文章的详情页面不会出现logo了
```

2. 关于home，archives等不是中文的问题

```
menu:
  Home: .
  Archives: archives  # 归档
  Categories: categories  # 分类
  Tags: tags  # 标签
  Links: links  # 友链
  About: about  # 关于
# 把这个地方的Home等改了不起作用，应该修改dir文件夹下面的配置文件，增加language: zh-CN
# ：后面的是访问url路径，需要和source文件夹下面的几个文件夹名字对应
```

3. 菜单栏无法访问 Connot get

```
需要把theme/pure/source文件夹下面的几个文件夹
移动到dir文件夹下面的source中

# 现在hexo s 打开浏览器应该就可以看见自己的博客了，点击对应的菜单也会跳转

```

4. 其他配置根据配置文件内的注释修改即可

-- 后面会记录

- GitHub+gitalk配置评论
- 七牛云+PicGO配置图床，方便markdown书写

# 连接Github显示code128(Time out error)

**错误信息**

```
fatal: unable to access 'https://github.com/gladdduck/gladdduck.github.io.git/':
Failed to connect to github.com port 443 after 21048 ms: Timed out
FATAL {
  err: Error: Spawn failed
  at ChildProcess.<anonymous> (D:\BaiduSyncdisk\Blog\node_modules\hexo-util\lib\spawn.js:51:21)
      at ChildProcess.emit (node:events:513:28)
      at ChildProcess.cp.emit (D:\BaiduSyncdisk\Blog\node_modules\cross-spawn\lib\enoent.js:34:29)
      at Process.ChildProcess._handle.onexit (node:internal/child_process:293:12) {
    code: 128
  }
} Something's wrong. Maybe you can find the solution here: %s https://hexo.io/docs/troubleshooting.html
```

**解决办法**

1. 设置host文件--没用
2. 关闭VPN-- 没用
3. 连手机热点--偶尔有用
4. 取消代理--偶尔有用

```
取消全局代理：
git config --global --unset http.proxy
 
git config --global --unset https.proxy
```

5. 配置host文件

在C:\Windows\System32\drivers\etc中的host文件下新增(没有访问权限可以copy一份在桌面修改完之后覆盖)

```
140.82.113.4 github.com 
199.232.69.194 github.global.ssl.fastly.net
185.199.108.153 assets-cdn.github.com
185.199.109.153 assets-cdn.github.com
185.199.110.153 assets-cdn.github.com
185.199.111.153 assets-cdn.github.com

```

cmd中**ipconfig /flushdns刷新dns缓存**

!!!!!!!

😳 😳 😳 😳
单独刷新dns也能用!
cmd中```ipconfig /flushdns```
然后```hexo d -g``` 就完全Ok了
😍 😍 😍 😍 