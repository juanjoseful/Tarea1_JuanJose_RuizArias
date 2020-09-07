#!/usr/bin/env python
# coding: utf-8

# In[9]:


from funciones import *


# la probabilidad de que si se hace este experimento 100 veces, el resultado sean 10 veces cara,

# In[10]:


probabilidad(100,10)


# la probabilidad de que caiga cara mas de 30 veces.

# In[12]:


prob = 0
i = 0
while i<30 or i==30:
     #inicializo
    prob = 1.0 - probabilidad(100,i)
    prob = prob
    i +=1
print(prob)
    


# la funcion Binomial(n,k) como Factorial(n) solo pueden recibir
# enteros y entregar enteros.

# In[13]:


binomial(-5,0)


# In[14]:


binomial(2,10)


# In[15]:


factorial(0)


# In[16]:


factorial(-5)


# In[17]:


factorial(1.1)


# In[ ]:




