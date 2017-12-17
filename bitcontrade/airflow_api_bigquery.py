import time
import os.path
import io
import urllib
import json
import csv
import datetime
from time import localtime
from pprint import pprint
#from google.cloud import bigquery
def main():
    timestamp = datetime.datetime.now()

    url = 'https://api.bithumb.com/public/ticker/BTC'  # api url
    request_url = url

    u = urllib.urlopen(request_url)
    data = u.read()
    j = json.loads(data)

    open_p = j['data']['opening_price']
    high_p = j['data']['max_price']
    low_p = j['data']['min_price']
    closed_p = j['data']['closing_price']

    #stream_data("test_de", "preprocess", timestamp, open_p, high_p, low_p, closed_p)


def stream_data(dataset_id, table_id, time_stamp, open_p, high_p, low_p, closed_p):
    bigquery_client = bigquery.Client()
    dataset_ref = bigquery_client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    # Get the table from the API so that the schema is available.
    table = bigquery_client.get_table(table_ref)

    rows = [{'traded_at': time_stamp.strftime("%Y%m%d%H%M%S"), 'open': open_p, 'high': high_p, 'low': low_p,
             'close': closed_p}]
    errors = bigquery_client.create_rows(table, rows)

    if not errors:
        print('Loaded 1 row into {}:{}'.format(dataset_id, table_id))
    else:
        print('Errors:')
        pprint(errors)


main()