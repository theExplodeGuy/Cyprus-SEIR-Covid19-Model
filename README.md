# Cyprus-SEIR-Covid19-Model

# Covid-19 SEIR Modeling

Epidemiology is quite a unique field combining biology, medicine, geography, and statistics. Through computer science the fields of epidemiology are brought together, observed, and analyzed to better our understanding of how diseases spread. In this way the effectiveness of various measures taken by governments and other authorities can be assessed and improved based on feedback got from the efficient analysis of data enabled by computer science. The aim of this essay is to analyze the transition of a population through the main stages of a pandemic using an SEIR model . The Compartmental model assigns the population the labels S, E, I, R (Susceptible, Exposed, Infected, Removed). People may progress through compartments based on several variables (Variables used in the model are transmission rate, contact rate, effective contact rate, the incubation period, days until recovery, death rate and days until death) . Lastly the model attempts to provide feedback on the effectiveness of government measures against a pandemic.   For the development of the model Python3.9 was employed, using the libraries of Pandas, NumPy, SciPy for derivative calculations and Matplotlib for data visualization. 

## Methodology

A model was programmed in python using the SciPy library for solving the system of ordinary differential equations.

The equations of the model were derived based on publicly available SEIR models  as follows:

Change in S population over time:	
ⅆS/ⅆt=( -β * S * I ) / N

Change in E population over time:	
ⅆE/ⅆt=( β * S * I ) / ( N - δ * Ε )

Change in I population over time:	
ⅆΙ/ⅆt=(δ * E * - ( 1 - α) * γ * I - α * ρ * Ι ) / 1

Change in R population over time:

Recoveries:		
ⅆR/ⅆt=( ( 1 - α ) * γ * Ι ) / 1

Deaths:		
ⅆD/ⅆt=( α * ρ * Ι ) / 1

Variables: state ([susceptible, exposed, infected, recovered, deaths]), t (days), 
Constants: N (total_pop), beta (effective_contact_rate), gamma (recovery_rate), delta (incubation_period), rho (days_until_death), alpha (death_rate)

Effective Contact Rate (β): the effective contact rate in the equations bellow is defined as the probability of transmitting a disease multiplied by the contact rate of a particular individual.


The Population Modeling was performed on Cyprus data . The relevant population values at time zero can found in Table1.

```
total_pop = 875899
recovered = 0
infected = 1
susceptible = total_pop - infected - recovered
exposed = 0
deaths = 0
transmission_rate = 0.028 # the ratio between positive results to the whole of the population
incubation_period = 1.0 / 10.0  # incubation period of five days
contact_rate = 17.7 # average people an individual meets
death_rate = 1.4 # 1.4% death rate
until_death = 1/15  # 15 days from infection until death
recovery_rate = 1/15 # 15 days from infection until recovery
effective_contact_rate = transmission_rate * contact_rate
R0 = effective_contact_rate / recovery_rate

```

## Results

The course and the stages of the pandemic without any measures imposed by Cyprus Government, are illustrated in Figure1, predicting an alarming number of infections at about 280 000 resulting to 12 255 deaths, raising concerns about the resilience of the healthcare systems. 

![figure 1](https://user-images.githubusercontent.com/63063093/114308233-ccdd9d80-9aeb-11eb-8494-e61fcdb032c8.PNG)


A decrease in the transmission rate caused by a lockdown (represented as a factor calculated by dividing the transmission rate after and before the lockdown), results in the model predicting a flattening of the curves of Deaths and Infections, implying a release of pressures on the healthcare system.

![figure 2 1](https://user-images.githubusercontent.com/63063093/114308259-df57d700-9aeb-11eb-8d42-99b93c0acdad.PNG) ![figure 2](https://user-images.githubusercontent.com/63063093/114308276-ebdc2f80-9aeb-11eb-9202-7eceb088efd6.PNG)


## Conclusion

In conclusion, this essay has attempted to demonstrate the importance of Computer Science and the help it can provide in a pandemic. In this essay only by exploring a small subfield of statistical modeling it is shown that Computes Science can be immensely helpful to “understand some characteristics of population, how they react and how a disease will spread in a real-world setting” as Dr. Ran Balicer, chief innovation officer at Clalit, stated in an interview for the podcast “Malicious Life”


Please make sure to update data as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
