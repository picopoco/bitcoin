import matplotlib.pyplot as plt
from pandas import DataFrame, read_csv
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
import numpy as np
import pandas as pd
#define data location
import pylab as pl

df = read_csv('t/bch.csv')
pl.xticks(rotation = 90)
# xs = df['date'][:30]
# print (xs)

ys = df['price'][:30]
print (ys)

#df.Datetime = pd.to_datetime(df.date)
#df.set_index('date')
ys.plot()