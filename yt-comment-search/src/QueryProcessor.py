from CommentProcessor import *
from OkapiBM25 import getBM25Score


class QueryProcessor:
	def __init__(self, queries, comments):
		self.queries = queries
		self.dlt = findDocumentLength(comments)
		self.index = buildInvertIndexAndLength(comments)

	
	def run(self):
		results = []
		print(self.queries)
		for query in self.queries:
			#print(query)
			results.append(self.run_query(query))
		return results

	def run_query(self, query):
		query_result = dict()
		for term in query:
			if term in self.index:
				doc_dict = self.index[term] # retrieve index entry
				for docID, freq in doc_dict.items(): #for each document and its word frequency
					score = getBM25Score(n=len(doc_dict), f=freq, qf=1, r=0, N=len(self.dlt),
									   docLength=self.dlt.getLength(docID), averageDocLength=self.dlt.getAverageLength()) # calculate score
					if docID in query_result: #this document has already been scored once
						query_result[docID] += score
					else:
						query_result[docID] = score
		print(query_result,'result')
		return query_result
