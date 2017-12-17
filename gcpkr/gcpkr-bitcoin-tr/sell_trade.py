from selectTrade import tTrade

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
                            if  resT and resT['meme_type'] == 'b':
                                tPrice = resT['price']
                                t_accumulate_amount = resT['accumulate_amout']
                                print("###__", i, resT['meme_type'], ptrade.difPrice, ptrade.price, ptrade.trading_at)
                                isql = self.isqlSellTrade(ptrade,tPrice,t_accumulate_amount)
                                print('isqlSellTrade', isql)
                                return ptrade.cursor.execute(isql)

    @classmethod
    def isqlSellTrade(self,ptrade,tPrice,t_accumulate_amount):
        print("isqlSellTrade", ptrade.difPrice, ptrade.price, ptrade.trading_at)
        isql = (
            " INSERT INTO trades "
            + " (traded_at, price, meme_type, volume, profit_amount, accumulate_amout, profit_rate, created_at)"
            + "values("
            + ptrade.trading_at + "," + str(ptrade.price) + ", 's', " + str(
                ptrade._VOLUME) + " , 0+" + str(
                ptrade.difPrice * 1) + ",0, 0 / " + str(
                ptrade.difPrice) + "," + " sysdate() "
            + ")"
        )
        return isql