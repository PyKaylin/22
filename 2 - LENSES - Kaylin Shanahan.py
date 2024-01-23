#!/usr/bin/env python
# coding: utf-8

# ## Lenses: Kaylin Shanahan 26/09/22
# 
# ---
# A python programmme to calculate the image distace and magnification of a convex lens using the equations:
# 
# $$ \frac{1}{f} = \frac{1}{d_{o}} + \frac{1}{d_{i}} $$
# $$ m = - \frac{d_{i}}{d_{o}} $$
# 
# 1. Ask the user to input the value for focal length in centimetres.
# 2. Calculate the image distance value and magnification using the formulas.
# 3. Output the answer.
# 
# 

# In[4]:


# Input values for f and do
f = eval(input("Enter value for focal length in centimetres: "))
do = eval(input("Enter value for object distance in centimetres: "))

# Calculate the image distance and magnification
di = 1 / ((1/f) / (1/do))
m = - (di/do)

# Output the answer
print ("The image distance is: {0:6.1} centimetres".format(di))
print ("The magnification is: {0:10.2e}".format(m))

