import time
import os.path
import io
import urllib
import json
import csv
import datetime
from time import localtime

now = datetime.datetime.now().strftime("%Y%m%d%H") # current day
file_exists = os.path.isfile(now+'.csv') # file_name exists check

with open(now+'.csv', 'a') as f:
        fieldnames = ['timestamp', 'open', 'high', 'low', 'close'] # column name
        writer = csv.DictWriter(f, fieldnames = fieldnames, delimiter = ',', lineterminator='\n')
        if not file_exists: # file doesn't exists, write header and data if the file already exists,(header exists) do not write again
                writer.writeheader()

        url = 'https://api.bithumb.com/public/ticker/BTC' # api url

        request_url = url

        u = urllib.urlopen(request_url)
        data = u.read()

        j = json.loads(data) # data fetch

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S") # current timestamp
        open_p = j['data']['opening_price']
        high_p = j['data']['max_price']
        low_p = j['data']['min_price']
        closed_p = j['data']['closing_price']

        writer.writerow({'timestamp' : timestamp, 'open' : open_p, 'high' : high_p, 'low' : low_p, 'close' : closed_p}) # write data (append)

#EXPORT204 = "gsutil -m cp /home/Tora/code"+now+".csv gs://gcpkr-bitcoin-keras/preprocess" # copy the file to gcs bucket
EXPORT204 = "gsutil -m cp /home/Tora/code/"+now+".csv gs://test_bucket0125" # copy the file to gcs bucket
EXPORT205 = "mv "+now+".csv 201712_csv"

os.system(EXPORT204)  # execute EXPORT204
os.system(EXPORT205)
