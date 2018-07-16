#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename:continue.py

if __name__ == '__main__':
    while True:
        s = input('Enter something :')
        if s == 'quit':
            break
        if len(s) < 3:
            print('Too small')
            continue
        print('Input is of sufficient length')
        # Do other kinds of processing here..

