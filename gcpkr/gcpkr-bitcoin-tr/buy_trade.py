from selectTrade import tTrade
from common  import common
class buy():

    def __init__(self):
       # trade = trade
        pass

    @classmethod
    def trade(self,ptrade):
        result =''
        try:
            result =  self.tradeExec(ptrade)
        except Exception as e:
            print('buy trade error', e)
            return {'buy trade error': str(e)}
        return result

    @classmethod
    def tradeExec(self,ptrade):
        j = 0
        tPrice = 0
        t_accumulate_amoun = 0
        #ptrade =ptrade
        r = ptrade.r
        cursor = ptrade.cursor
        for i in range(0, len(r) - 4):
            #print(i, j, "1close", r[i]['close'], r[i + 1]['close'], r[i + 2]['close'], r[i + 3]['close'], r[i + 4]['close'])
            if float(r[i]['close']) < float(r[i + 1]['close']):
                if float(r[i + 1]['close']) < float(r[i + 2]['close']):
                    if float(r[i + 2]['close']) < float(r[i + 3]['close']):
                        if float(r[i + 3]['close']) < float(r[i + 4]['close']):
                            print(i, j, "close", r[i]['close'], r[i + 1]['close'], r[i + 2]['close'], r[i + 3]['close'],r[i + 4]['close'])
                            j += 1
                            #  try:
                            # INSERT
                            # with cur.cursor() as con:

                            ptrade.difPrice = r[i + 1]['close'] - r[i]['close']
                            ptrade.price = str(r[i]['close'])
                            ptrade.trading_at = str(r[i]['trading_at'])

                            resT = tTrade.select(ptrade)
                            common.buyStrage( resT, ptrade, i)
                            #ptrade.conn.commit()
                           # common.sellStrage( resT, ptrade, i)
                           # ptrade.conn.commit()

        return False


