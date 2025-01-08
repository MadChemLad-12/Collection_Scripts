# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:56:16 2023

@author: jackh
"""

### Goals I need to do
# Encript and de-cript password
# Remember and get passwords
# Make new passwords if needed

#Note: This works in VSC but not spyder?

from cryptography.fernet import Fernet

class PasswordManager:
    
    #This is the basic structure of the password manager
    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
        
        #This is key generation for encrypting my password files
    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)
       
     #to save the created key so I can access my passwords again       
    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()
    
    #used to set path to pasword file
    def create_password_file(self, path, initial_values = None):
       self.password_file = path 
       
       #Adding new passwords
       if initial_values is not None:
           for key, value in initial_values.items:
               self.add_password(key, value)

    #Grabing old saved passwords for a given site
    def load_password_file(self, path):
        self.password_file = path
        
        #Ok had to cheat here cause I had now clue what I'm doing
        #load password file fore each line in it
        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")   #We seperate at the colin 
                
                #We read each line and decrypt password then load it into the dictionary
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).encode()        #We read each line and decrypt password then load it into the dictionary

    def add_password(self, site, password):
        #looks for password at specific site
        self.password_dict[site] = password
        
        #append new password if current website doesnt have one
        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode()) #encrypted just makes the last part of the load password easy
                f.write(site + ":" + encrypted.decode() + "\n")
                
    def get_password(self, site):
       return self.password_dict[site]
       
def main(): 
    password = {
        "test":"1234567",
        "facebook":"myfbpassword",
        "youtube":"helloworld12"
        }
    
    pm = PasswordManager()
    
    print("""What do you wnat to do?
    (1) Create a new key
    (2) Load an exisiting key
    (3) Create new password file
    (4) Load existing password file
    (5) Add a new Password
    (6) Get a password
    (q) Quit
    """)

    done = False
    while not done:
        choice = input("enter your choice: ")
        if choice == "1":
            path = input("Enter a path: ")
            pm.create_key(path)
            
        elif choice == "2":
            path = input("Enter a path: ")
            pm.load_key(path)
            
        elif choice == "3":
            path = input("Enter a path: ")
            pm.create_password_file(path, password)
        
        elif choice == "4":
            path = input("Enter a path: ")
            pm.load_password_file(path)
        
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
            
        elif choice == "6":
            site = input("Enter the site: ")
            pm.get_password(site)
            print(f"Password for {site} is {pm.get_password(site)}")
            
        elif choice == "q":
            done = True
            print("Bye")
            
    
        else: 
            print("this is an invalid choice")
            
if __name__ == "__main__":
    main()
























