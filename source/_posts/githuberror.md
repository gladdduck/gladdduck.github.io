---
title: git Time out error解决
categories:
  - 杂七杂八配置
tags:
  - git Time out
  - github Time out
toc: true# 是否启用内容索引
---
错误信息:

```bash
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

解决:

git中输入

```
git config --global --unset http.proxy
 
git config --global --unset https.proxy
```

cmd 中输入

```bash
ipconfig /flushdns
```

刷新 `dns`缓存

然后再执行相应命令.

![](https://image.yayan.xyz/20230221185957.png)

> 成功
