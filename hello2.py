#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename:str_format.py
"I am : doestr.__doc__"
import imp
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import calendar

message = "After editing"

def printer():
    print('reloaded:',message)

def func(spam, eggs=0, toast = 0, ham = 0):
    print(spam, eggs, toast, ham)

def indirect(func, arg):
    func(arg)

def intersect(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if x not in other :break
        else:
            res.append(x)
    return res

def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res


def outer(x):
    global inner
    def inner(i):
        print(i)
        if i : inner(i - 1)
        inner(x)


class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('Current value = {0}'.format(self.data))

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __mul__(self, other):
        self.data = self.data * other

class Subclass():
    data = 'SPAM'
    def __init__(self, value):
        self.data = value
    def display(self):
        print(self.data, Subclass.data)

def factory(aClass, *args):
    return imp.apply(aClass, args)

class Spam:
    "I am: spam.__doc__ or docstr.spam.__doc__"
    def doit(self, message):
        print(message)

    def method(self, arg):
        "I am: spam.method.__doc__ or self.method.__doc__"
        pass

    def func(args):
        "I am: docstr.func.__doc__"
        pass

class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job



if __name__ == '__main__':
    print('This program is being run by itself')
    '''
    table = {'Python': 'Guido van Rossum', 'Perl':'Larry Wall', 'Tcl': 'John Ousterhout'}
    language = 'Python'
    creator = table[language]
    print(creator)

    for lang in table.keys():
        print("  {0}'s creator is : {1}".format(lang, table[lang]))
    '''
    ''''
    # -*- coding: utf-8 -*-
    """
    Created on Thu Sep 24 16:17:13 2015

    @author: Eddy_zheng
    """

    from matplotlib import pyplot as plt
    import numpy as np
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure()
    ax = Axes3D(fig)
    X = np.arange(-4, 4, 0.25)
    Y = np.arange(-4, 4, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)

    # 具体函数方法可用 help(function) 查看，如：help(ax.plot_surface)
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')

    plt.show()
    '''
    # -*- coding: utf-8 -*-
    """
    Created on Thu Sep 24 16:37:21 2015

    @author: Eddy_zheng
    """

    ''''
    data = np.random.randint(0, 255, size=[40, 40, 40])

    x, y, z = data[0], data[1], data[2]
    ax = plt.subplot(111, projection='3d')  # 创建一个三维的绘图工程
    #  将数据点分成三部分画，在颜色上有区分度
    ax.scatter(x[:10], y[:10], z[:10], c='y')  # 绘制数据点
    ax.scatter(x[10:20], y[10:20], z[10:20], c='r')
    ax.scatter(x[30:40], y[30:40], z[30:40], c='g')

    ax.set_zlabel('Z')  # 坐标轴
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    plt.show()
    '''

    # !/usr/bin/python3


    print("我的姓名是{0}，年龄是{1}".format("杨萌青","20"))

else:
     print("I am being imported from another module")
print('Done')



