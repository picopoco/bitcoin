from selectTrade import tTrade

class buy():

    def __init__(self,trade):
        trade = trade
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
        #ptrade =ptrade
        r = ptrade.r
        cursor = ptrade.cursor
        for i in range(0, len(r) - 4):
            #print(i, j, "1close", r[i]['close'], r[i + 1]['close'], r[i + 2]['close'], r[i + 3]['close'], r[i + 4]['close'])
            if float(r[i]['close']) < float(r[i + 1]['close']):
                if float(r[i + 1]['close']) < float(r[i + 2]['close']):
                    if float(r[i + 2]['close']) < float(r[i + 3]['close']):
                        if float(r[i + 3]['close']) < float(r[i + 4]['close']):
                            #print(i, j, "close", r[i]['close'], r[i + 1]['close'], r[i + 2]['close'], r[i + 3]['close'],r[i + 4]['close'])
                            j += 1
                            #  try:
                            # INSERT
                            # with cur.cursor() as con:

                            ptrade.difPrice = r[i + 1]['close'] - r[i]['close']
                            ptrade.price = str(r[i]['close'])
                            ptrade.trading_at = str(r[i]['trading_at'])

                            resT = tTrade.select(ptrade)
                            if resT :
                                t_accumulate_amoun = resT['accumulate_amout']
                                tPrice = resT['price']
                                print("###__", i, resT['meme_type'], ptrade.difPrice, ptrade.price, ptrade.trading_at)

                            if not resT or resT['meme_type'] == 's':
                                isql = self.isqlBuyTrade(ptrade, tPrice, t_accumulate_amoun)
                                print('isqlBuyTrade',isql)
                                return ptrade.cursor.execute(isql)
        return False

    @classmethod
    def isqlBuyTrade(self,ptrade,tPrice, t_accumulate_amoun):
        print("isqlBuyTrade", ptrade.difPrice, ptrade.price, ptrade.trading_at)
        isql = (
            " INSERT INTO trades "
            + " (traded_at, price, meme_type, volume, profit_amount, accumulate_amout, profit_rate, created_at)"
   #         + "values("+ ptrade.trading_at + "," + str(ptrade.price) + ", 'b', " + str(ptrade._VOLUME) + " , 0+" + str( ptrade.difPrice * 1) + ",0, 0 / " + str(ptrade.difPrice) + "," + " sysdate() "
            + "values(" + ptrade.trading_at + "," + str(ptrade.price) + ", 'b', " + str(ptrade._VOLUME) + " , 0+" + str(ptrade.difPrice * 1) + ",0, 0 / " + str(ptrade.difPrice) + "," + " sysdate() "
            + ")"
        )
        return isql
