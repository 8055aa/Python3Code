#!/usr/bin/env python3
# encoding:UTF-8
# Filename: test.py

import cmath
import random
import sys

__author__ = 'Thomas Yang'
__project__ = 'This is My Simple Python Application '

'''
a = float(input('输入三角形第一边长：'))
b = float(input('输入三角形第二边长：'))
c = float(input('输入三角形第三边长：'))
while a + b <= c or a + c <= b or b + c <= a:
    print('输入的边构不成三角形，请重新输入！！')
    a = float(input('输入三角形第一边长：'))
    b = float(input('输入三角形第二边长：'))
    c = float(input('输入三角形第三边长：'))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print('三角形的面积为： %0.2f' % area)              '''

# print(random.randint(0, 9))
'''
num = int(input('请输入一个数字：'))
if(num % 2) == 0:
    print('{0} 是偶数'.format(num))
else:
    print('{0} 是奇数'.format(num))        '''
# Python 程序用于检测用户输入的数字是否为质数

'''
# 用户输入数字
num = int(input("请输入一个数字: "))

# 质数大于 1
if num > 1:
    # 查看因子
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "不是质数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")

# 如果输入的数字小于或等于 1，不是质数
else:
    print(num, "不是质数")      '''

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 1, 1, 1, 2]
list3 = ["a", "b", "c", "d"]

tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

dict1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict2 = {'abc': 987}


def area(width, height):
    return width * height


def print_welcome(name):
    print("Welcome {0} !!!!!!".format(name))


def ChangeInt(a):
    a = 10
    print(a)


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出：")
    print(arg1)
    for var in vartuple:
        print(var)
    return


def outer():
    num = 10

    def inner():
        nonlocal num
        num = 200
        print(num)

    inner()
    print(num)


def change_me(mylist):
    mylist = [1, 2, 3, 4, 5]
    print("函数内取值：", mylist)
    return

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)

if __name__ == '__main__':
    print('程序自身运行')
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{0} x {1} = {2}\t'.format(j, i , i*j), end =' ')
        print()
else:
    print('我来自另一个模块')


