import numpy as np
import matplotlib.pyplot as plt

# Here you put your code to read the CSV-file into a DataFrame df
from pandas import DataFrame, read_csv
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import  plotly
import  collections
from plotly.graph_objs import Scatter, Layout


import pandas as pd
import common
#define data location



def  runchart(coinObj):
    plt.xticks(rotation = 90)
    # xs = df['date'][:100]
    # print (xs)
    # ys = df['price'][:100]
    # print (ys)
    print (list(coinObj.keys())[0])
    xs = coinObj[list(coinObj.keys())[0]]['date'][:100]
    xs = pd.to_datetime(xs)
    #print(xs)
    #coinList = list(coinObj)
   # for idx, coinNM in enumerate(coinList):
    idx = 1
    print('len',len(coinObj))
    # coinList = []
    # coinNmList = []
    for coinNM  in coinObj:
         xs = coinObj[coinNM]['date'][:100]
         xs = pd.to_datetime(xs)
         ys = coinObj[coinNM]['price'][:100]
         coinObjlen = len(coinObj)
         subnum =  coinObjlen *100 +10 + idx
         plt.subplot(subnum)
         plt.ylabel(coinNM)
         plt.xlabel('Exposure Time')
         plt.plot(xs, ys ,label=coinNM)
         plt.grid(True)
         plt.legend(loc='best', title=coinNM)
         idx += 1
        # plt.title(coinNM)
         # coinList.append([Scatter(x=xs, y=ys)])
         # coinNmList.append(Layout(title=coinNM))

    # plotly.offline.plot({
    #     "data":  [Scatter(x=xs, y=ys)],
    #     "layout": Layout(title='Coin')
    # })

    #  plt.title('coin  classes')
    # plotly.offline.plot({
    #    "data": [Scatter(x=xs, y=ys)],
    #    "layout": Layout(title=coinNM)
    # })
    #plt.plot(xs, ys, label='bch')


    # plt.grid(alpha=0.4)
    # plt.yscale('log')
    plt.show()


if __name__ == '__main__':
     df = collections.OrderedDict()
     coinNames = common.getCoinName()
     for coinNm in coinNames:
         coinpath = 't/'+coinNm+'.csv'
         #conNm = str(coinNm)
         df[coinNm] = read_csv(coinpath)
     runchart(df)