from QueryParser import *
from CommentParser import *
from QueryProcessor import QueryProcessor
import operator

class Search:


    def __init__(self):
        self.index = dict()
        self.queryfilename = './text/query.txt'
        self.commentfilename = './text/comment2.json'
        #self.commentfilename = './text/commenttest.txt'
        self.result = dict()

    def getqueryfile(self):
        return self.queryfilename

    def getcommentfile(self):
        return self.commentfilename
    
    def setqueryfile(self,filename):
        self.queryfilename = filename

    def setcommentfile(self,filename):
        self.commentfilename = filename

    def getRankedResult(self):
        query = QueryParser(self.getqueryfile())
        comment = CommentParser(self.getcommentfile())
        query.parse()
        parsedQuery = query.getQuery()
        comment.parsejson()
        parsedComment = comment.getcomment()
        commentline = comment.getcommentLine()
        results = QueryProcessor(parsedQuery, parsedComment).run()
        queryNum = 0
        returnedlist= dict()
        for result in results:
            rankedlist = sorted(result.items(), key=operator.itemgetter(1))
            rankedlist.reverse()
            index = 0
            for i in rankedlist[:10]:
                tmplist = (queryNum, i[0], index, i[1],commentline[str(i[0])].strip('\n'))
                #print(tmplist)
                index += 1
                returnedlist[str(index)] = tmplist[4]
                #print(tmplist[4])
            queryNum += 1
        return returnedlist


