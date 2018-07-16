#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: support.py
# using: sys

import sys

def printFunc(par):
    print('Hello : ',par)
    return

print('命令行参数如下：')
for i in sys.argv:
    print(i)
print('\n\nPython路径为：',sys.path,'\n')

if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')