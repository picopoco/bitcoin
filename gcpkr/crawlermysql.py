import threading
from urllib import request
import winsound
import json

def main():

print("### STARTING... ###")
checkCoin('https://min-api.cryptocompare.com/data/pricemulti?fsyms=STEEM&tsyms=BTC,USD,KRW')
def checkCoin(url):
threading.Timer(10, checkCoin, [url]).start()
data = request.urlopen(url).read(2000) # number of chars that should catch the announcement

print("########### http data ############")
#print(data)

json_data = json.loads(data)
print(json_data)
print(json_data["STEEM"]["KRW"])

krw = json_data["STEEM"]["KRW"]

if krw > 3000:
    print("▲▲▲")
    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
else:
    print("Nothing")
main()