from builtins import range
from flask import Flask, jsonify
from flaskext.mysql import MySQL
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import pymysql
#from matplotlitb import pyplot as plt
import matplotlib.pyplot as plt



from sell_trade import sell
from buy_trade  import buy



app = Flask(__name__)
with app.app_context():
    # within this block, current_app points to app.
    print(app.name)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'gitcoin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'gitcoin'
app.config['MYSQL_DATABASE_DB'] = 'gitcoin'
app.config['MYSQL_DATABASE_HOST'] = '35.200.98.245'
mysql.init_app(app)

def getConnection():
    return pymysql.connect(host='35.200.98.245', user='gitcoin', password='gitcoin',
                           db='gitcoin', charset='utf8')

class bitcoinTr():
    _VOLUME = 1
    difPrice = 0
    price = 0
    trading_at = ''
    conn = ''
    cursor = ''
    r =[]
    @classmethod
    def trade(self):
        try:
            print("trades",self)

            _timeStart = '20161106030001'
            _limit = '1000'
            _offset = '100'

            print(_timeStart, _limit, _offset)
            conn = mysql.connect()
            cursor = conn.cursor()

            # sql = (
            # "SELECT trading_at, close"
            # + " FROM predicts "
            # + " where  trading_at >= " + _timeStart
            # + " order by trading_at desc limit " + _limit + " offset " + _offset
            # )

            sql = (
                "SELECT traded_at, close"
                + " FROM tickers "
                + " where  traded_at >= " + _timeStart
                + " order by traded_at desc limit " + _limit + " offset " + _offset
            )

            print(sql)
            cursor.execute(sql)
            print("11")

            r = [dict((cursor.description[i][0], value)
                      for i, value in enumerate(row)) for row in cursor.fetchall()]
            print ('  r = r',len(r),r[0])
            x = [ x['traded_at'] for x in r ]
            y = [ x['close'] for x in r ]

            plt.plot(x, y)
            plt.ylabel('tickers close')
            plt.show()

            self.r = r
            self.conn = conn
            self.cursor = cursor
            # plt.plot([1, 2, 3, 4])
            # plt.ylabel('some numbers')
            # plt.show()
           #buy().trade(self)
           # sell().trade(self)
           # conn.commit()
           # conn.close()
                #print(i,"trading_at", r[i]['trading_at'], r[i+1]['trading_at'], r[i+2]['trading_at'])

            return jsonify(
                {"resultMessage": "OK", "resultCount": r.__len__(), "totalCount": _limit, "resultCode": "200",
                 'resultData': r})

        except Exception as e:
            print (e)
            return {'error': str(e)}


if __name__ == '__main__':
  print(bitcoinTr.trade())
   #app.run(host='0.0.0.0',debug=True)