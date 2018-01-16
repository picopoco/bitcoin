import requests as rq
import time
from retrying import retry
import os
import common

SECONDS_CONVERT_RATE = 1000  # s <-> ms 변환시 사용

STOP_MAX_ATTEMPT_NUMBER = 7  # 에러 발생시 몇 번까지 시도할 지
WAIT_RANDOM_MIN = 10000      # 에러 발생시 몇초 기다릴지 최소값
WAIT_RANDOM_MAX = 20000      # 에러 발생시 몇초 기다릴지 최대값


def get_day_micro_seconds(delta=1):
    sec_of_minute = 60
    sec_of_hour = sec_of_minute * 60
    sec_of_day = sec_of_hour * 24
    return (sec_of_day * SECONDS_CONVERT_RATE) * delta


def get_today_micro_seconds():
    return int(time.time() * SECONDS_CONVERT_RATE)


@retry(stop_max_attempt_number=STOP_MAX_ATTEMPT_NUMBER, wait_random_min=WAIT_RANDOM_MIN, wait_random_max=WAIT_RANDOM_MAX)
def get_history(sdate, edate, coin):

    url = 'http://index.bithumb.com/api/coinmarketcap/localAPI.php'
    #url = 'https://api.bithumb.com/public/ticker/BTC'  # api url

    res = rq.get(url, params={
        'api': 'graph',
        'coin': coin,
        'subject': 'price_usd',
        'start': sdate,
        'end': edate
    })

    return res.json()


def save(dataset, coin):
   # dataset.reverse()
    SAVE_DIRECTORY = 't'
    FILE_NAME = '%s.csv'%(coin)
    FILE_PATH = os.path.join(SAVE_DIRECTORY, FILE_NAME)

    if not os.path.isdir(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)

    if not os.path.isfile(FILE_PATH):
        with open(FILE_PATH, 'w') as f:
            f.write('date,price\n')

    with open(FILE_PATH, 'a+') as f:
        for datapacket in dataset:
            date = time.ctime(datapacket[0]/SECONDS_CONVERT_RATE)
            price = str(datapacket[1])
            f.write('%s,%s\n'%(date, price))

def save(dataset, coin):
   # dataset.reverse()
    SAVE_DIRECTORY = 't'
    FILE_NAME = '%s.csv'%(coin)
    FILE_PATH = os.path.join(SAVE_DIRECTORY, FILE_NAME)

    if not os.path.isdir(SAVE_DIRECTORY):
        os.makedirs(SAVE_DIRECTORY)

    if not os.path.isfile(FILE_PATH):
        with open(FILE_PATH, 'w') as f:
            f.write('date,price\n')

    with open(FILE_PATH, 'a+') as f:
        for datapacket in dataset:
            date = time.ctime(datapacket[0]/SECONDS_CONVERT_RATE)
            price = str(datapacket[1])
            f.write('%s,%s\n'%(date, price))



def run(coin):
    edate = get_today_micro_seconds()
    sdate = edate - get_day_micro_seconds()

    is_continue = True

    count = 0

    while is_continue and count <2:

        history = get_history(sdate, edate, coin)
        history_length = len(history)
        print('history_length',history_length)

        if not history_length:
            is_continue = False
        else:
            count +=1
            history.reverse()

            first_history = history[0]  # 첫 번째 데이터
            last_history = history[history_length - 1]  # 마지막 데이터터

            print(time.ctime(first_history[0] / SECONDS_CONVERT_RATE))
            print(time.ctime(last_history[0] / SECONDS_CONVERT_RATE))

            save(history, coin)

            print('===================')
            edate = sdate
            sdate = edate - get_day_micro_seconds()


if __name__ == '__main__':


    for coin in common.getCoinName():
     run(coin)