#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to reverse a string

# In[2]:


def rev(str):  #Declaring the function
    str1 = ""   # Declaring the string
    for i in str:  
        str1 = i + str1  
    return str1      
     
str = "1234abcd"    # Given String       
print("The reverse string is",rev(str)) 

