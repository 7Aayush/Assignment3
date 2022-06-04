#!/usr/bin/env python
# coding: utf-8

# In[2]:


a = int(input("Enter Number "))

b = bin(a)


print("Binary equivalent of entered number is:",b)


# In[3]:


operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('You have not typed a valid operator, please run the program again.')


# In[ ]:


import math

a=(3+4)*5
print(a)

n=int(input())
b=n*(n-1)/2
print(b)

r=int(input())
c=4*math.pi*(r**2)
print(c)

r_1 = int(input("Enter Number"))
a = int(input("Enter Angle in degrees for cos"))
b=int(input("Enter Angle in degrees for sin"))
c = math.cos(a*math.pi/180)**2
d = math.sin(b*math.pi/180)**2
answ = (r_1*c + r_1*d)**0.5
print(answ)

y1 = int(input("Enter Number y1"))
y2 = int(input("Enter Number y2"))
x1 = int(input("Enter Number x1"))
x2 = int(input("Enter Number x2"))
ansr = (y2 - y1)/(x2 - x1)
print(ansr)


# In[5]:


for a in range(5):
    print(a)
print("-----")    
for b in range(3,10):
    print(b) 
print("-----")     
for c in range(4,13,3):
    print(c)
print("-----")
for d in range(15,5,-2):
    print(d)
print("-----")
for e in range(5,3):
    print(e)
print("-----")    


# In[ ]:


H_w = 1.00794
C_w = 12.0107
O_w = 15.9994
H = int(input("Enter number of hydrogen atoms "))
C = int(input("Enter number of carbon atoms "))
O = int(input("Enter number of oxygen atoms "))
weight= H*H_w + C*C_w + O*O_w
print("The molecular weight=", weight)

