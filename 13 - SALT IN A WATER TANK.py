#!/usr/bin/env python
# coding: utf-8

# ## Salt in a Water Tank
# 
# Kaylin Shanahan 2023 
# 
# ---
# This is a Python notebook to estimate the mass of salt in a tank of water over a period of 500 minutes. This will be done using Euler's technique, and display the results on a graph of the numerical and exact analytical solutions.
# <br>
# 
# Initially, the water tank contains 1000 litres of fresh water, with water flowing into the tank at a rate of 10 litres per minute, and flowing out at the same rate. The water flowing has a salt concentration of 0.050 kilograms per litre.
# <br>
# 
# In order to calculate the rate at which the mass of salt changes, we must construct a differential equation. Q will be used to represent the mass of salt in the tank in kilograms, with $ Q_{0} = 0 kg $.
# <br>
# 
# The rate at which the salt is flowing into the tank must be considered, as described by the following equation:
# $$ \frac {dQ}{dt} = +R_{s} $$
# Where $ R_{s} $ is the rate at which salt enters the tank in kilograms per minute, which can be calculated as: 
# $$ R_{s} = (10 L min^{‒1}) (0.050 kg L^{‒1}) = 0.50 kg min^{‒1} $$
# <br>
# 
# As salt is also flowing out of the tank, the rate at which it flows out must also be considered, which is equal to the fraction of water leaving the tank per minute times the amount of salt in the tank:
# $$ \frac {dQ}{dt} = +R_{s} - (\frac {R_{w}}{V}) Q $$
# Where $ R_{w} $ is the rate at which water enters and leaves the tank in litres per minute and V represents the volume of water in the tank in litres. This is the equation which will be used in the Euler routine.
# <br>
# 
# Integrating this equation will provide the equation in a form which can be solved analytically for the exact solution:
# $$ Q = R_{s} ( \frac {V}{R_{w}} )  (1 - e^{-(\frac {R_{w}}{V})t}) $$
# <br>
# 
# * Input the initial conditions
# * Determine the number of steps required
# * Initialise Q and T values
# * Calculate the mass of salt using the differential equation above
# * Output the Q and T values
# * Output a plot of the numerical and analytical solutions on a graph

# In[24]:


# Use Euler's Technique to calculate the mass of salt in a water tank

# Numpy is needed for the natuaral log and exponential function
import numpy as np
# Matplotlib is needed to plot graphs
import matplotlib.pyplot as plt

# Initial conditions
W_0 = 1000           # Initial amount water contained in tank in litres
W_FLOW = 10          # Water flowing in/out tank per minute
Q_0 = 0              # Initial mass of salt in kilograms
Q_IN = 0.5           # Salt flowing into tank per minute

# Time values required for programme
T_MAX = 500          # Iterate up to a maximum time of 500 (minutes)
D_T = 20             # Set the time step in minutes
N = int(T_MAX/D_T)   # Calculate the number of time jumps in minutes

# Set up NumPy arrays to hold the W, Q and t values and initialise
# We need one element more in each array, than the number of jumps
Q = np.zeros(N + 1)
T = np.zeros(N + 1)

# Initialise salt mass in tank
Q[0] = 0
# Initialise time in minutes
T[0] = 0

# Use a for loop to step along the t-axis
for i in range(N):
    # Calculate mass of Q flowing in
    Slope_Q = +Q_IN - ((W_FLOW/W_0) * Q[i])
    Q[i+1] = Q[i] + Slope_Q * D_T

    # Calculate time T at the end of the interval
    T[i + 1] = T[i] + D_T

# Plot the numerical solution as points
plt.plot(T, Q, "ro")
plt.title("Graph of Mass of Salt vs Time")
plt.xlabel("Time (mins)")
plt.ylabel("Mass of Salt in Water Tank (kg)")
plt.grid()

# Plot the analytical solution as a line
# Use the same (N+1) T values
Q_analytic = (Q_IN) * (W_0/W_FLOW) * (1 - np.exp(-(W_IN/W_0)*T))
plt.plot(T, Q_analytic)
plt.show()


# In[25]:


# Find the maximum mass of salt present
MAX_Q = np.max(Q)
print("Maximum mass of salt present is {0:8.2e} kilograms".format(MAX_Q))

# Find the time at which the amount of salt is a maximum
MAX_i = np.argmax(Q)
MAX_T = T[MAX_i]
print("Time at which amount of salt is a maximum is {0:8.2f} minutes".format(MAX_T))

