#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename:guizeroTest.py

from guizero import *

app = App(title = "Hello world")
build_a_snowman = yesno("A question...","Do you want to build a snowman?")
if build_a_snowman == True:
    info("Snowman","It doesn't have to be a snowman")
else:
    error("Snowman", "Okay bye...")

app.display()
