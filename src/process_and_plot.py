import matplotlib.pyplot as plt
import numpy as np

c1 = "United States of America"
c2 = "Uruguay"
# Indexing of columns:
# 0year, 1urban population, 2rural population, 3total emissions,
# 4food transport, 5food consumption
# files don't have headers but should
c1_data = np.genfromtxt(c1+'_processed.csv', delimiter=',', skip_header=1)
c2_data = np.genfromtxt(c2+'_processed.csv', delimiter=',', skip_header=1)

# Fig One: net emissions per capita of both countries as a function of time
c1_emissions_per_capita = c1_data[:, 3]/(c1_data[:, 1]+c1_data[:, 2])
c2_emissions_per_capita = c2_data[:, 3]/(c2_data[:, 1]+c2_data[:, 2])
plt.plot(c1_data[:, 0], c1_emissions_per_capita, label=c1, color='m')
plt.plot(c2_data[:, 0], c2_emissions_per_capita, label=c2, color='b')
plt.xlabel("Year")
plt.ylabel("Emissions Per Capita")
plt.legend()
plt.savefig('fig1.png')
plt.close()
# Fig Two: urban population/(total population) ratio of both countries
c1_urban_rural = 100*c1_data[:, 1]/(c1_data[:, 2]+c1_data[:, 1])
c2_urban_rural = 100*c2_data[:, 1]/(c2_data[:, 2]+c2_data[:, 1])
plt.plot(c1_data[:, 0], c1_urban_rural, label=c1, color='m')
plt.plot(c2_data[:, 0], c2_urban_rural, label=c2, color='b')
plt.xlabel("Year")
plt.ylabel("Urban Population (%)")
plt.legend()
plt.savefig('fig2.png')
plt.close()

# Fig Three: ratio of emissions from food consumption to emissions from
# food transport
c1_consumption_to_transport = c1_data[:, 4]/c1_data[:, 5]
c2_consumption_to_transport = c2_data[:, 4]/c2_data[:, 5]
plt.plot(c1_data[:, 0], c1_consumption_to_transport, label=c1, color='m')
plt.plot(c2_data[:, 0], c2_consumption_to_transport, label=c2, color='b')
plt.xlabel("Year")
plt.ylabel("Ratio of Emissions from Food Transport to Food Consumption")
plt.legend()
plt.savefig('fig3.png')
plt.close()
