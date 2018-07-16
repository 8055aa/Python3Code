#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: pythonDataType.py
# using: os, random, sys

import os,random,sys
sys.setrecursionlimit(1000000)

class Turtle: #Python 中类名约定以大写字母开头
    """关于类的一个简单例子"""
    #属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    #方法
    def climb(self):
        print('我正在努力的向前爬....')

    def run(self):
        print('我正在飞快的向前跑')
    
    def bite(self):
        print('咬死你，咬死你！！！')

    def eat(self):
        print('有的吃，有得喝，很满足～～～～')

    def sleep(self):
        print('困了，睡了，晚安，Zzzzzz')

tt = Turtle()
tt.sleep()
print(str(tt.shell))