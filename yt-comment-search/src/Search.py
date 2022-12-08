from QueryParser import *
from CommentParser import *
from QueryProcessor import QueryProcessor
import operator
import os

class Search:


    def __init__(self, comments):
        self.index = dict()
        self.result = dict()
        self.comments = comments

    def getRankedResult(self, queryData):
        query = QueryParser(queryData)
        comment = CommentParser(self.comments)
        query.parse()
        parsedQuery = query.getQuery()
        parsedComment = comment.getcomment()
        comment.parsejsonwithinfo()
        commentlineinfo = comment.getcommentLinewithinfo()
        results = QueryProcessor(parsedQuery, parsedComment).run()
        queryNum = 0
        returnedlist= dict()
        for result in results:
            rankedlist = sorted(result.items(), key=operator.itemgetter(1))
            rankedlist.reverse()
            index = 0
            for i in rankedlist[:10]:
                textsToShow = commentlineinfo[str(i[0])]['text'].strip('\n')
                authorToShow = commentlineinfo[str(i[0])]['authorName']
                numLikesToShow = str(commentlineinfo[str(i[0])]['numLikes'])
                numberRepliesToShow = str(commentlineinfo[str(i[0])]['numReplies'])
                timestampToShow = commentlineinfo[str(i[0])]['timestamp']
                profileToShow = commentlineinfo[str(i[0])]['authorProfilePic']
                tmplist = [queryNum, i[0], index, i[1],textsToShow,authorToShow,numLikesToShow,numberRepliesToShow,timestampToShow,profileToShow]
                index += 1
                returnedlist[str(index)] = tmplist
            queryNum += 1
        return returnedlist


