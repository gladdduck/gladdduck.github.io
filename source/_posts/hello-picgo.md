---
title: print(Hello picgo)
categories:
  - hexo博客配置
tags:
  - hexo博客配置picgo
toc: true# 是否启用内容索引
---
# 起因

在hexo配置完成开始写博客，但是markdown的图片在xxxx.githun.io中显示不出来
各方搜索，贴一个[解决方法](https://www.suyuanblog.xyz/2021/10/14/%E5%9B%BE%E7%89%87%E6%98%BE%E7%A4%BA/#:~:text=%E8%A7%A3%E5%86%B3%E6%96%B9%E6%A1%88,%E5%A4%B9%E9%87%8C%E6%96%B9%E4%BE%BF%E5%90%8E%E9%9D%A2%E5%BC%95%E7%94%A8%E3%80%82)。
但是个人觉得有点麻烦，而且考虑到以后写markdown也实在不想再搞个文件夹存图片。

于是，找到七牛云+picgo配置图云，把图片转为在线的

# 七牛云配置

1. 登陆注册略(50G的图片空间),[七牛云](https://portal.qiniu.com/home)
2. 创建新的存储空间，名字随便起
   ![](https://image.yayan.xyz/20221020131544.png)
3. 配置key
   ![](https://image.yayan.xyz/20221020131707.png)
   ![](https://image.yayan.xyz/20221020131754.png)
4. 记住分给自己的域名(这个能用一个月，一个月之后咋办我不知道)

# picgo配置

1. 下载[picgo](https://picgo-1251750343.cos.ap-chengdu.myqcloud.com/2.3.1-beta.6/PicGo-Setup-2.3.1-beta.6-x64.exe)
2. 配置七牛云
   ![](https://image.yayan.xyz/20221020132155.png)

- AccessKey和SecretKey：上面记住的key
- Bucket：第2步自己起的名字
- 访问地址：分配给自己的域名
- 存储区域：[七牛云的存储区域对应的代码](https://developer.qiniu.com/kodo/1671/region-endpoint-fq)（华东 z0，华北 z1，华南 z2，北美 na0，东南亚 as0 ）

3. 设为默认图床之后就可以上传了，具体的使用方法可以自己摸索

补充，设置为默认图床之后应该还要再输一遍，然后点确定

![](https://image.yayan.xyz/20221020132516.png)
复制图片之后点击，就可以直接Ctrl+V粘贴图片地址了
