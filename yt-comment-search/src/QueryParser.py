import re
class QueryParser:

    def __init__(self, filename):
        self.filename = filename
        self.queries = []

    #to process the txt file
    def parse(self):
        #print(self.filename)
        with open(self.filename) as f:
            lines = ''.join(f.readlines())
            lines=re.sub('[(),.<>]', '', lines)
            result = lines.rstrip().split()
            #print('hello',lineWithoutNewLine)
            #result = lineWithoutNewLine.rstrip().split()
            print(result)
            self.queries.append(result)
            print('query',self.queries)
        
    def getQuery(self):
        return self.queries

