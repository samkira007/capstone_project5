#!/usr/bin/env python
# coding: utf-8

# In[11]:


import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread('her.jpg')


# In[12]:



plt.imshow(img)


# In[13]:


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img_gray)


# In[14]:


img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)
plt.imshow(img_blur)


# In[15]:


edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200)

plt.imshow(edges)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




