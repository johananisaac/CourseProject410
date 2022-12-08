import re
import string
class QueryParser:

    def __init__(self, query):
        self.query = query
        self.queries = []

    # Lowercase, remove punctuation, and tokenize query
    def parse(self): 
        query = self.query.lower()
        query = re.sub(r'[%s]' % re.escape(string.punctuation), '', query)
        self.queries.append(query.split())
    
    # Return tokenized query    
    def getQuery(self):
        return self.queries

