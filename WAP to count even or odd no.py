#!/usr/bin/env python
# coding: utf-8

# # Write a Python program to count the number of even and odd numbers from a series of numbers.
# Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
# 
# Expected Output :
# 
# Number of even numbers : 5
# 
# Number of odd numbers : 4

# In[29]:


#Case 1------>   Considering the error is not intentional on the Edyoda page then true value comes out to be-

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for value in numbers:
    if (not value % 2):
            even+=1
    else:
            odd+=1  
            
print("Number of even numbers : ",even)
print("Number of odd numbers : ",odd)


# In[1]:


#Case 2------>   Considering the error is intentional on the Edyoda page then this would be the following case-
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for value in numbers:
    if (not value % 2):
            odd+=1
    else:
            even+=1  
            
print("Number of even numbers : ",even)
print("Number of odd numbers : ",odd)

