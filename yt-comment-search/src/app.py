
from flask import Flask, request, jsonify
from flask import render_template
from Search import Search

app = Flask(__name__,template_folder='../output')

@app.route('/')
def showResult():
    data = Search().getRankedResult()

    return render_template('search.html', data = Search().getRankedResult())

@app.route('/comments', methods=["POST"])
def add_comments():
    print(request.json["commentData"])
    ## Send comments to get stored
    return {"response": "comments added"}

@app.route('/query', methods=["POST"])
def get_query():
    data = request.form
    print(data['query'])
    ## Run query and get results

    return {"response": "comments added"}

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