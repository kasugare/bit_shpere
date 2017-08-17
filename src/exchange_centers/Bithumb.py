#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib.request
from urllib.request import Request, urlopen
import codecs
import time

URL = 'https://api.bithumb.com/public/ticker/all'

class Bithumb:
	def __init__(self, logger, clogger):
		self._logger = logger
		self._clogger = clogger

	def getTicker(self):
		urlTicker = urllib.request.urlopen(URL)
		readTicker = urlTicker.read().decode('utf8')
		jsonTicker = json.loads(readTicker)
		return jsonTicker

	def getBTC(self):
		jsonTicker = self.getTicker()
		findBTC = jsonTicker['data']['BTC']['closing_price']
		BTC = int(findBTC)
		return BTC

	def getBTCAll(self):
		jsonTicker = self.getTicker()
		timestamp = jsonTicker['data']['date']
		findBTC = jsonTicker['data']['BTC']

		findBTC['timestamp'] = int(timestamp)
		findBTC['sell_price'] = float(findBTC['sell_price'])
		findBTC['buy_price'] = float(findBTC['buy_price'])
		findBTC['units_traded'] = float(findBTC['units_traded'])
		findBTC['min_price'] = float(findBTC['min_price'])
		findBTC['max_price'] = float(findBTC['max_price'])
		findBTC['average_price'] = float(findBTC['average_price'])
		findBTC['opening_price'] = float(findBTC['opening_price'])
		findBTC['closing_price'] = float(findBTC['closing_price'])
		findBTC['volume_1day'] = float(findBTC['volume_1day'])
		findBTC['volume_7day'] = float(findBTC['volume_7day'])
		return findBTC

	def getETH(self):
		jsonTicker = self.getTicker()
		findETH = jsonTicker['data']['ETH']['closing_price']
		ETH = int(findETH)
		return ETH

	def getDASH(self):
		jsonTicker = self.getTicker()
		findDASH = jsonTicker['data']['DASH']['closing_price']
		DASH = int(findDASH)
		return DASH

	def getLTC(self):
		jsonTicker = self.getTicker()
		findLTC = jsonTicker['data']['LTC']['closing_price']
		LTC = int(findLTC)
		return LTC

	def getETC(self):
		jsonTicker = self.getTicker()
		findETC = jsonTicker['data']['ETC']['closing_price']
		ETC = int(findETC)
		return ETC

	def getXRP(self):
		jsonTicker = self.getTicker()
		findXRP = jsonTicker['data']['XRP']['closing_price']
		XRP = int(findXRP)
		return XRP
