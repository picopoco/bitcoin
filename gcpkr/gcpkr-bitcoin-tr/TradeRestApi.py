from builtins import range

from flask import Flask, jsonify
from flaskext.mysql import MySQL
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'gitcoin'
app.config['MYSQL_DATABASE_PASSWORD'] = 'gitcoin'
app.config['MYSQL_DATABASE_DB'] = 'gitcoin'
app.config['MYSQL_DATABASE_HOST'] = '35.200.98.245'

mysql.init_app(app)
api = Api(app)

@app.route('/')
def index():
    return jsonify({"resultMessage": "OK", "resultCount": "0", "totalCount": "0", "resultCode": 2000, 'resultData': {}})

class trades(Resource):
    def get(self):
        try:
            # print("trades",self)
            parser = reqparse.RequestParser()
            parser.add_argument('timeStart', type=str)
            parser.add_argument('limit', type=str)
            parser.add_argument('offset', type=str)
            args = parser.parse_args()

            _timeStart = '20171106030001'
            _limit = 1000
            _offset = 0

            if args['timeStart']:
                _timeStart = (args['timeStart'])
            if args['limit']:
                _limit = (args['limit'])
            if args['offset']:
                _offset = (args['offset'])

            print(_timeStart, _limit, _offset)
            cur = mysql.connect().cursor()
            sql = (
            "SELECT tid, traded_at, price, meme_type, volume,profit_amount,accumulate_amout,profit_rate, created_at"
            + " FROM trades "
            + " where  traded_at >= " + str(_timeStart)
            + " order by traded_at limit " + str(_limit) + " offset " + str(_offset)
            )
            print(sql)
            # cur.execute("select traded_at,close from tickers  where traded_at >="+ _timeStart +  40 order by traded_at limit _limit +" offset "+ _offset
            cur.execute(sql)
            print("11")
            r = [dict((cur.description[i][0], value)
                      for i, value in enumerate(row)) for row in cur.fetchall()]
            return jsonify(
                {"resultMessage": "OK", "resultCount": r.__len__(), "totalCount": _limit, "resultCode": "200",
                 'resultData': r})

        except Exception as e:
            return {'error': str(e)}

api.add_resource(trades, '/trades')


class buy(Resource):
    _VOLUME = 1
    difPrice = 0
    price = 0
    trading_at = ''

    def get(self):
        try:
            print("trades",self)
            parser = reqparse.RequestParser()
            parser.add_argument('timeStart', type=str)
            parser.add_argument('limit', type=str)
            parser.add_argument('offset', type=str)
            args = parser.parse_args()

            _timeStart = '20171106030001'
            _limit = '1000'
            _offset = '0'

            if args['timeStart']:
                _timeStart = args['timeStart']
            if args['limit']:
                _limit = (args['limit'])
            if args['offset']:
                _offset = (args['offset'])

            print(_timeStart, _limit, _offset)
            conn = mysql.connect()
            cursor = conn.cursor()

            sql = (
            "SELECT trading_at, close"
            + " FROM predicts "
            + " where  trading_at >= " + _timeStart
            + " order by trading_at desc limit " + _limit + " offset " + _offset
            )
            print(sql)
            # cur.execute("select traded_at,close from tickers  where traded_at >="+ _timeStart +  40 order by traded_at limit _limit +" offset "+ _offset
            cursor.execute(sql)
            print("11")

            r = [dict((cursor.description[i][0], value)
                      for i, value in enumerate(row)) for row in cursor.fetchall()]
            print (len(r),r[0])
            j =  0
            for  i in range(0,len(r)-4):
                  if float(r[i]['close']) < float(r[i+1]['close'] ):
                     if float(r[i+1]['close']) < float(r[i+2]['close']):
                         if float(r[i + 2]['close']) < float(r[i + 3]['close']):
                             if float(r[i + 3]['close']) < float(r[i + 4]['close']):
                               print (i,j,"close",r[i]['close'] ,r[i+1]['close'],r[i+2]['close'],r[i+3]['close'],r[i+4]['close'])
                               j += 1
                             #  try:
                                   # INSERT
                                  # with cur.cursor() as con:

                               self.difPrice = r[i + 1]['close'] - r[i]['close']
                               self.price  = str(r[i]['close'])
                               self.trading_at =  str(r[i]['trading_at'])
                               print("__", i,self.difPrice,self.price,self.trading_at)

                               # isql = (
                               #     " newcoinObj trades "
                               #     + " (traded_at, price, meme_type, volume, profit_amount, accumulate_amout, profit_rate, created_at)"
                               #     + "values("
                               #     + trading_at + "," + str(price) + ", 'b', " + str(
                               #         self._VOLUME) + " , 0+" + str(
                               #         difPrice * 1) + ",0, 0 / " + str(
                               #         difPrice) + "," + " sysdate() "
                               #     + ")"
                               # )
                               isql = self.iSqltBuyTrade()
                               print (isql)
                               cursor.execute(isql)
            conn.commit()
            conn.close()
                #print(i,"trading_at", r[i]['trading_at'], r[i+1]['trading_at'], r[i+2]['trading_at'])

            return jsonify(
                {"resultMessage": "OK", "resultCount": r.__len__(), "totalCount": _limit, "resultCode": "200",
                 'resultData': r})

        except Exception as e:
            return {'error': str(e)}

    @classmethod
    def iSqltBuyTrade(self):
        print("self", self.difPrice, self.price, self.trading_at)

        isql = (
            " newcoinObj trades "
            + " (traded_at, price, meme_type, volume, profit_amount, accumulate_amout, profit_rate, created_at)"
            + "values("
            + self.trading_at + "," + str(self.price) + ", 'b', " + str(
                self._VOLUME) + " , 0+" + str(
                self.difPrice * 1) + ",0, 0 / " + str(
                self.difPrice) + "," + " sysdate() "
            + ")"
        )
        return isql
api.add_resource(buy, '/buy')



if __name__ == '__main__':
   app.run(debug=True)
   #app.run(host='0.0.0.0',debug=True)