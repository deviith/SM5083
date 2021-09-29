
# Show that (2, 4), (3, 0), (5, 3) and (4, 7) arethe vertices of a Parallelogram.

# In[2]:


import numpy as np


# In[3]:


vecA = np.array([2,4])
vecB = np.array([3,0])
vecC = np.array([5,3])
vecD = np.array([4,7])
print(f'A ={vecA}\n B ={vecB}\n C ={vecC}\n D ={vecD}')


# ABCDcan be a ‖gm if its opposite sides are parallel <br> i.e A−B=k1(D−C) andA−D=k2(B−C)

# In[4]:


vecAB = vecA - vecB
vecDC = vecD - vecC
print(f'AB = {vecAB}')
print(f'DC = {vecDC}')


# In[5]:


vecAD = vecA - vecD
vecBC = vecB - vecC
print(f'AC = {vecAD}')
print(f'BC = {vecBC}')


# In[6]:


if np.all((vecAB == vecDC) & (vecAD == vecBC)) :
    print('Here Opposite sides AB‖CD and AD‖BC \n  ∴  ABCD is a Parallelogram')
else:
    print('Here Opposite sides  are not parallel  \n  ∴  ABCD is not  a Parallelogram')


# Here Opposite sides AB‖CD and AD‖BC  ∴  ABCDis a ‖gm as the opposite sides are parallel.

# In[ ]:




