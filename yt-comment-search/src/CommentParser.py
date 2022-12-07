import re
import json

class CommentParser:

	def __init__(self, filename):
		self.filename = filename
		#self.regex = re.compile('^#\s*\d+')
		self.comment = dict()
		self.commentline = dict()

	def parsejsonwithinfo(self):
		with open(self.filename,'rb') as file:
			data = json.load(file, encoding = 'UTF-8')
		numOfComments = data['comments']
		for docnum in range(len(numOfComments)):
			docID = str(docnum)
			commentText = numOfComments[docnum]['text']
			self.commentline[docID] = commentText
			self.commentlinewithinfo[docID] = numOfComments[docnum]
			eachComment = re.sub('[(),.<>]', '', commentText)
			text = eachComment.split()
			self.comment[docID] = text

	def getcomment(self):
		return self.comment

	def getcommentLine(self):
		return self.commentline
	
	def getcommentLinewithinfo(self):
		return self.commentlinewithinfo
