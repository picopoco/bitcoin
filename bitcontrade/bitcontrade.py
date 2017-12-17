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
    return jsonify({"resultMessage": "OK","resultCount": "0","totalCount": "0","resultCode":2000,'resultData': {}})

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

            if  args['timeStart']:
                _timeStart = str(args['timeStart'])
            if args['limit']:
                _limit = (args['limit'])
            if args['offset']:
                _offset = (args['offset'])

            print( _timeStart,_limit,_offset)
            cur = mysql.connect().cursor()
            sql = ("SELECT tid, traded_at, price, meme_type, volume,profit_amount,accumulate_amout,profit_rate"
                    +" FROM trades "
                    +" where  traded_at >= " + _timeStart
                   +" order by traded_at limit "+  _limit + " offset "+ _offset
                 )
            print(sql)
           # cur.execute("select traded_at,close from tickers  where traded_at >="+ _timeStart +  40 order by traded_at limit _limit +" offset "+ _offset
            cur.execute(sql)
            print("11")
            r = [dict((cur.description[i][0], value)
                      for i, value in enumerate(row)) for row in cur.fetchall()]
            return jsonify({"resultMessage": "OK","resultCount": r.__len__(),"totalCount": _limit,"resultCode":"200",'resultData': r})

        except Exception as e:
            return {'error': str(e)}

api.add_resource(trades, '/trades')


if __name__ == '__main__':
   app.run(host='0.0.0.0',debug=True)