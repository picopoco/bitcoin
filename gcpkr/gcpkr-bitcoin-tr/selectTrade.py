class tTrade():

    def __init__(self,trade):
        trade = trade
        pass

    @classmethod
    def select(self,ptrade):
        cursor = ptrade.cursor
        sSqlTrade = (
            " select"
            + " traded_at, investment, price, meme_type, 1, profit_amount, accumulate_amout"
            + " from trades  where"
            + " traded_at <= "+ ptrade.trading_at
            + " order by traded_at desc limit 1"
        )
        print('select',sSqlTrade)
        cursor.execute(sSqlTrade)
        t = [dict((cursor.description[i][0], value)
                  for i, value in enumerate(row)) for row in cursor.fetchall()]

        if len(t)>0:
            print('t: ', len(t) ,type(t),t)

        return t

