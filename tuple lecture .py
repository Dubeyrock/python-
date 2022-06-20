#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#wap to make an empty list
#wap to make a single element list


# In[3]:


# tuple 

#list---->90% tuple 
#list & tuple are almost excatly the same.
# tuple of int 
x = (1,2,3,0, 9,6)


# In[4]:


x


# In[5]:


type(x)


# In[6]:


#tuple of string
x = ('shivam','python')


# x

# In[9]:


#3.
a = (1,2,3,1,2,3)


# In[11]:


a


# In[12]:


a = (1,2,3,'hello',4,5,9,34.0,6,0,True,'python')


# In[13]:


a


# In[14]:


type(a)


# In[ ]:


#duplicay is allowed in tuple.


# In[ ]:


#slicing with the help of index


# In[ ]:


#wap to slice a data ie 3 from the tuple


# In[15]:


# index--->orderd way
#slicing possible
a


# # muttable or immutable

# In[16]:


a


# In[18]:


a[2]=100


# In[22]:


# tuple --->immutable

a = (1,2,3,'hello', [4,5,34.0,6], 0,True,'python')


# In[23]:


a


# In[24]:


type(a)


# In[25]:


x =[12,34,67,78,89,65,('hello')]


# In[26]:


x


# In[27]:


tuple(x)


# In[28]:


type(x)


# In[29]:


a


# In[30]:


a[3]


# In[31]:


a[7]


# In[35]:


a[4][2]


# In[36]:


a


# In[37]:


a[3]=0


# In[39]:


a[4][2]=0


# In[40]:


a


# In[41]:


a = 1, 2, 3, 'hello',  0, True, 'python'


# In[42]:


a


# In[43]:


type(a)


# In[44]:


# tuple method 
# index 
#count
a


# In[46]:


a.index(0)


# In[47]:


a.index(100)


# In[48]:


a.cont()


# In[49]:


a.count(0)


# In[50]:


a.count(3)


# In[51]:


a.count(4)


# In[52]:


a.count(5)


# In[53]:


a.count(2)


# In[54]:


a.count(2)


# In[55]:


a = ('false', 1,2,3,'hello',0,True,'python')


# In[56]:


a


# In[57]:


a.count(0)


# In[58]:


#wap to create empty tuple
#wap to create songle element tuple .
x = ()
print(x)


# In[59]:


x


# In[60]:


type(x)


# In[61]:


a = (933)
print(x)


# In[62]:


type(x)


# In[63]:


a = ()
print(a)


# In[64]:


type(a)


# In[66]:


a = ('45',)
print(a)


# In[77]:


# maximum of two number  in python
a = [43,67,77,5,89,100]
greatest_num = a[0]
for i in a:
    if i>greatest_num:
        greatest_num = i
        
print(greatest_num)
    


# In[78]:


type(a)


# In[79]:


type(i)


# In[81]:


# minimum of two number in a python 

a = [32,45,67,78,89,90,2]
minimum_num = a[0]
for i in a:
    if i<minimum_num:
        minimum_num = i
        
        print(minimum_num)
        


# In[82]:


type(i)


# In[83]:


type(a)


# In[88]:


#Python | Reversing a List


numbers = [22, 33, 75, 27,17,2,5,6,7,12]


numbers.reverse()


print('Reversed List:', numbers)





# In[92]:


type(a)


# In[93]:


type(i)


# In[ ]:


# Sum of number digits in List

 

