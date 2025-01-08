# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:20:30 2023

@author: jackh
"""

#Email Slicer

def Email_Slicer(email=None):
    email = email.strip()
    username = email[:email.index("@")]
    domain_name = email[email.index("@")+1:]
    format = ("Your user name is ", username, "and your domain is ",domain_name)
    print(format)
    

#Test
#my_email = "jack.hinsch@griffithuni.edu.au"
#Sliced =  Email_Slicer(my_email)    
