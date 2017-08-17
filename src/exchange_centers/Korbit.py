#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib.request
from urllib.request import Request, urlopen

URL = 'https://api.korbit.co.kr/v1/ticker?currency_pair='

class Korbit:
	def __init__(self, logger):
		self._logger = logger

	def _getCoinData(self, pairtype):
		url = '%s%s' %(URL, pairtype)
		reqCoin = Request(url , headers={'User-Agent': 'Mozilla/5.0'})
		readCoin = urlopen(reqCoin).read().decode('utf8')
		jsonCoin = json.loads(readCoin)
		findCoin = jsonCoin['last']
		coinInfo = int(findCoin)
		return coinInfo

	def getBTC(self):
		BTC = self._getCoinData(pairtype = 'btc_krw')
		return BTC

	def getETH(self):
		ETH = self._getCoinData(pairtype = 'eth_krw')
		return ETH

	def getETC(self):
		ETC = self._getCoinData(pairtype = 'etc_krw')
		return ETC

	def getXRP(self):
		XRP = self._getCoinData(pairtype = 'xrp_krw')
		return XRP

	def getDASH(self):
		return None

	def getLTC(self):
		return None