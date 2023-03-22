---
title: Linux的一些常用命令记录
categories:
  - 快捷命令
tags:
  - Linux快捷命令
toc: true# 是否启用内容索引
---
```bash
# 查看cpu型号
cat /proc/cpuinfo | grep 'model name'

# 查看系统
uname -a

# 查看显卡
lshw -C display

# 如果显卡是Nvidia
nvidia-smi

# 后台运行程序
nohup ***** & 

# 查看所有进程
ps -aux
```
