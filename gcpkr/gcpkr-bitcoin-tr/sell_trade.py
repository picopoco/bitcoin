from selectTrade import tTrade
from common import common
class sell:

    @classmethod
    def __init__(self):
     pass

    @classmethod
    def trade(self,ptrade):
        result = ''
        try:
            result = self.tradeExec(ptrade)
        except Exception as e:
            print('sell trade error' ,e)
            return {'sell trade error': str(e)}
        return result

    @classmethod
    def tradeExec(self,ptrade):
        r = ptrade.r
        j = 0
        for i in range(0, len(r) - 4):
           # print(i, j, "1close", r[i]['close'], r[i + 1]['close'], r[i + 2]['close'], r[i + 3]['close'],r[i + 4]['close'])
            if float(r[i]['close']) > float(r[i + 1]['close']):
                if float(r[i + 1]['close']) > float(r[i + 2]['close']):
                    if float(r[i + 2]['close']) > float(r[i + 3]['close']):
                        if float(r[i + 3]['close']) > float(r[i + 4]['close']):
                           # print(i, j, "close", r[i]['close'], r[i + 1]['close'], r[i + 2]['close'], r[i + 3]['close'],r[i + 4]['close'])
                            j += 1
                            ptrade.difPrice = r[i + 1]['close'] - r[i]['close']
                            ptrade.price = str(r[i]['close'])
                            ptrade.trading_at = str(r[i]['trading_at'])

                            resT = tTrade.select(ptrade)
                            common.sellStrage(resT, ptrade, i)
                            #common.buyStrage(resT, ptrade, i)

