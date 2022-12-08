Please use app.py to run on the local server
-----------------------------------------------------------------------------------------------------------------------------
updated: Dec 7, 2022
updated file: /src/CommentParser.py
              /src/Search.py
              /output/search.html
search.html can now show the additional information including author name, number of likes, time stamp, and profile pickture
-----------------------------------------------------------------------------------------------------------------------------

# Project Documentation
-----------------------------------------------------------------------------------------------------------------------------
### (1) An overview of the project
The project applies some basic natural language processing techniques to process the text data from Youtube video comments and return comments according to their ranking score, given a search query. The project includes front-end and back-end interactions. We use the chrome extension package manifest V3, HTML, CSS and JavaScript for the front-end development and python for the back-end development. A user can get the searched result by opening up the extension in a Youtube video page, entering a query in the input textbox, then clicking the search button. Top-ranked comments, author names, profile photos, timestamps, and the number of replies will be displayed on a new page.
### (2) Team member contributions
Jiyao Zou - I created and designed a popup section for chrome extensions. I also wrote and modified python files to parse the JSON files received from the front end, run BM25 and return the ranked list of comments. Furthermore, I wrote and designed the popup page when the user clicks the search button.

Johanan Isaac - I wrote the code for extracting and storing comments from the YouTube API. I also wrote the code for communication between the extension and server, the server API endpoints, and the database which stores the comments for each video.
### (3) Libraries, models or other third-party tools:
##### Programming Languages:
- Python
- CSS
- JavaScript
- HTML

##### Ranking Model:
- Okapi BM25

##### Other tools:
- Flask
- SQLAlchemy
- Chrome Extension Manifest V3.0
- YouTube Data API v3

### (4) Code structures

##### Chrome extension:
- **manifest.json** - A config-like document for a chrome extension to work.
- **pop.css** - Format and design information for the pop-up section.
- **popup.html** - HTML page for pop-up section.
- **popup.js** - Adds event listener for popup.html search button and retrieves video URL.

##### Python for BM25 ranking and processing:
* **output/Search.py** - Master class that calls subclasses and methods to return sorted results by ranking scores.
  - **src/CommentExtractor.py** - To extract comments by calling the YouTube API.
  - **src/CommentParser.py** - To store and parse comments extracted from the YouTube page.
  - **src/QueryParser.py** - To store and parse queries entered by the user from the Chrome extension.
  - **src/QueryProcessor.py** - To process the parsed query by calculating the ranking score for each document.
    - **src/OkapiBM25.py** - Low-level class for calculating ranking scores using BM25.
    - **src/CommentProcessor.py** - To process parsed comments by creating an inverted index with word count in comments and document ID, and calculating each document length.
      - **src/DocLength.py** - Low-level class and methods to calculate document length
      - **src/InvertedIndex.py** - Low-level class and methods to calculate the inverted index

##### Flask and output pages:
- **src/app.py** - Flask frame to communicate with the front-end, manage the database, call Search.py, and display information to search.html
output/search.html - displays results in a static HTML webpage.
output/error.html - displays an error page if there is a problem loading comments.

### (5) Instructions to setup and run the application
- Download the code from Github.
- Open a Chrome browser.
  - Click “Extensions”
  - Click “Manage Extensions”
  - Click “Load Unpacked”
  - Find the “yt-comment-search” folder
  - Click “Select Folder”
- Open a YouTube video. 
  - (For more accurate and measurable results, we suggest you open relatively popular videos with more than 100 comments.)
- Click on the extension in the top right corner of the browser window.
- In the pop-up section, enter the query you want to search, then click the “search” button.
- A new page with the top-ranked comments and relative information will be displayed.
  - You can go back to the YouTube video page and make multiple search queries.
  - For videos with large comment sections (5,000+ comments) it may take some time to load.
