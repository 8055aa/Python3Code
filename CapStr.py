#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: whileLoop.py
# using: random


class CapStr(str):
    def __new__(cls, string):
        string = string.upper()
        return str.__new__(cls, string)
        
    def getPeri(self):
        return (self.x + self.y) * 2

    def getArea(self):
        return self.x * self.y

