#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: Hello.py
# using: os, random

import os,random
from collections import Iterable

secret = random.randint(1,10)
print('-------------------------Thomas Yang---------------------')
temp = input('Please enter a number:')
guess = int(temp)
count = 0
while((guess != secret) and (count < 4)):
 
    if guess == secret:
        print("Bingo ,That's right.")
    else:
        if guess > secret:
            print('It\'s Big')
        else:
            print('It\'s Small')
        count = count + 1
    temp = input("Sorry,It's fault, Please enter another number:")
    guess = int(temp)

print('------------------GAME OVER-------------------------------')