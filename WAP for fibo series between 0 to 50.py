#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to get the Fibonacci series between 0 to 50

# In[36]:


x=0
y=1
sum=0
max=50
if (sum<50):
    for fibo in range(0,max):
        print(sum,end=" ")
        x=y
        y=sum
        sum=x+y

