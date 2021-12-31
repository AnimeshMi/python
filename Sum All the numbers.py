#!/usr/bin/env python
# coding: utf-8

# # Write a Python function to sum all the numbers in a list.

# In[2]:


def sum(numbers): #DECLARING THE FUNCTION
    value = 0
    for x in numbers:
        value += x
    return value   #RETURNING TRHE FUNCTION
print(sum((8, 2, 3, 0, 7)))

