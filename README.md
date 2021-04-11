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
Figure 1 - Area Graph. Course of pandemic without any measures taken.

A decrease in the transmission rate caused by a lockdown (represented as a factor calculated by dividing the transmission rate after and before the lockdown), results in the model predicting a flattening of the curves of Deaths and Infections, implying a release of pressures on the healthcare system.

![figure 2](https://user-images.githubusercontent.com/63063093/114308276-ebdc2f80-9aeb-11eb-9202-7eceb088efd6.PNG)
Figure 2.1 - Infections before and after a lockdown was imposed. Effective contact rate falls from 1.4% to 0.28%.

![figure 2 1](https://user-images.githubusercontent.com/63063093/114308259-df57d700-9aeb-11eb-8d42-99b93c0acdad.PNG) 
Figure 2.2 - Deaths before and after a lockdown was imposed.

## Conclusion

In conclusion, this essay has attempted to demonstrate the importance of Computer Science and the help it can provide in a pandemic. In this essay only by exploring a small subfield of statistical modeling it is shown that Computes Science can be immensely helpful to “understand some characteristics of population, how they react and how a disease will spread in a real-world setting” as Dr. Ran Balicer, chief innovation officer at Clalit, stated in an interview for the podcast “Malicious Life”.


Please make sure to update data as appropriate.


## Bibliography

Alberto Godio, Francesca Pace, and Andrea Vergnano, SEIR Modeling of the Italian Epidemic of SARS-CoV-2 Using Computational Swarm Intelligence, Int J Environ Res Public Health, 17:10(2020): 3535.
Baidu. How Baidu is bringing AI to the fight against coronavirus. MIT Technology Review. March 2020. [https://www.technologyreview.com/2020/03/11/905366/how-baidu-is-bringing-ai-to-the-fight-against-coronavirus/ last accessed: 25th November 2020]
David Pringle. Computer science versus COVID-19. Science Business. March 2020. [https://sciencebusiness.net/covid-19/news/computer-science-versus-covid-19 last accessed: 23rd November 2020]
Henri Froese. Infectious Disease Modelling: Beyond the Basic SIR Model. April 2020 [https://towardsdatascience.com/infectious-disease-modelling-beyond-the-basic-sir-model-216369c584c4 last accessed: 1st December 2020]
Julie Shah and Neel Shah. Fighting Coronavirus with Big Data. Harvard Business Review. April 2020. [https://hbr.org/2020/04/fighting-coronavirus-with-big-data last accessed: 29th November 2020]
Mwalili, S., Kimathi, M., Ojiambo, V. et al. SEIR model for COVID-19 dynamics incorporating the environment and social distancing. BMC Res Notes 13(2020):352.
Rob Mitchum. How computer science can help fight COVID-19. UChicagoNews. July 2020. [https://news.uchicago.edu/story/how-computer-science-can-help-fight-covid-19 last accessed: 23rd November 2020]
Tom Rocks Maths. Oxford Mathematician explains SIR Disease Model for COVID-19 (Coronavirus). Tom Rocks Maths YouTube. March 2020. [https://www.youtube.com/watch?v=NKMHhm2Zbkw last accessed: 10th December 2020]
Undefined. SEIR and SEIRS models; HIV Model documentation. Bill and Melinda Gates foundation. 2020 [https://docs.idmod.org/projects/emod-hiv/en/latest/model-seir.html last accessed: 1st December 2020]
3Blue1Brown. Simulating an epidemic. 3Blue1Brown YouTube. March 2020. [https://www.youtube.com/watch?v=gxAaO2rsdIs&t=1038s last accessed: 10th December] 


## License
[MIT](https://choosealicense.com/licenses/mit/)
