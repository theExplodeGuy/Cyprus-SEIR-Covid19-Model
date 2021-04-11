#%%

import pandas as pd
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# flatten the curve based on contact_rate
def adjust_rate(contact_rate, day):
    if day > 50:
        return contact_rate * 0.2
    else:
        return contact_rate

# The SIR model differential equations.
def deriv(state, t, N, beta, gamma, delta, rho, alpha):
    S, E, I, R, D = state
    
    # Change in S population over time
    dSdt = -beta * S * I / N
    # Change in R population over time
    dEdt = beta * S * I / N - delta * E
    # Change in I population over time
    dIdt = delta * E - (1 - alpha) * gamma * I - alpha * rho * I
    # Change in R population over time
    dRdt = (1 - alpha) * gamma * I

    dDdt = alpha * rho * I

    return dSdt, dEdt, dIdt, dRdt, dDdt

def deriv_adj(state, t, N, beta, gamma, delta, rho, alpha):
    S, E, I, R, D = state
    beta = adjust_rate(beta, t)
    
    # Change in S population over time
    dSdt = -beta * S * I / N
    # Change in R population over time
    dEdt = beta * S * I / N - delta * E
    # Change in I population over time
    dIdt = delta * E - (1 - alpha) * gamma * I - alpha * rho * I
    # Change in R population over time
    dRdt = (1 - alpha) * gamma * I

    dDdt = alpha * rho * I

    return dSdt, dEdt, dIdt, dRdt, dDdt


total_pop = 875899 


transmission_rate = 0.028
incubation_period = 1.0 / 10.0  # incubation period of five days
contact_rate = 17.7
death_rate = 0.014  # 1.4% death rate
until_death = 1/15  # 15 days from infection until death


effective_contact_rate = transmission_rate * contact_rate

# A list of days, 0-360
days = range(0, 360)
recovery_rate = 1/15

# We'll compute this for fun
print("R0 is", effective_contact_rate / recovery_rate)

# What's our start population look like?
# Everyone not infected or recovered is susceptible

recovered = 0
infected = 1
susceptible = total_pop - infected - recovered
exposed = 0
deaths = 0



# Use differential equations magic with our population
ret = odeint(deriv,
             [susceptible, exposed, infected, recovered, deaths],
             days,
             args=(total_pop, effective_contact_rate, recovery_rate, incubation_period, until_death, death_rate))
S, E, I, R, D = ret.T

ret = odeint(deriv_adj,
             [susceptible, exposed, infected, recovered, deaths],
             days,
             args=(total_pop, effective_contact_rate, recovery_rate, incubation_period, until_death, death_rate))
Sadj, Eadj, Iadj, Radj, Dadj = ret.T


# Build a dataframe to use in ploting
df = pd.DataFrame({
    'suseptible': S,
    'exposed': E,
    'infected': I,
    'recovered': R,
    'deaths': D,
    'day': days
})
print(df)
plt.style.use('ggplot')
df.plot(x='day',
        y=['infected', 'suseptible', 'exposed', 'recovered', 'deaths'],
        color=['#d56d92', '#246a49', '#55246c', '#fada5e', '#00688b'],
        kind='area',
        stacked=False)

print("R after measures is", adjust_rate(effective_contact_rate, 51) / recovery_rate)

df = pd.DataFrame({
    'infected': I,
    'infected_lockdown': Iadj,
    'day': days
})


plt.style.use('ggplot')
df.plot(x='day',
        y=['infected', 'infected_lockdown'])

df = pd.DataFrame({
    'deaths': D,
    'deaths_lockdown': Dadj,
    'day': days
})

plt.style.use('ggplot')
df.plot(x='day',
        y=['deaths', 'deaths_lockdown'])


# %%
