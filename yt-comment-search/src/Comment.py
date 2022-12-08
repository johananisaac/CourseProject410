class Comment:
	def __init__(self, text, numLikes, timestamp, authorName, authorProfilePic, authorChannelLink, isUpdated):
		self.text = text
		self.numLikes = numLikes
		self.timestamp = timestamp
		self.authorName = authorName
		self.authorProfilePic = authorProfilePic
		self.authorChannelLink = authorChannelLink
		self.isUpdated = isUpdated

	def asdict(self):
		return {
				"text": self.text,
				"numLikes": self.numLikes,
				"timestamp": self.timestamp,
				"authorName": self.authorName,
				"authorProfilePic": self.authorProfilePic,
				"authorChannelLink": self.authorChannelLink,
				"isUpdated": self.isUpdated
			}