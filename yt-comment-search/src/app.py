
from flask import Flask, request, jsonify
from flask import render_template
from Search import Search
from CommentExtractor import CommentExtractor
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__,template_folder='../output')
app.secret_key = "temp"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy()
db.init_app(app)

class StoredComments(db.Model):
    videoID = db.Column(db.String, primary_key=True)
    comments = db.Column(db.String, unique=False, nullable=True)

with app.app_context():
    db.create_all()

@app.route('/results/<videoID>/<query>')
def showResult(videoID, query):
    result = db.session.execute(db.select(StoredComments).where(StoredComments.videoID == videoID)).one_or_none()
    if result == None:
        return render_template('error.html')
    comments = json.loads(result[0].comments)
    return render_template('search.html', data = Search(comments).getRankedResult(query))

@app.route('/query', methods=["POST"])
def get_query():
    data = request.form
    currentVideoID = data['url'].split("?v=").pop()
    currentVideoID = currentVideoID.split("&")[0]
    stored = db.session.execute(db.select(StoredComments).where(StoredComments.videoID == currentVideoID)).one_or_none()
    if stored == None:
        print("Storing new video comments!")
        extractor = CommentExtractor()
        extractor.requestComments(currentVideoID)
        currentComments = extractor.getComments()
        storedComment = StoredComments(
            videoID = currentVideoID,
            comments = json.dumps(currentComments)
        )
        db.session.add(storedComment)
        db.session.commit()
    else:
        print("Video already stored!")
    return {"response": "ok"}

@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5102)
    #print('The result is',Search().getRankedResult())
    #print(Search().getRankedResult())
	#main()
	#print(type(main()))