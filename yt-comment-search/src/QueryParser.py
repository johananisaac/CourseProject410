import re
import string
class QueryParser:

    def __init__(self, query):
        self.query = query
        self.queries = []

    #to process the txt file
    def parse(self):
        query = self.query.lower()
        query = re.sub(r'[%s]' % re.escape(string.punctuation), '', query)
        self.queries.append(query.split())
        #print('query',self.queries)
        
    def getQuery(self):
        return self.queries

