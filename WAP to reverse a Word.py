#!/usr/bin/env python
# coding: utf-8

# # Write a Python program that accepts a word from the user and reverse it.

# In[1]:


char = input("Enter a word  ")
for reverse in range(len(char) -1,-1,-1):
    print(char[reverse],end="")

