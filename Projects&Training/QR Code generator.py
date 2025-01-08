# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 13:01:57 2023

@author: jackh
"""

import pyqrcode
from pyqrcode import QRCode

def QRCode_maker(s, n):
    url = pyqrcode.create(s)
    url.svg("MyQRCode.svg", scale = n)
    

s = input("Input URL: ")
n = input("How large? ")

QRCode_maker(s, n)

