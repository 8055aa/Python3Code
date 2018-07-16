#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: pythonDataType.py
# using: os, 

class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0 )

    def __len__(self):
        return len(self.values)

    def __getitem__(self, Key):
        self.count[Key] += 1
        return self.values[Key]