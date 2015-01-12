#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json

request = urllib2.Request('https://coinbase.com/api/v1/prices/buy')

try: 
    coinbase_api = urllib2.urlopen(request)
    response = coinbase_api.read()
    response_dictionary = json.loads(response)
    # reads bit coin value from coinbase
    btc = 'The value of 1 bitcoin is: ' + str(response_dictionary['subtotal']['amount']) + '.  '
except urllib2.HTTPError, e:
    btc = 'Failed to connect to coinbase.  '
except urllib2.URLError, e:
    btc = 'Failed to connect to coinbase.  '
except Exception:
    btc = 'Failed to connect to coinbase.  '

#print response_dictionary['amount']
#print response_dictionary['subtotal']['amount']

print btc
