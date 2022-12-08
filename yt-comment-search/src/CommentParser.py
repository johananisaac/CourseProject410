import re
import json
import string

class CommentParser:

	def __init__(self, comments):
		self.comments = comments
		self.comment = dict()
		self.commentline = dict()
		self.commentlinewithinfo = dict()

	def parsejsonwithinfo(self):
		comments = self.comments['comments']
		for docnum in range(len(comments)):
			docID = str(docnum)
			text = comments[docnum]['text']
			self.commentline[docID] = text
			self.commentlinewithinfo[docID] = comments[docnum]
			text = text.lower()
			text = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', text)
			text = text.split()
			self.comment[docID] = text

	def getcomment(self):
		return self.comment

	def getcommentLine(self):
		return self.commentline
	
	def getcommentLinewithinfo(self):
		return self.commentlinewithinfo
