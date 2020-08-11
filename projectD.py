from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt


def f(t,y):
    '''
    This function accepts a floating point value t and an array y. The array
    has values that correspond to certain things. Beta = infection rate,
    v = recovery rate, S = who can get the disease, I = who can infect others,
    and R = who has recovered and is immune. The function returns another array
    with the derivatives of S, I, and R. Note how the recovery and infection
    rates are constant.
    '''
    [beta, v, S, I, R] = y
    N = S + I + R #total population
    
    SP = (-1/N) * beta * S * I
    IP = (1/N) * beta * S * I - (v * I)
    RP = v * I
    
    return np.array([0, 0, SP, IP, RP])

def fV(t,y):
    '''
    This functions does the same thing as f(t, y) with the addition of two 
    values, p and V. p = fraction of S population that is vaccinated daily,
    and V = total vaccinated population. The function returns the derivatives 
    of S, I, R, and V. Note how, in addition to the recovery and infected rate,
    the vaccination rate is also constant.
    '''

    [beta, v, p, S, I, R, V] = y
    N = S + I + R + V #total population
    
    SP = (-1/N) * beta * S * I - (p * S)
    IP = (1/N) * beta * S * I - (v * I)
    RP = v * I
    VP = p * S
    
    return np.array([0, 0, 0, SP, IP, RP, VP])

def calcSIR(beta, v, S0, I0, R0):
    '''
    This function uses the scipy module to solve the differential equations in
    f(t, y) when given the parameters. The function returns an array with the 
    values of S, I, and R over 365 days.
    '''

    y0 = np.array([beta, v, S0, I0, R0])
    t_start = 0
    t_end = 364
    N = 365 # Number of time points
    t = np.linspace(t_start, t_end, N)
    result = solve_ivp(f, [t_start, t_end], y0, t_eval=t) #solve differentials
    
    S = result.y[2]
    I = result.y[3]
    R = result.y[4]
    
    return (t,S,I,R) # Return results here
    
def calcSIRV(beta, v, p, S0, I0, R0, V0):
    '''
    This function uses the scipy module to solve the differential equations in
    fV(t, y) when given the parameters. The function returns an array with the 
    values of S, I, R, and V over 365 days.
    '''

    y0 = np.array([beta, v, p, S0, I0, R0, V0])
    t_start = 0
    t_end = 364
    N = 365 # Number of time points
    t = np.linspace(t_start, t_end, N)
    result = solve_ivp(fV, [t_start, t_end], y0, t_eval=t) #solve differentials
    
    S = result.y[3]
    I = result.y[4]
    R = result.y[5]
    V = result.y[6]
    
    return (t,S,I,R,V)
    
def plotSIR(t,S,I,R):
    '''
    This functions plots how S, I, and R change over time. Also, the figure is
    formatted to display a legend, title and x/y labels. 
    '''

    plt.figure()
    
    plt.plot(t, S, label='Susceptible')
    plt.plot(t, I, label='Infected')
    plt.plot(t, R, label='Recovered')
    
    plt.title('SIR Model')
    plt.xlabel('Day')
    plt.ylabel('Number')
    plt.legend(loc='best')
    
    plt.xlim(0,364)
    plt.ylim(0, 1500)
    
def plotSIRV(t,S,I,R,V):
    '''
    This functions plots how S, I, R, and V change over time. Also, the figure is
    formatted to display a legend, title and x/y labels. 
    '''

    plt.figure()
    
    plt.plot(t, S, label='Susceptible')
    plt.plot(t, I, label='Infected')
    plt.plot(t, R, label='Recovered')
    plt.plot(t, V, label='Vaccinated')
    
    plt.title('SIRV Model')
    plt.xlabel('Day')
    plt.ylabel('Number')
    plt.legend(loc='best')
    
    plt.xlim(0, 364)
    plt.ylim(0, 1500)
    
def main():
    '''
    This function calls other functions in this script to simulate the 
    progression of a disease over 365 days. 4 different scenarios are provided
    so there are 4 different blocks of code below. To receive a plot of a 
    simulations, simply delete the octothorpe before the code lines. I will 
    describe each one below.
    '''
    
    '''
    Simulation 1: The code block below provides a simulation for the initial 
    condition of 1500 susceptible people and 1 infected. The initial infection 
    and recovery rates are 0.5 and 0.1 respectively.
    In terms of variables:
        beta = 0.5
        v = 0.1
        S0 = 1500
        I0 = 1
        R0 = 0
    '''
    #(t, S, I, R) = calcSIR(0.5, 0.1, 1500, 1, 0)
    #plotSIR(t, S, I, R)
    
    '''
    Simulation 2: The code block below provides a simulation for the same 
    initial conditions as simulation 1, but social distancing measures and
    mask-wearing are now strongly encouraged. These measures are used to 
    flatten the curve of infections so the healthcare system isn't overloaded.
    The infection rate now decreases because of these measures.
    In terms of variables:
        beta = 0.15 (was 0.5 before)
        v = 0.1
        S0 = 1500
        I0 = 1
        R0 = 0
    '''
    (t, S, I, R) = calcSIR(0.15, 0.1, 1500, 1, 0)
    plotSIR(t, S, I, R)
    
    '''
    Simulation 3: The code block below provides a simulation for the same
    initial conditions as simulation 1, but there is now a treatment for the
    disease that doubles the recovery rate. This means that people aren't 
    infected as long.
    In terms of variables:
        beta = 0.5 
        v = 0.2 (was 0.1 before)
        S0 = 1500
        I0 = 1
        R0 = 0
    '''
    #(t, S, I, R) = calcSIR(0.5, 0.2, 1500, 1, 0)
    #plotSIR(t, S, I, R)
    
    '''
    Simulation 4: The code block below provides a simulation for the initial 
    condition of 1000 susceptible people, 1 infected, and 500 vaccinated. The
    initial infection and recovery rates are 0.5 and 0.1 respectively. Since
    a vaccine is now available, 1% of the susceptible population is vaccinated
    every day (this percentage is represennted by the variable p). 
    In terms of variables:
        beta = 0.5 
        v = 0.1
        p = 0.01
        S0 = 1000
        I0 = 1
        R0 = 0
        V0 = 500
    '''
    #(t, S, I, R, V) = calcSIRV(0.5, 0.1, 0.01, 1000, 1, 0, 500)
    #plotSIRV(t, S, I, R, V)
    
    
if __name__== "__main__":
    from IPython import get_ipython
    get_ipython().run_line_magic('matplotlib', 'auto') 
    plt.close('all')
    main()