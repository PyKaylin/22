#!/usr/bin/env python
# coding: utf-8

# ## 3D Polar Coordinate Conversion
# 
# Kaylin Shanahan 2022
# 
# ---
# This is a python programme to convert spherical polar coordinates of $(r, \theta , \phi)$ to cartesian coordinates $(x, y, z)$ using a function.
# 
# <br>
# In 3 dimensions a point can be defined by cartesian coordinates $(x, y, z)$ or spherical polar 
# coordinates $(r, \theta, \phi)$.
# <br>
# These cartesian coordinates and sperical polar coordinates are related by the following equations: 
# <br>
# $$ x = r sin \theta cos \phi $$
# $$ y = r sin \theta sin \phi $$
# $$ z = r cos \theta $$
# 
# * Define function to convert polar coordinates to cartesian coordinates
# * Input spherical polar coordinate values of $(r, \theta , \phi)$
# * Calculate cartesian coordinates $(x, y, z)$ with function using equations outlined above
# * Output cartesian coordinates $(x, y, z)$

# In[8]:


# Numpy is needed for our calculations
import numpy as np

# Define the function to convert polar coordinates to cartesian coordinates
def cart(r, t, p):
    x = (r)*(np.sin(t*np.pi/180))*(np.cos(p*np.pi/180))
    y = (r)*(np.sin(t*np.pi/180))*(np.sin(p*np.pi/180))
    z = (r)*(np.cos(t*np.pi/180))
    return x, y, z
    
# Main programme
def main():
    radius = eval(input("Enter a value for radius in metres: "))
    theta = eval(input("Enter a value for theta in degrees: "))
    phi = eval(input("Enter a value for phi in degrees: "))
    [xv, yv, zv] = cart(radius, theta, phi)
    
    # Display cartesian coordinates
    print("The cartesian coordinates are:")
    print("x = {0:10.2e}".format(xv), "metres")
    print("y = {0:10.2e}".format(yv), "metres")
    print("z = {0:10.2e}".format(zv), "metres")
    
main()


# In[9]:


# Numpy is needed for our calculations
import numpy as np

# Define the function to convert polar coordinates to cartesian coordinates
def cart(r, t, p):
    x = (r)*(np.sin(t*np.pi/180))*(np.cos(p*np.pi/180))
    y = (r)*(np.sin(t*np.pi/180))*(np.sin(p*np.pi/180))
    z = (r)*(np.cos(t*np.pi/180))
    return x, y, z
    
# Main programme
def main():
    radius = eval(input("Enter a value for radius in metres: "))
    theta = eval(input("Enter a value for theta in degrees: "))
    phi = eval(input("Enter a value for phi in degrees: "))
    [xv, yv, zv] = cart(radius, theta, phi)
    
    # Display cartesian coordinates
    print("The cartesian coordinates are:")
    print("x = {0:10.2e}".format(xv), "metres")
    print("y = {0:10.2e}".format(yv), "metres")
    print("z = {0:10.2e}".format(zv), "metres")
    
main()

