from Utils import csv,map
from Row import Row
from Cols import Cols
class Data:
	def __init__(self,src={}):
		self.rows = list()
		self.cols = None
		if type(src) == str:
			csv(src,self.add)
		else:
			map(src,self.add)

	def add(self,t):
		if not self.cols:
			self.cols = Cols(t)
		else:
			if type(t) == list:
				t = Row(t)
				self.cols.add(t)
				self.rows.append(t)

	




