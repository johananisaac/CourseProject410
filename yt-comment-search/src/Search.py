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
        # Parse the query
        query = QueryParser(queryData)
        query.parse()
        parsedQuery = query.getQuery()

        # Parse the comments
        comment = CommentParser(self.comments)
        parsedComment = comment.getComment()
        comment.parseCommentInfo()
        commentLineInfo = comment.getCommentLineWithInfo()

        # Get the results for which comments match query 
        results = QueryProcessor(parsedQuery, parsedComment).run()

        queryNum = 0
        returnedList= dict()

        for result in results:
            rankedlist = sorted(result.items(), key=operator.itemgetter(1))
            rankedlist.reverse()
            index = 0

            # Store information for displaying comments
            for i in rankedlist:
                textsToShow = commentLineInfo[str(i[0])]['text'].strip('\n')
                authorToShow = commentLineInfo[str(i[0])]['authorName']
                numLikesToShow = str(commentLineInfo[str(i[0])]['numLikes'])
                timestampToShow = commentLineInfo[str(i[0])]['timestamp']
                profileToShow = commentLineInfo[str(i[0])]['authorProfilePic']
                tmplist = [queryNum, i[0], index, i[1],textsToShow,authorToShow,numLikesToShow,timestampToShow,profileToShow]
                index += 1
                returnedList[str(index)] = tmplist
            queryNum += 1
        return returnedList


