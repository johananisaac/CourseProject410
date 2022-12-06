from DocLength import *

class InvertedIndex:

	def __init__(self):
		self.index = dict()

	def __contains__(self, item):
		return item in self.index

	def __getitem__(self, item):
		return self.index[item]

	def addWordByID(self, word, docid):
		if word in self.index:
			if docid in self.index[word]:
				self.index[word][docid] += 1
			else:
				self.index[word][docid] = 1
		else:
			document = dict()
			document[docid] = 1
			self.index[word] = document
    

