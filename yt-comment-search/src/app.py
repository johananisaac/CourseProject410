
from flask import Flask, request, jsonify
from flask import render_template
from Search import Search
from CommentExtractor import CommentExtractor
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__,template_folder='../output')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy()
db.init_app(app)


# The schema for database entries (videoID, comments)
#   comments is a string-casted dictionary of comment data for a certain video
class StoredComments(db.Model):
    videoID = db.Column(db.String, primary_key=True)
    comments = db.Column(db.String, unique=False, nullable=True)

with app.app_context():
    db.create_all()


# This is the route to the results page
#   The extension redirects here after the search button is pressed
#   URL is dependent on the videoID and query
@app.route('/results/<videoID>/<query>')
def showResult(videoID, query):
    # Query the database for comments matching the videoID
    result = db.session.execute(db.select(StoredComments).where(StoredComments.videoID == videoID)).one_or_none()

    # If videoID is not in the database, show an error page
    if result == None:
        return render_template('error.html')

    # Recast comments to python dictionary
    comments = json.loads(result[0].comments)

    # Calls Search.getRankedResult to get the results for the query
    return render_template('search.html', data = Search(comments).getRankedResult(query))


# This is a route for handling post requests
#   The extension makes a post request here containing the video URL and query
@app.route('/query', methods=["POST"])
def get_query():

    data = request.form

    # Extract videoID from URL
    currentVideoID = data['url'].split("?v=").pop()
    currentVideoID = currentVideoID.split("&")[0]

    # Query the database for videoID
    stored = db.session.execute(db.select(StoredComments).where(StoredComments.videoID == currentVideoID)).one_or_none()

    # If videoID is not in the database, extract the comments and store them in the database
    if stored == None:
        extractor = CommentExtractor()
        extractor.requestComments(currentVideoID)
        extractedComments = extractor.getComments()
        newComments = StoredComments(
            videoID = currentVideoID,
            comments = json.dumps(extractedComments)
        )
        db.session.add(newComments)
        db.session.commit()

    return {"response": "ok"}


# This runs after each request to add headers to response
#   Allows requests from any origin
@app.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 5102)