# Temperature('c) on different dates is+tured in a csv file as (10)
# 'Weather_data.csv' with the fields date, temperature and humidity.
# l.Draw a plot of the weather report with date as the x-axis and temperature as
# the y-axis.
# -
# 2. .Draw a scatter plot of the weather report with date as the x-axis and humidity
# as the y-axis.
# Give appropriate titles and labels in the plot.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('weather.csv')
# x = df['date']
# # print(x)
# y = df['temperature']
# # print(y
# plt.plot(x,y,label="line")
# plt.title("Weather")
# plt.xlabel("Date")
# plt.ylabel("Temperature")
# plt.legend()
# plt.show()

x = df['date']
# print(x)
y = df['humidity']
# print(y)
plt.scatter(x,y,label="line")
plt.title("Weather")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.legend()
plt.show()