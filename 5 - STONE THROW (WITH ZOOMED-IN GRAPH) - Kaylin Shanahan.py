#!/usr/bin/env python
# coding: utf-8

# ## Stone Throw Graph
# 
# Kaylin Shanahan 2022 
# 
# ---
# This is a python programme that can describe the motion of a ball thrown using the kinematic equation. The programme can then display the motion of the ball, which is thrown vertically upwards at the edge of a 50 m high cliff with an initial velocity of 40 ms<sup>-1</sup>, on a graph of height of the ball as a function of time, over a 10-second period. Using this graph, we can then estimate the time taken for this ball to hit the ground at the base of the cliff. 
# 
# 
# <br>
# The motion of the ball can be described with the following kinematic equation: 
# <br>
# $$ x(t) = x_0 + v_0t + \frac {1}{2} at ^{2} $$
# Where $ x_0 $ is the initial position, $ v_0t $ is the initial velocity, $ a $ is acceleration and $ t $ is time.
# 
# 
# It is important to remember we must consider the effects of gravity on the upward and downward speed of the the ball, where,
# $$ g = \left({- / +} \right)   9.81 ms^{2} $$
# 
# * Input given values for intial position, initial velocity and acceleration/deceleration
# * Calculate the motion of the ball as a function of time using the kinematic equationin an array operation
# * Output a graph of the height of the ball as a function of time
# * Output a graph of the height of the ball as a function of time zoomed in on the region where the height value is 0
# * Estimate the time taken for the ball to reach the ground

# In[13]:


# Numpy is needed for our calculations
import numpy as np 

# Matplotlib is needed to plat a graph of Height vs Time
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')

# Terms used in equation:
x_0 = 50 # Initial position of ball in m
v_0 = 40 # Initial velocity of ball in ms^-1
a = -9.81 # Acceleration of ball, due to gravity, in ms^-2

# Define a linearly spaced array of time values, t in seconds
t = np.linspace(0, 10)

# in an array operation calculate the height of the ball, h as a function of time, t
h = x_0 + v_0*t + 0.5*a*t**2

# plot the graph of the height of the ball as a function of time
plt.plot(t, h) 
plt.title("Motion of a Ball Thrown from a Cliff") 
plt.xlabel("Time $(s)$")
plt.ylabel("Height $(m)$")
plt.ticklabel_format(style = 'sci', axis = 'both', scilimits = ( -2,2) ) 
plt.grid() 
plt.show()


# In order to find the most accurate estimate of how long it takes the ball to hit the ground possible from our graph, we must zoom-in on the region of interest.
# <br>
# In this case, this means producing a zoomed-in graph to estimate the y-value, time, where the x-value, height, is 0.

# In[14]:


# Zoom-in on the graph to find the probable time taken for the ball to hit the ground
plt.plot(t, h) 
plt.xlim(8, 10) 
plt.ylim(-2.5, 2.5) 
plt.title("Motion of a Ball Thrown from a Cliff") 
plt.xlabel("Time $(s)$")
plt.ylabel("Height $(m)$")
plt.ticklabel_format(style = 'sci', axis = 'both', scilimits = ( -2,2) ) 
plt.grid() 
plt.show() 


# From the graph in the code cell above, we can estimate that the point on the graph whre h = 0 is (0, 9.25). 
# <br>
# This means that the time taken for the ball to hit the ground is approximately 9.25 seconds.
