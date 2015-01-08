#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import json
import decimal

request = urllib2.Request('http://finance.yahoo.com/webservice/v1/symbols/FB/quote?format=json')

try: 
    stocks1_api = urllib2.urlopen(request)
    response = stocks1_api.read()
    response_dictionary = json.loads(response)
    # reads bit coin value from coinbase
    # Stock 1  Facebook
    # get the name
    symbol1_name = response_dictionary['list']['resources'][0]['resource']['fields']['name']
    # trim the weird stuff in the end - this one has a comma
    symbol1_name = symbol1_name.rpartition(',')
    symbol1_name = symbol1_name[0]

    # get the price
    symbol1_price = response_dictionary['list']['resources'][0]['resource']['fields']['price']
    # trim it to something sane
    symbol1_price = decimal.Decimal(symbol1_price)
    symbol1_price = round(symbol1_price,2)
    symbol1_price = str(symbol1_price)
    
    stck = symbol1_name + ' is trading at ' + symbol1_price + '.  '
    

    
except urllib2.HTTPError, e:
    stck = 'Failed to connect to Yahoo Finance.  '
except urllib2.URLError, e:
    stck = 'Failed to connect to Yahoo Finance.  '
except Exception:
    stck = 'Failed to connect to Yahoo Finance.  '

# print stck

request_2 = urllib2.Request('http://finance.yahoo.com/webservice/v1/symbols/POT.NZ/quote?format=json')

try: 
    stocks2_api = urllib2.urlopen(request_2)
    response_2 = stocks2_api.read()
    response_2_dictionary = json.loads(response_2)
    
    # get the name
    symbol2_name = response_2_dictionary['list']['resources'][0]['resource']['fields']['name']
    # trim the weird stuff in the end - this one has a bracket
    symbol2_name = symbol2_name.rpartition('(')
    symbol2_name = symbol2_name[0]

    # get the price
    symbol2_price = response_2_dictionary['list']['resources'][0]['resource']['fields']['price']
    # trim it to something sane
    symbol2_price = decimal.Decimal(symbol2_price)
    symbol2_price = round(symbol2_price,2)
    symbol2_price = str(symbol2_price)


    stck2 = ' and ' + symbol2_name + ' is trading at ' + symbol2_price + '.  '

except urllib2.HTTPError, e:
    stck2 = 'Failed to connect to Yahoo Finance.  '
except urllib2.URLError, e:
    stck2 = 'Failed to connect to Yahoo Finance.  '
except Exception:
    stck2 = 'Failed to connect to Yahoo Finance.  '

# print stck2

stck = stck + stck2

#print stck