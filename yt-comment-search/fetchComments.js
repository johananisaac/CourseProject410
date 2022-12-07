const API_KEY = "AIzaSyBVZzoXTcwXQ7cIXKrwH1CY1dDTpYl00Gc";


class Comment{
  constructor(text, hasReplies, numLikes, timestamp, authorName, authorProfilePic, authorChannelLink, isUpdated){
    this.text = text;
    this.hasReplies = hasReplies;
    this.numLikes = numLikes;
    this.timestamp = timestamp;
    this.authorName = authorName;
    this.authorProfilePic = authorProfilePic;
    this.authorChannelLink = authorChannelLink;
    this.isUpdated = isUpdated;
    this.replies = [];
    this.numReplies = 0;
  }

  addReply(comment) {
    let text = comment.snippet.textOriginal;
    let hasReplies = false;
    let numLikes = comment.snippet.likeCount;
    let timestamp = comment.snippet.publishedAt;
    let authorName = comment.snippet.authorDisplayName;
    let authorProfilePic = comment.snippet.authorProfileImageUrl;
    let authorChannelLink = comment.snippet.authorChannelUrl;
    let isUpdated = timestamp != comment.snippet.updatedAt;

    let newReply = new Comment(text, hasReplies, numLikes, timestamp, authorName, authorProfilePic, authorChannelLink, isUpdated);
    this.replies.push(newReply);
    this.numReplies += 1;
  }

  addReplies(replies){
    replies.comments.forEach(comment => this.addReply(comment))
  }

}

class Comments{
  constructor(){
    this.numComments = 0;
    this.comments = [];
  }

  addComment(comment){
    this.comments.push(comment);
    this.numComments += 1;
    this.numComments += comment.numReplies;
  }
}


/* Returns videoId of the current tab

  TODO - make sure videoID extraction works for multiple url schemes
*/
async function getVideoId() {
  tab = window.location.href;
  return tab.split("?v=").pop();
}


/*

  TODO - make separate function with fetch request for replies
*/
async function getComment(comment) {
  let text = comment.snippet.topLevelComment.snippet.textOriginal;
  let hasReplies = comment.snippet.totalReplyCount > 0;
  let numLikes = comment.snippet.topLevelComment.snippet.likeCount;
  let timestamp = comment.snippet.topLevelComment.snippet.publishedAt;
  let authorName = comment.snippet.topLevelComment.snippet.authorDisplayName;
  let authorProfilePic = comment.snippet.topLevelComment.snippet.authorProfileImageUrl;
  let authorChannelLink = comment.snippet.topLevelComment.snippet.authorChannelUrl;
  let isUpdated = timestamp != comment.snippet.topLevelComment.snippet.updatedAt;

  let newComment = new Comment(text, hasReplies, numLikes, timestamp, authorName, authorProfilePic, authorChannelLink, isUpdated)

  //Populate replies
  if (hasReplies) {
    newComment.addReplies(comment.replies)
  }
  
  //Put comment in commentData
  commentData.addComment(newComment);
}


async function getCommentPage(comments, pageToken, videoId) {
  comments.forEach(getComment)
  if (pageToken != 0) {
    await fetch(`https://www.googleapis.com/youtube/v3/commentThreads?part=snippet%2Creplies&videoId=${videoId}&pageToken=${pageToken}&key=${API_KEY}`)
    .then(response => response.json())
    .then(async function(data) {
      nextPageToken = 0;
      if ("nextPageToken" in data) {
        nextPageToken = data["nextPageToken"]
      }
      await getCommentPage(data["items"], nextPageToken, videoId)
    })
  }
}



/* Fills commentData with video comments */
async function getComments() {
  /*chrome.tabs.query({ active: true, lastFocusedWindow: true }, function (tabs) {
    var videoUrl = tabs[0]
  });*/
  //let videoId = videoUrl.split("?v=").pop()
  //let videoId = await getVideoId();
  let videoId = "O_3Xf3gTzEE"
  //let videoId = window.location.href.split("?v=").pop()
  //alert(videoId)
  await fetch(`https://www.googleapis.com/youtube/v3/commentThreads?part=snippet%2Creplies&videoId=${videoId}&key=${API_KEY}`)
  .then(response => response.json())
  .then(async function(data) {
    nextPageToken = 0;
    if ("nextPageToken" in data) {
      nextPageToken = data["nextPageToken"]
    }
    await getCommentPage(data["items"], nextPageToken, videoId)
  });
  return commentData
}

async function updateDom() {
  let comments = await getComments();

  fetch("http://127.0.0.1:5102/comments", {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({commentData})
  })
  .then( (response) => { 
    console.log(response.json())
  });
}

var commentData = new Comments();
updateDom()