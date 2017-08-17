#!/usr/bin/env python
# -*- coding: utf-8 -*-

from common.util_logger import Logger
from exchange_centers.Bithumb import Bithumb
from exchange_centers.Coinone import Coinone
from exchange_centers.Korbit import Korbit

import time
DEFAULT_KEYS = ['sell_price', 'buy_price', 'average_price', 'closing_price', 'opening_price', 'units_traded', 'min_price', 'max_price', 'volume_1day', 'volume_7day']

VKey1 = ['sell_price', 'buy_price', 'closing_price']
VKey2 = ['average_price', 'opening_price', 'units_traded', 'min_price', 'max_price', 'volume_1day', 'volume_7day']
SPEACIAL_KEYS = ['sell_price', 'buy_price', 'closing_price', 'average_price']

class BitShpere:
	def __init__(self):
		self._logger = Logger('BitSphere_System').getLogger()
		self._clogger = Logger('BitSphere_Coin').getLogger()
		self._coinInfoRepository = {}
		self._continuousLevel = {}

	def doProcess(self):
		bithumb = Bithumb(self._logger, self._clogger)
		coinone = Coinone(self._logger)
		korbit = Korbit(self._logger)

		currCoinInfo = bithumb.getBTCAll()
		prevCoinInfo = self._getPrevCoinInfo(currCoinInfo)
		diffCoinInfo = self._calDiffCoinInfo(prevCoinInfo, currCoinInfo)
		continuousLevel = self._calContinuousLevel(diffCoinInfo)

		self._saveCurrCoinInfo(currCoinInfo)
		self.showCoinInfo(currCoinInfo, prevCoinInfo, diffCoinInfo, continuousLevel)

	def _saveCurrCoinInfo(self, currCoinInfo):
		currTS = currCoinInfo['timestamp']
		self._coinInfoRepository[currTS] = currCoinInfo

		if len(self._coinInfoRepository) >= 10:
			TSs = list(self._coinInfoRepository.keys())
			TSs.sort()
			self._coinInfoRepository.pop(TSs[0])


	def _getPrevCoinInfo(self, currCoinInfo):
		if self._coinInfoRepository:
			tsKeys = list(self._coinInfoRepository.keys())
			tsKeys.sort()
			prevTS = tsKeys[-1]
			prevCoinInfo = self._coinInfoRepository[prevTS]
		else:
			return currCoinInfo

		return prevCoinInfo

	def _calDiffCoinInfo(self, prevCoinInfo, currCoinInfo):
		diffCoinInfo = {}
		for key in DEFAULT_KEYS:
			diffValue = float(currCoinInfo[key]) - float(prevCoinInfo[key])
			diffCoinInfo[key] = diffValue
		return diffCoinInfo

	def _calContinuousLevel(self, diffCoinInfo):
		for key in DEFAULT_KEYS:
			diffValue = diffCoinInfo[key]
			if key not in self._continuousLevel:
				self._continuousLevel[key] = 0

			cLevel = self._continuousLevel[key]

			if diffValue >= 0 and cLevel >= 0:
				self._continuousLevel[key] += 1
			else:
				self._continuousLevel[key] = 0
		return self._continuousLevel

	def showCoinInfo(self, prevCoinInfo, currCoinInfo, diffCoinInfo, continuousLevel):
		self._clogger.info("       status name      |       prev info      |     current info     |     difference   |  count ")
		self._clogger.info('-' * 100)

		for key in VKey1:
			diffValue = diffCoinInfo[key]
			keyName = ' '.join(key.split('_'))

			prevValue = prevCoinInfo[key]
			currValue = currCoinInfo[key]
			cLevel = continuousLevel[key]

			sk = ' '
			if key in SPEACIAL_KEYS:
				sk = '*'

			coinValues = '%s | %s | %s | %s' %(format(prevValue, ',').rjust(20), format(currValue, ',').rjust(20), format(diffValue, ',').rjust(16), format(cLevel, ',').rjust(4))
			if diffValue > 0 :
				self._clogger.debug(" %s %s : %s" %(sk, keyName.ljust(20), coinValues))
			elif diffValue < 0 :
				self._clogger.error(" %s %s : %s" %(sk, keyName.ljust(20), coinValues))
			else:
				self._clogger.info(" %s %s : %s" %(sk, keyName.ljust(20), coinValues))
		print('')

if __name__ == '__main__':
	shpere = BitShpere()
	while True:
		shpere.doProcess()
		time.sleep(1)
