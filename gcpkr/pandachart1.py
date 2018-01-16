import numpy as np
import matplotlib.pyplot as plt

# Here you put your code to read the CSV-file into a DataFrame df
from pandas import DataFrame, read_csv
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd
#define data location
df = read_csv('t/bch.csv')
plt.xticks(rotation = 90)
xs = df['date'][:100]
print (xs)
ys = df['price'][:100]
print (ys)

xs = pd.to_datetime(xs)
#xs = df.set_index('date')
print(xs)
print('len',len(df))
#for i in range(len(df)):
#for i in range(100):
#     xs = np.array(df['date'])[i] # Use values from odd numbered columns as x-values
#     ys = np.array(df['price'])[i] # Use values from even numbered columns as y-values
#     plt.plot(xs, ys, marker='o', label=df.index[i])
#     for j in range(len(xs)):
#         plt.annotate(df.columns[0::2][j][-3:] + '"', # Annotate every plotted point with last three characters of the column-label
#                      xy = (xs[j],ys[j]),
#                      xytext = (0, 6),
#                      textcoords = 'offset points',
#                      va = 'bottom',
#                      ha = 'center',
#                      rotation = 90,
#                      clip_on = True)


plt.plot(xs, ys*2 ,label='bch1')
plt.plot(xs, ys, label='bch')
plt.title('coin  classes')
plt.xlabel('Exposure Time')
plt.ylabel('price')

#plt.grid(alpha=0.4)
#plt.yscale('log')
plt.legend(loc='best', title='bitcoin class')
#plt.legend(['y = x', 'y = 2x',], loc='upper left',title='bitcoin class)

plt.show()


# df = pd.read_csv('t/bch.csv')
#
# sample_data_table = FF.create_table(df.head())
# py.iplot(sample_data_table, filename='sample-data-table')
#

