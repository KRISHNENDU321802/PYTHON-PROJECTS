#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random as r
t="Y"
def one():
    print("|----------|")
    print("|          |")
    print("|          |")
    print("|    *     |")
    print("|          |")
    print("|          |")
    print("|----------|")
def two():
    print("|----------|")
    print("|          |")
    print("|          |")
    print("|    **    |")
    print("|          |")
    print("|          |")
    print("|----------|")
def three():
    print("|----------|")
    print("|          |")
    print("|          |")
    print("|    *     |")
    print("|   * *    |")
    print("|          |")
    print("|----------|")
def four():
    print("|----------|")
    print("|          |")
    print("|   *  *   |")
    print("|          |")
    print("|   *  *   |")
    print("|          |")
    print("|----------|")
    
def five():
    print("|----------|")
    print("|          |")
    print("|          |")
    print("|   * *    |")
    print("|  * * *   |")
    print("|          |")
    print("|----------|")
    
def six():
    print("|----------|")
    print("|          |")
    print("|  *  *  * |")
    print("|          |")
    print("|  *  *  * |")
    print("|          |")
    print("|----------|")






while(t=="Y"):
    x=r.randint(1,6)
    if(x==1):
        one()
    elif(x==2):
        two()
    elif(x==3):
        three()
    elif(x==4):
        four()
    elif(x==5):
        five()
    elif(x==6):
        six()
    t=input("ENTER Y TO PLAY")
print("Good Bye!!")    


# In[ ]:




