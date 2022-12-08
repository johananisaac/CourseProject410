from DocLength import *
from InvertedIndex import *

# Builds inverted index
def buildInvertIndexAndLength(comment):
	idx = InvertedIndex()
	
	for docID in comment:
		for word in comment[docID]:
			idx.addWordByID(str(word), str(docID))
	return idx

# Calculates document length
def findDocumentLength(comment):
    docLength = DocLength()
    for docID in comment:
        length = len(comment[docID])
        docLength.add(docID, length)
    return docLength
