from CommentProcessor import *
from OkapiBM25 import getBM25Score


class QueryProcessor:
	def __init__(self, queries, comments):
		self.queries = queries
		self.dlt = findDocumentLength(comments)
		self.index = buildInvertIndexAndLength(comments)

	# Run each query 
	def run(self):
		results = []
		for query in self.queries:
			results.append(self.run_query(query))
		return results

	def run_query(self, query):
		query_result = dict()

		# Run for each token in the query
		for term in query:
			if term in self.index:
				# Retrieve index entry
				doc_dict = self.index[term] 

				# For each document
				for docID, freq in doc_dict.items(): 

					# Get the score from the ranking algorithm
					score = getBM25Score(n=len(doc_dict), f=freq, qf=1, r=0, N=len(self.dlt),
									   docLength=self.dlt.getLength(docID), averageDocLength=self.dlt.getAverageLength()) # calculate score
					
					# Check if this document has been scored before
					if docID in query_result: 
						query_result[docID] += score
					else:
						query_result[docID] = score
		return query_result
