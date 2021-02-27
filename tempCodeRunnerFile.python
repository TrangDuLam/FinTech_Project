from yahoo_fin import stock_info
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

price = stock_info.get_data("2330.TW", start_date='01/01/2021')["adjclose"]
date = price.index

plt.plot(date, price)
plt.xlabel('date')
plt.ylabel("price")
plt.show()
