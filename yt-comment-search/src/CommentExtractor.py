import requests
import googleapiclient.discovery

API_KEY = "AIzaSyBVZzoXTcwXQ7cIXKrwH1CY1dDTpYl00Gc";
API_SERVICE = "youtube"
API_VERSION = "v3"

class CommentExtractor:

	def __init__(self):
		self.comments = {
			"numComments": 0,
			"comments": []
		}

	# Processes each comment in the list and adds it to self.comments
	def addComments(self, comments):
		for comment in comments:

			# Gathers attributes from the API resource into a dictionary
			commentInfo = {
				"text": comment["snippet"]["topLevelComment"]["snippet"]["textOriginal"],
				"numLikes": comment["snippet"]["topLevelComment"]["snippet"]["likeCount"],
				"timestamp": comment["snippet"]["topLevelComment"]["snippet"]["publishedAt"],
				"authorName": comment["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
				"authorProfilePic": comment["snippet"]["topLevelComment"]["snippet"]["authorProfileImageUrl"],
				"authorChannelLink": comment["snippet"]["topLevelComment"]["snippet"]["authorChannelUrl"],
				"isUpdated": comment["snippet"]["topLevelComment"]["snippet"]["updatedAt"]
			}

			self.comments["comments"].append(commentInfo)
			self.comments["numComments"] += 1

	# Calls the YouTube API to retrieve comment threads
	def requestComments(self, videoID):

		# Setting up and executing the request
		youtube = googleapiclient.discovery.build(API_SERVICE, API_VERSION, developerKey = API_KEY)
		url = "https://www.googleapis.com/youtube/v3/commentThreads?part=snippet%2Creplies"
		request = youtube.commentThreads().list(
			part = "snippet",
			videoId = videoID
		)
		response = request.execute()

		# Add the results of the first page to self.comments
		self.addComments(response["items"])

		# Keep requesting each new page and adding comments until the last page
		while "nextPageToken" in response:
			request = youtube.commentThreads().list(
				part = "snippet",
				videoId = videoID,
				pageToken = response["nextPageToken"]
				)
			response = request.execute()
			self.addComments(response["items"])

	# Return the list of comments extracted
	def getComments(self):
		return self.comments
