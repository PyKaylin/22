#!/usr/bin/env python
# coding: utf-8

# ## Power Series Expansion for Arcsin
# 
# Kaylin Shanahan 2022 
# 
# ---
# This is a python programme to calculate arcsin to 12 significant digits with a function using a while loop. 
# <br>
# 

# In[3]:


# Power series expansion for arcsin

def psarc(x): 
    import numpy as np 

    accuracy = 1e-12

    # Initialise the zeroth term and the sum 
    n = 0
    termn = 1
    powersum = termn

    # use a while Loop to get the required accuracy 
    while (abs(termn / powersum) > accuracy):
        n = n + 1
        termn = termn * x / n 
        powersum = powersum + termn

    print("Number of terms in power series = ", n) 
    print("Power series expansion for arcsin(x) = ", powersum) 
    print("NumPy result for arcsin(x) = ", (x))

psarc(0.25)
psarc(0.95)

