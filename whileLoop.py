#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: whileLoop.py
# using: random

import random as r
class MyDecriptor:
 
    def __get__(self, instance, owner):
        print('getting....... ',self, instance, owner)

    def __set__(self, instance, value):
        print('Setting......  ', self, instance, value)

    def __delete__(self, instance):
        print('deleting........ ', self, instance)

class Test:
    x = MyDecriptor()

test = Test()
test.x = 'X - man'

del test.x