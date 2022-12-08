import re
import json
import string

class CommentParser:

	# Takes extracted comment dictionary as input
	def __init__(self, comments):
		self.comments = comments
		self.comment = dict()
		self.commentLine = dict()
		self.commentLineWithInfo = dict()

	# Parses comment dictionary and tokenizes
	def parseCommentInfo(self):
		comments = self.comments['comments']

		for docnum in range(len(comments)):
			# create an ID for each comment
			docID = str(docnum)

			# Store original comment text
			text = comments[docnum]['text']
			self.commentLine[docID] = text

			# Store original comment data
			self.commentLineWithInfo[docID] = comments[docnum]

			# Lowercase, remove punctuation, and tokenize comment text
			text = text.lower()
			text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
			text = text.split()

			# Store tokenized comment
			self.comment[docID] = text

	# Return tokenized comments
	def getComment(self):
		return self.comment

	# Return original comments text
	def getCommentLine(self):
		return self.commentLine

	# Return original comments data
	def getCommentLineWithInfo(self):
		return self.commentLineWithInfo
