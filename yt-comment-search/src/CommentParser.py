import re
import json

class CommentParser:

	def __init__(self, filename):
		self.filename = filename
		#self.regex = re.compile('^#\s*\d+')
		self.comment = dict()
		self.commentline = dict()

	def parsetxt(self):
		commentStoreList=[]
		with open(self.filename) as f:
			for line in f:
				commentStoreList.append(line)
		docnum = 0
		for eachComment in commentStoreList:
			docID = str(docnum)
			self.commentline[docID] = eachComment
			eachComment=re.sub('[(),.<>]', '', eachComment)
			text = eachComment.split()
			self.comment[docID] = text
			docnum += 1
		#print(self.comment["3"])

	def parsejson(self):
		commentStoreList=[]
		with open(self.filename,'rb') as file:
			data = json.load(file, encoding = 'UTF-8')
		numOfComments = data['comments']
		for i in range(len(numOfComments)):
			commentStoreList.append(numOfComments[i]['text'])
		docnum = 0
		for eachComment in commentStoreList:
			docID = str(docnum)
			self.commentline[docID] = eachComment
			eachComment=re.sub('[(),.<>]', '', eachComment)
			text = eachComment.split()
			self.comment[docID] = text
			docnum += 1
		#print(self.comment["3"])

	def getcomment(self):
		return self.comment

	def getcommentLine(self):
		return self.commentline