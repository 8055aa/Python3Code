#!/usr/bin/env python3

import sys

countries = ["Denmark","Finland","Norway","Sweden"]

list1 = ['spam', 'eggs', 'Apple', 100, 1234]
    
def getInt(msg):
    while True:
        try:
            i = int(input(msg))
            return i
        except ValueError as err:
            print("please input Int")

for x in countries:
    try:
        lens = len(str(x))

        print("{0}'lens is .....{1}".format(x, len(x)))
    except ValueError as err:
        lens = len(str(x))
        print("{0}'lens is .....{1}".format(x, len(x)))


