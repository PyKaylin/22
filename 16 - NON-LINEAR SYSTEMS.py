#!/usr/bin/env python
# coding: utf-8

# ## Non-Linear Systems
# 
# Kaylin Shanahan 2023 
# 
# ---
# This is a python function which takes as parameters, the initial population $ x_{0} $, the growth parameter $ r $, and the number of generations $ N $, and returns an array containing the $ N $ successive population values. This will be done using the May equation, and display the results on a graph. This graph will display $ 50 $ successive population values for two different initial population values, which we will then use a while-loop determine after how many generations the populations diverge by $ 20 \% $.
# <br>
# 
# In a population model, successive populations are related by the May equation:
# $$ X_{i+1} = x_{i}e^{r(1-x_{i})} $$
# <br>
# 
# 
# 
# In this particular population model, our initial growth parameter $ r $ is set to $ 3.0 $ and the number of genertions $ N $ is set to $ 50 $.
# 
# The first population will have an initial population of $ X_{0} = 2.00000 $.
# The second population will have an initial population of $ X_{0} = 2.00001 $.
# <br>
# 
# * Input function to determine number of steps required
# * Input intial conditions
# * Calculate the populations using the May equation
# * Calculate the number of populations at which they diverge by 20%
# * Output number of generations
# * Output a plot of population 1 and population 2 on a graph

# In[3]:


# Function to calculate N generations of the May equation
# with growth parameter r and initial population X_0
# Returns an array X containing the populations

def logistic(X_0, r, N):
    
    import numpy as np
    X = np.zeros(N)
    X[0] = X_0
    
    for i in range(N - 1):
        X[i+1] = X[i] * np.exp(r*(1 - X[i]))
        
    return X


# In[5]:


def main():
    
    import matplotlib.pyplot as plt
    
    X1_0 = 2.00000   # set the initial population of Population 1
    X2_0 = 2.00001   # set the initial population of Population 2
    r = 3.0          # set the growth parameter
    N = 50           # set the number of generations
    
    # Call the function which calculates the populations of Population 1
    X1 = logistic(X1_0, r, N)
    
    # Call the function which calculates the populations of Population 2
    X2 = logistic(X2_0, r, N)
    
    # Determine after how many generations the populations diverge by 20%
    i = 0
    while abs(((X1[i] - X2[i]) / X1[i])) < 0.2:
        i += 1
    print("Population diverges by 20% after " +  str(i) + " generations")
    
    # Plot population against generation
    plt.plot(range(N), X1)
    plt.plot(range(N), X2, linestyle = 'dashed')
    plt.xlim(0, N)
    plt.ylim(0, 1.0)
    plt.legend(['Population 1', 'Population 2'], loc ="lower left")
    plt.xlabel("Generation i")
    plt.ylabel("Population $x_i$")
    plt.title("May Equation, $X1_0$ = {0:5.3f}, $X2_0$ = {0:5.3f}, r = {1}".format(X1_0, X2_0, r))
    plt.grid()
    
main()

