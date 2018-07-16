#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: strFormat.py
# using: os, 

__author__ = 'Tomas Yang'

from multiprocessing import Process
import os, time, random

'''
def long_time_task(name):
    print('Run task {0} ({1})...'.format(name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task {0} runs {1} seconds.'.format(name, (end - start)))

if __name__ == '__main__':
    print('Parent process {0}.'.format(os.getpid()))
    p = Pool(16)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
'''
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print('{0:10} ==> {1:10d}'.format(name, phone))