#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[5]:


np.__version__

#_ _(有兩個)


# In[36]:


#生成一個等差數列，首數為 0，尾數為 20，公差為 1 的數列。
np.arange(21)


# In[37]:


#呈上題，將以上數列取出偶數。
np.arange(2,21,2)


# In[44]:


#呈 1 題，將數列取出 3 的倍數。
np.arange(0,21,step=3)


# In[47]:


a = np.arange(0,21,step=3)
print("包含結束值:", a)


# In[ ]:




