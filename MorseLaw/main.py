import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
#ln(TranistorCount(year))=M.year+b
slope = np.log(2) /2 #given everry two year count doubles 
interception = np.log(2250)-np.log(2)/2*1971
mooreslaw = lambda x:np.exp(slope*x+interception)

data = pd.read_csv("output.csv")
model = np.polynomial.Polynomial.fit(data["Year"],np.log(data["Transistor count"]),deg=1)
b,m=model.convert()

year = data["Year"]
transistor_count = data["Transistor count"]
transistor_Moores_law = mooreslaw(year)
transistor_count_predicted = np.exp(b)*np.exp(m*year)

#plt.semilogy(year, transistor_count, "s", label="MOS transistor count")
#plt.semilogy(year, transistor_count_predicted, label="linear regression")
#plt.plot(year, transistor_Moores_law, label="Moore's Law")
#plt.title(
#    "MOS transistor count per microprocessor\n"
#    + "every two years \n"
#    + "Transistor count was x{:.2f} higher".format(np.exp(m * 2))
#)
#plt.xlabel("year introduced")
#plt.legend(loc="center left")
#plt.ylabel("# of transistors\nper microprocessor")
#plt.show()
transistor_count2020 = transistor_count[year == 2020]
print(transistor_count2020.max(),transistor_count2020.min(),transistor_count2020.mean())
plt.plot(
    2020 * np.ones(np.sum(year == 2020)),
    transistor_count2020,
    "ro",
    label="2020",
    alpha=0.2,
)
year = np.linspace(2019.5,2020.5)
transistor_Moores_law = mooreslaw(year)
transistor_count_predicted = np.exp(b)*np.exp(m*year)
plt.plot(2020, transistor_count2020.mean(), "g+", markersize=20, mew=6)
plt.plot(year,transistor_count_predicted, label="Your prediction")
plt.plot(year,transistor_Moores_law, label="Moores law")
plt.ylabel("# of transistors\nper microprocessor")
plt.legend()
plt.xscale("linear")
plt.show()
np.savez(
    "mooreslaw_regression.npz",
    year=year,
    transistor_count=transistor_count,
    transistor_count_predicted=transistor_count_predicted,
    transistor_Moores_law=transistor_Moores_law,
    regression_csts=(b, m),
)
