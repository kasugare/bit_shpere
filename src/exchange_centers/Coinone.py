#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib.request
from urllib.request import Request, urlopen

URL = 'https://api.coinone.co.kr/ticker/?currency=all'

class Coinone:
	def __init__(self, logger):
		self._logger = logger

	def getTicker(self):
		urlTicker = urllib.request.urlopen(URL)
		readTicker = urlTicker.read().decode('utf8')
		jsonTicker = json.loads(readTicker)
		return jsonTicker

	def getBTC(self):
		jsonTicker = self.getTicker()
		findBTC = jsonTicker['btc']['last']
		BTC = int(findBTC)
		return BTC

	def getETH(self):
		jsonTicker = self.getTicker()
		findETH = jsonTicker['eth']['last']
		ETH = int(findETH)
		return ETH

	def getDASH(self):
		return None

	def getLTC(self):
		return None

	def getETC(self):
		jsonTicker = self.getTicker()
		findETC = jsonTicker['etc']['last']
		ETC = int(findETC)
		return ETC

	def getXRP(self):
		jsonTicker = self.getTicker()
		findXRP = jsonTicker['xrp']['last']
		XRP = int(findXRP)
		return XRP
