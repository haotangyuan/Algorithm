#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/12 9:47
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
for beer in range(int(82.3 / 2.3)):
    for drink in range(int(82.3 / 1.9)):
        if 2.3 * beer + 1.9 * drink == 82.3 and beer < drink:
            print("Beer =", beer, "Drink =", drink)
