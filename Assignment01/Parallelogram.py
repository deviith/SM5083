#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt

# AB
x1 = [2,3]
y1 = [4,0]
# plotting  
plt.plot(x1, y1,color='blue')
# BC
x2 = [3,5]
y2 = [0,3]
# plotting  
plt.plot(x2, y2,color='red')
# CD
x3 = [5,4]
y3 = [3,7]
# plotting  
plt.plot(x3, y3,color='blue')
# AD
x4 = [2,4]
y4 = [4,7]
# plotting 
plt.plot(x4, y4,color='red')

plt.annotate("A", (2,4))
plt.annotate("B", (3,0))
plt.annotate("C", (5,3))
plt.annotate("D", (4,7))


plt.ylabel('$y-axis$')
plt.xlabel('$x-axis$')
plt.grid() 
plt.axis('equal')
plt.show()


# In[ ]:




