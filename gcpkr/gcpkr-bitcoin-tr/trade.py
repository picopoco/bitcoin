from builtins import range
from flask import Flask, jsonify
from flaskext.mysql import MySQL
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import pymysql

from sell_trade import sell
from buy_trade  import buy
from matplotlitb import pyplot as plt

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

class trade():
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
            plt.plot([1, 2, 3, 4])
            plt.ylabel('some numbers')
            plt.show()

            _timeStart = '20161106030001'
            _limit = '100000'
            _offset = '0'

            print(_timeStart, _limit, _offset)
            conn = mysql.connect()
            cursor = conn.cursor()

            sSqlpredict = (
            "SELECT trading_at, close"
            + " FROM predicts "
            + " where  trading_at >= " + _timeStart
            + " order by trading_at desc limit " + _limit + " offset " + _offset
            )
            #print(sSqlpredict)
            cursor.execute(sSqlpredict)


            sRes = [dict((cursor.description[i][0], value)
                      for i, value in enumerate(row)) for row in cursor.fetchall()]


            #전역변수에 저장
            self.r = sRes
            self.conn = conn
            self.cursor = cursor

          #  for sr ,in sRes:
          #  buy.trade(self)
           # sell.trade(self)
            conn.commit()
            conn.close()
                #print(i,"trading_at", r[i]['trading_at'], r[i+1]['trading_at'], r[i+2]['trading_at'])

            return jsonify(
                {"resultMessage": "OK", "resultCount": sRes.__len__(), "totalCount": _limit, "resultCode": "200",
                 'resultData': sRes})


        except Exception as e:
            print (e)
            return {'error': str(e)}


if __name__ == '__main__':
  print(trade.trade())
   #app.run(host='0.0.0.0',debug=True)