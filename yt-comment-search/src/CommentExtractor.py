from Comment import Comment
import requests
import googleapiclient.discovery

API_KEY = "AIzaSyBVZzoXTcwXQ7cIXKrwH1CY1dDTpYl00Gc";
API_SERVICE = "youtube"
API_VERSION = "v3"

class CommentExtractor:

	def __init__(self):
		self.comments = {}
		self.comments["numComments"] = 0
		self.comments["comments"] = []

	def addComments(self, comments):
		for comment in comments:
			text = comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"]
			numLikes = comment["snippet"]["topLevelComment"]["snippet"]["likeCount"]
			timestamp = comment["snippet"]["topLevelComment"]["snippet"]["publishedAt"]
			authorName = comment["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"]
			authorProfilePic = comment["snippet"]["topLevelComment"]["snippet"]["authorProfileImageUrl"]
			authorChannelLink = comment["snippet"]["topLevelComment"]["snippet"]["authorChannelUrl"]
			isUpdated = comment["snippet"]["topLevelComment"]["snippet"]["updatedAt"]
			newComment = Comment(text, numLikes, timestamp, authorName, authorProfilePic, authorChannelLink, isUpdated)
			self.comments["comments"].append(newComment.asdict())
			self.comments["numComments"] += 1

	def requestComments(self, videoID):
		youtube = googleapiclient.discovery.build(API_SERVICE, API_VERSION, developerKey = API_KEY)
		url = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet%2Creplies"
		request = youtube.commentThreads().list(
			part = "snippet",
			videoId = videoID
		)
		response = request.execute()
		self.addComments(response["items"])
		while "nextPageToken" in response:
			request = youtube.commentThreads().list(
				part = "snippet",
				videoId = videoID,
				pageToken = response["nextPageToken"]
				)
			response = request.execute()
			self.addComments(response["items"])

	def getComments(self):
		return self.comments
