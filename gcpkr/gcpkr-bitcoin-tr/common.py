

class common:
    trade =''

    def __init__(self):
        pass

    @classmethod
    def buyStrage(self, resT, ptrade, i):
        print("buyStrage", i,resT, ptrade)
        tPrice=0
        t_accumulate_amoun =0
        if resT:
            resT = resT[0]
            t_accumulate_amoun = resT['accumulate_amout']
            tPrice = resT['price']
            print("###__len", len(resT), i, resT['meme_type'], ptrade.difPrice, ptrade.price, ptrade.trading_at)
            #if resT['meme_type'] == 's':
            isql = self.isqlBuyTrade(ptrade, tPrice, t_accumulate_amoun)
            print('isqlBuyTrade', isql)
        else:
            isql = self.isqlBuyTrade(ptrade, tPrice, t_accumulate_amoun)


        return ptrade.cursor.execute(isql)

        # elif resT[0]['meme_type'] == 's':
        #     isql = self.isqlBuyTrade(ptrade, tPrice, t_accumulate_amoun)
        #     print('isqlBuyTrade', isql)
        #     return ptrade.cursor.execute(isql)

    @classmethod
    def sellStrage(self, resT, ptrade, i):
        print("sellStrage", i,resT, ptrade)

        if resT:
            resT = resT[0]
            if resT['meme_type'] == 'b':
                tPrice = resT['price']
                t_accumulate_amount = resT['accumulate_amout']
                print("###__", i, resT['meme_type'], ptrade.difPrice, ptrade.price, ptrade.trading_at)
                isql = self.isqlSellTrade(ptrade, tPrice, t_accumulate_amount)
                print('isqlSellTrade', isql)
                return ptrade.cursor.execute(isql)

    @classmethod
    def isqlSellTrade(self,ptrade,tPrice,t_accumulate_amount):
        profit_amount = float(ptrade.price) - tPrice
        accumulate_amout = profit_amount + t_accumulate_amount
        print("isqlSellTrade", tPrice, ptrade.price,profit_amount,ptrade.trading_at)
        isql = (
            " newcoinObj trades "
            + " (traded_at, price, meme_type, volume, profit_amount, accumulate_amout, profit_rate, created_at)"
            + "values("
            + ptrade.trading_at + "," + str(ptrade.price) + ", 's', " + str(ptrade._VOLUME) + " , 0+" + str(profit_amount) + ","+str(accumulate_amout)+", 0 / " + str( ptrade.difPrice) + "," + " sysdate() " + ")"
        )
        return isql

    @classmethod
    def isqlBuyTrade(self, ptrade, tPrice, t_accumulate_amoun):
        print("isqlBuyTrade", ptrade.difPrice, ptrade.price, ptrade.trading_at)
       # accumulate_amout = tPrice + int(t_accumulate_amoun)
        isql = (
            " newcoinObj trades "
            + " (traded_at, price, meme_type, volume, profit_amount, accumulate_amout, profit_rate, created_at)"
            #         + "values("+ ptrade.trading_at + "," + str(ptrade.price) + ", 'b', " + str(ptrade._VOLUME) + " , 0+" + str( ptrade.difPrice * 1) + ",0, 0 / " + str(ptrade.difPrice) + "," + " sysdate() "
            + "values(" + ptrade.trading_at + "," + str(ptrade.price) + ", 'b', " + str(ptrade._VOLUME) + " , 0+" + str(
                int(tPrice) + int(t_accumulate_amoun)) + ",0, 0 / " + str(ptrade.difPrice) + "," + " sysdate() "
            + ")"
        )
        return isql
