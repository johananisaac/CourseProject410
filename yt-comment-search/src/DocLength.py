class DocLength:

	def __init__(self):
		self.info = dict()

	def __len__(self):
		return len(self.info)

	def add(self, docID, length):
		self.info[docID] = length

	def getLength(self, docID):
		if docID in self.info:
			result = self.info[docID]
			return result

	def getAverageLength(self):
		counter = 0
		for length in self.info.values():
			counter += length
		result = float(counter) / float(len(self.info))
		return result

