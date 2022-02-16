import urllib.request,json
import requests


def fetch_quotes():
    url='http://quotes.stormconsultancy.co.uk/random.json'.format()
    response=requests.get(url).json()
    return response