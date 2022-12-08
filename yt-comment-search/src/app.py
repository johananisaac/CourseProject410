
from flask import Flask, request, jsonify
from flask import render_template
from Search import Search
from CommentExtractor import CommentExtractor

import json
import os

app = Flask(__name__,template_folder='../output')

@app.route('/')
def showResult():
    #data = Search().getRankedResult()
    dirname = os.path.join(os.path.dirname(__file__), '..', 'text')
    commentfilename = os.path.join(dirname, 'comments4.json')
    with open(commentfilename, 'rb') as file:
        comments = json.load(file)
    query = "peppa pig"
    return render_template('search.html', data = Search(comments).getRankedResult(query))

@app.route('/query', methods=["POST"])
def get_query():
    data = request.form
    videoID = data['url'].split("?v=").pop()
    query = data['query']
    ## Run query and get results
    print(videoID)
    extractor = CommentExtractor()
    extractor.requestComments(videoID)
    comments = extractor.getComments()
    print(comments)
    return render_template('search.html', data = Search(comments).getRankedResult(query))

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5102)
    #print('The result is',Search().getRankedResult())
    #print(Search().getRankedResult())
	#main()
	#print(type(main()))