#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: test.py
# using: support.py

from selenium import webdriver

from time import  sleep

from firebase import firebase
import  matplotlib.pyplot as plt
from pylab import  *
import requests, os
from bs4 import BeautifulSoup
from  urllib.request import urlopen

rcParams['font.sans-serif'] = ['SimHei']

url = "https://aa550872690.firebaseio.com/"
urls = ['http://www.baidu.com']

students = [{'no':1,'name':'张三'}, {'no':2, 'name':'李四'}, {'no':3, 'name':'王五'}]

listx = [1, 5, 7, 9, 13, 16]
listy = [15, 50, 80, 40, 70, 50]

url = 'http://www.tooopen.com/img/87.aspx'

html1 = requests.get(url)
html1.encoding = "utf-8"

sp = BeautifulSoup(html1.text, 'html.parser')

images_dir = "images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

all_links = sp.find_all('a', 'img')
for link in all_links:
    src = link.get('src')
    href = link.get('href')
    attrs = [src, src]
    for attr in attrs:
        if attr != None and ('.jpg' in attr or '.png' in attr):
            full_path = attr
            filename = full_path.split('/')[-1]
            ext = filename.split('.')[-1]
            filename = filename.split('.')[-2]
            if 'jpg' in ext:
                filename = filename + '.jpg'
            else:
                filename = filename + '.png'

            print(filename)

            try:
                image =urlopen(full_path)
                f = open(os.path.join(images_dir, filename), 'wb')
                f.write(image.read())
                f.close()
            except:
                print("{} 无法读取！！".format(filename))

