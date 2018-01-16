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
import common ,time
import unicodecsv as csv

#define data location
from datetime import datetime

import itertools
def reversed_enumerate(sequence):
    return itertools.izip(
        reversed(range(len(sequence))),
        reversed(sequence),
    )

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
    chart_idx = 1
    print('len',len(coinObj))
    # coinList = []
    # coinNmList = []

    for coinNM  in coinObj:
        # coninList = coinObj[coinNM]
        print (coinObj[coinNM])
        xs = coinObj[coinNM]['date']
        xst = pd.to_datetime(xs)
        ys = coinObj[coinNM]['price']

        coinObjlen = len(coinObj)

        #chart create
        subnum =  coinObjlen *100 +10 + chart_idx
        plt.subplot(subnum)
        plt.ylabel(coinNM)
        plt.xlabel('Exposure Time')
        plt.plot(xst, ys ,label=coinNM)

        plt.grid(True)
        plt.legend(loc='best', title=coinNM)
        chart_idx += 1

        meme_buy_count = 1;
        meme_sell_count = 1;
        memelist = []
        for idx, val in enumerate(ys):
            print (idx, val ,ys[idx])
            mobj = collections.OrderedDict()
            mobj['date'] =''
            mobj['price'] =''
            mobj['buy_volume'] = 0
            mobj['sell_volume'] = 0
            mobj['sum_buy'] = 0
            mobj['sum_sell'] = 0
            mobj['sum_volume'] = 0

            if idx < len(ys) - 3:
                # buy
                if ys[idx] > ys[idx + 1]:
                    if ys[idx + 1] > ys[idx + 2]:
                        if ys[idx + 2] > ys[idx + 3]:
                           # if not memelist or memelist[-1]['sell_volume'] ==1:
                              # print('b', meme_buy_count, str(idx - 1) + '>' + str(idx), ys[idx])
                                meme_buy_count += 1
                                plt.scatter(xst[idx], ys[idx], color='g', marker='^')
                                mobj['buy_volume'] = 1
                                mobj['sum_buy'] = ys[idx] * mobj['buy_volume']
         #               memelist.append(mobj)
                        #     coinObj[coinNM][idx]['buy'] = 1
                        # else:
                        #     coinObj[coinNM][idx]['buy'] = 0
                # sell
                if ys[idx] < ys[idx + 1]:
                    if ys[idx + 1] < ys[idx + 2]:
                        if ys[idx + 2] < ys[idx + 3]:
                         #   if memelist[-1]['buy_volume'] ==1:
                                print('s', meme_sell_count, str(idx - 1) + '>' + str(idx), ys[idx])
                                meme_sell_count += 1
                                plt.scatter(xst[idx], ys[idx], color='r', marker='v')
                                mobj['sell_volume'] = 1
                                if memelist:
                                    mobj['sum_sell'] = ys[idx] * mobj['sell_volume']


            mobj['date'] = xs[idx]
            mobj['price'] = ys[idx]
            if memelist :
               mobj['sum_volume']  =  memelist[-1]['sell_volume']+mobj['buy_volume']- mobj['sell_volume']
               #mobj['sell_volume']  =  memelist[-1]['sell_volume']+mobj['sell_volume']
               #mobj['buy_volume']  =  memelist[-1]['buy_volume']+ mobj['buy_volume']


            memelist.append(mobj)

        print(memelist[:100])
        keys = memelist[0].keys()
        with open('t/'+coinNM+'_trade.csv', 'wb') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(memelist)
    plt.xticks(rotation=90)
    plt.show()


if __name__ == '__main__':
     df = collections.OrderedDict()
     coinNames = common.getCoinName()
     for coinNm in coinNames:
         coinpath = 't/'+coinNm+'.csv'
         #conNm = str(coinNm)
         df[coinNm] = read_csv(coinpath)
     runchart(df)