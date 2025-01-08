# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:39:48 2023

@author: jackh
"""

import random 

def Password_Generator(Length):
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password = "".join(random.sample(s,Length ))
    print(password)
    

#Password_Generator(10)    



