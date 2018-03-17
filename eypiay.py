#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

Hive-Autoswitch
Ver. 2.0

Install curl:
apt-get install python-dev
pip install certifi
pip install logging
'''

import pycurl
import sys
import os
import datetime
import urllib
import urllib2
import hmac
import hashlib
import StringIO
import json
import certifi
from CONFIG import *
from time import sleep
import logging

LOG_FILENAME = '/home/user/hiveos/hive-autoswitch/autoswitch.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

argv = sys.argv
argc = len(sys.argv)
null = 0


class HiveAPI:

    def __init__(self):
        pass

    __SECRET_KEY = SECRET_KEY
    """
        Your secret API key, you sign the message with it
        @var string 64 hex chars
        """

    __PUBLIC_KEY = PUBLIC_KEY
    """
        This is a public key
        @var string 64 hex chars
        """

    __URL = "https://api.hiveos.farm/worker/eypiay.php"
    """
        Api connection URL
        Please use HTTPS, not HTTP for calls for better security.
        @var string
        """


    def run(self):
        self.__log("=== Hive API example ===")

        method = argv[1]

        if method != "multiRocket":
            # run this class methods by name
            m = getattr(self, method)
            result = m()
        else:
            if argc >= 4:
                # at least rig ids and miner required
                # take the arguments from commandline
                result = self.multiRocket(argv[2], argv[3], argv[4], argv[5], argv[6])
            else:
                # To use rocket you have to know what you are doing. Then delete these lines and edit the following.
                self.log("Please edit the source to use multiRocket method")
                exit()

                # this is just an example, use some of your real ids which you get with other methods

                # set everything to rigs ids 1, 2 and 3
                result = self.multiRocket("1,2,3", "claymore", "xmrig", 107800, 800)

                # set bminer to rigs ids 4 and 5, unset second miner
                # ??? result = self.multiRocket("4,5", "bminer", "0", null, null)

        if result is not None:
            # print_r($result);
            print json.dumps(result, indent=4)
            print

    def request(self, params):
        """
            Make API request with given params. Signs the request with secret key.
            @param: array params
            @return array
            """
                
        params["public_key"] = self.__PUBLIC_KEY
        post_data = urllib.urlencode(params)
        hmac_ = hmac.new(self.__SECRET_KEY, post_data, hashlib.sha256).hexdigest()

        try:
            curl = pycurl.Curl()
            curl.setopt(pycurl.CAINFO, certifi.where())
            curl.setopt(pycurl.URL, self.__URL)
            curl.setopt(pycurl.HTTPHEADER, ['HMAC: ' + str(hmac_)])
            curl.setopt(pycurl.POST, True)
            curl.setopt(pycurl.POSTFIELDS, post_data)
            curl.setopt(pycurl.CONNECTTIMEOUT, 10)
            curl.setopt(pycurl.TIMEOUT, 5)

            buf = StringIO.StringIO()
            curl.setopt(pycurl.WRITEFUNCTION, buf.write)
            curl.perform()

            response = buf.getvalue()

            # Uncomment to debug raw JSON response
            # self.__log("< " + response)

            http_code = curl.getinfo(pycurl.HTTP_CODE)

            curl.close()

        except pycurl.error:
            print "Oops!  That was no valid request..."
            response = "Something went wrong with the request"
            http_code = null
            
        if http_code != 200:
            result = {}
            self.__log("ERROR: HTTP " + str(http_code) + ":\n" + response)
        else:
            result = json.loads(response)
            if result is None:
                self.__log("ERROR: Unparsable JSON " + response)
            else:
                if 'error' in result:  # || !$result["result"]
                    self.__log("ERROR: " + json_encode(result["error"]))
                else:
                    result = result["result"]

        return result

    @staticmethod
    def __log(msg):        
        print "================================================"
        str_ = '\n[' + str(datetime.datetime.today()) + '] ' + msg
        print str_
        # with open(loggerFilename) as log_file:
        #     log_file.write(str_)

    def getRigs(self):
        """
        Rigs list
        """
        params = {
            'method': 'getRigs'
        }
        rigs = self.request(params)
        if 'error ' in rigs:
            return False

        return rigs

    def getWallets(self):
        """
        Wallets list
        """
        params = {
            'method': 'getWallets'
        }
        wallets = self.request(params)
        if 'error' in wallets:
            return False

        return wallets

    def getOC(self):
        """
        Overclocking profiles
        """
        params = {
            'method': 'getOC'
        }
        ocs = self.request(params)
        if 'error' in ocs:
            return False

        return ocs

    def getCurrentStats(self):
        """
        Monitor stats for all the rigs
        """
        params = {
            'method': 'getCurrentStats'
        }
        stats = self.request(params)
        if 'error' in stats:
            return False

        return stats

    def multiRocket(self, rig_ids_str, miner, miner2, id_wal, id_oc):
        """
        Sets parameters for rigs

        @param rig_ids_str coma separated string with rig ids "1,2,3,4"
        @param miner Miner to set. Leave it null if you do not want to change. "claymore", "claymore-z", "ewbf", ...
        @param miner2 Second miner to set. Leave it null if you do not want to change. "0" - if you want to unset it.
        @param id_wal ID of wallet. Leave it null if you do not want to change.
        @param id_oc ID of OC profile. Leave it null if you do not want to change.
        @return bool|mixed
        """
        
        if rig_ids_str is None:
            self.__log("Rigs ids required")
            exit()

        params = {
            'method': 'multiRocket',
            'rig_ids_str': rig_ids_str,
            'miner': miner,
            'miner2': miner2,
            'id_wal': id_wal,
            'id_oc': id_oc
        }

        result = self.request(params)
        if 'error' in result:
            return False

        return result



class WhatToMine:
    counter = 0
    retry_limit = 5
    most_profitable = {}
    most_profitable_keys = []
    
    def __init__(self):
        pass
    
    def __log(self, msg):
        str_ = '[' + str(datetime.datetime.today()) + '] ' + msg
        print str_
        # with open(loggerFilename) as log_file:
        #     log_file.write(str_)
        
    def getProfitableCoins(self):
        
        url_opener = urllib2.build_opener()
        url_opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
        try:
            response = url_opener.open(SOURCE["whattomine"]["url"])
            string = response.read().decode('utf-8')
            json_obj = json.loads(string)
        except:
            json_obj = {'coins': {}}
            print ("error")

        return json_obj["coins"]
    
    def calculateMostProfitable(self, profitable_coins):
        most_profitable = {}
        if len(profitable_coins["coins"]) > 0:
            for key, val in profitable_coins["coins"].items():

                if len(most_profitable) <= 0:
                    most_profitable[key] = val
                else:
                    if most_profitable[list(most_profitable.keys())[0]][SOURCE["whattomine"]["profitable_key"]] < val[SOURCE["whattomine"]["profitable_key"]]:
                        del most_profitable[list(most_profitable.keys())[0]]
                        most_profitable[key] = val
        return most_profitable

    def sortProfitableKey(self, profitable_coins):
        import operator
        profitable_sorted = {}
        if len(profitable_coins) > 0:
            for key, val in profitable_coins.items():
                profitable_sorted[key] = val[SOURCE["whattomine"]["profitable_key"]]

            x = sorted(profitable_sorted.items(), key=operator.itemgetter(1), reverse=True)    
                    
        return x
   
    def applyChanges(self):
        hive_api = HiveAPI()
        wallets = hive_api.getWallets()
        wallet_id = null
        coin_name = ""
        counter = 0
        result = None
        
        while counter < len(self.most_profitable_keys[0]):
            for key, val in wallets.items():           
                if self.most_profitable_keys[counter][0] == val["name"]:                
                    wallet_id = val["id_wal"]
                    coin_name = val["name"]
            counter += 1

        if wallet_id > 0:
            result = hive_api.multiRocket(SOURCE["whattomine"]["rig_ids"], null, null, wallet_id, null)            

            logging.debug('Process ID: ' + str(self.checkExistingProcess()))
            logging.debug('Date Time: ' + str(datetime.datetime.today()))
            logging.debug('Coin Switch: ' + coin_name )
            logging.debug('Rig IDs: ' + SOURCE["whattomine"]["rig_ids"])
            logging.debug('Wallet ID: ' + str(wallet_id))
                          
            print "Changes has been applied."
            print "Miner/s will now dig : " + coin_name
            print "Wallet ID : " + str(wallet_id)
            print "Rig ID/s : " + SOURCE["whattomine"]["rig_ids"]
            print "Restarting Miner."

            if result is None:
                return False
            else:
                return True
        else:
            return False
    def checkExistingProcess(self):
        return os.getpid()		
    
    def run(self):
        self.__log("\n=== Autoswitch Miner for Hiveos ===")
        self.most_profitable = self.getProfitableCoins()
        self.most_profitable_keys = self.sortProfitableKey(self.most_profitable)
        
        #print json.dumps(self.most_profitable_keys, indent = 4)
        result = self.applyChanges()
        while not result:            
            self.counter += 1
            if self.counter >= self.retry_limit:
                break
            sleep(5)
            self.run()
        
w = WhatToMine()
w.run()

