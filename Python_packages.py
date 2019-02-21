import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
revenue = [145, 760, 861, 917, 805, 810, 114, 976, 103, 143, 107, 154]
expenses = [120, 569, 123, 120, 865, 840, 328, 582, 697, 166, 100, 380]
revenue_a = np.array(revenue)
expenses_a = np.array(expenses)
profit = revenue_a - expenses_a
print("Profit = %s" %(profit))
Fin_Status = dict(zip(months, profit))
print("Financial Status =" + str(Fin_Status))
print(pd.Series(Fin_Status))
x = months
y = profit
plt.plot(x, y, color="blue", linewidth=2)
plt.xlabel("Months", fontsize=14)
plt.ylabel("Profit", fontsize=14)
plt.show()
