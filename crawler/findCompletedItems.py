
import os
import sys
from optparse import OptionParser

sys.path.insert(0, '%s/../' % os.path.dirname(__file__))

from common import dump

import ebaysdk
from ebaysdk.finding import Connection as finding
from ebaysdk.exception import ConnectionError

def init_options():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)

    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug", default=False,
                      help="Enabled debugging [default: %default]")
    parser.add_option("-y", "--yaml",
                      dest="yaml", default='ebay.yaml',
                      help="Specifies the name of the YAML defaults file. [default: %default]")
    parser.add_option("-a", "--appid",
                      dest="appid", default=None,
                      help="Specifies the eBay application id to use.")

    (opts, args) = parser.parse_args()
    return opts, args


def run(opts):

    try:
        api = finding(debug=opts.debug, appid=opts.appid,
                      config_file=opts.yaml, warnings=True)

        api_request = {
             'keywords': 'book',
             'itemFilter': [
#                 {'name': 'Condition',
#                  'value': 'Used'},
#                 {'name': 'LocatedIn',
#                  'value': 'US'},
                 {'name': 'SoldItemsOnly',
                  'value': 'true'},
                 {'name': 'MaxPrice',
#                  'paramName': 'Currency',
#                  'paramvalue': 'USD',
                  'value': '2000'},
                 {'name': 'MinPrice',
                  #'paramName': 'Currency',
                  #'paramvalue': 'USD',
                  'value': '100'}
             ]
        }

        response = api.execute('findCompletedItems', api_request)

        dump(api)
    except ConnectionError as e:
        print(e)
        print(e.response.dict())

if __name__ == "__main__":
    print("Finding samples for SDK version %s" % ebaysdk.get_version())
    (opts, args) = init_options()
    run(opts)

#Category: Books
#Keywords: Books, Old Books
#Item Filters:
#Condition: Used, New __Yes__
#Price: 50-400 (Max price, Min Price)
#Show Only: Sold Listings (findCompletedItems)
#Item Location: North America, US Only (LocatedIn)
