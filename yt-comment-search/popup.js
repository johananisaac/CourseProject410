search = document.getElementById("search-form")
button = document.getElementById("ycse410_opts_btn_cache")
search.addEventListener("submit", (event) => {
  // Prevents default form submission
  event.preventDefault();

  // Button shows "Loading" while comments are extracted
  button.innerHTML = "Loading"

  // Create request and data to send
  var request = new XMLHttpRequest();
  var data = new FormData(search);
  url = "http://127.0.0.1:5102/query"
  
  // Runs function when request is finished
  request.onreadystatechange = function() {
    if (request.readyState == 4) {
        // If status is OK
        if (request.status == 200) {
            // Change button back to "Search"
            button.innerHTML = "Search"

            // Get the videoID from the URL
            videoID = data.get("url").split("?v=").pop()
            videoID = videoID.split("&")[0]

            //Build the URL for the result page and opens in new tab
            query = videoID.concat("/", data.get("query"))
            result_url = "http://127.0.0.1:5102/results/"
            window.open(result_url.concat(query)).location;
        }
    }
  }

  // Send the request
  request.open("POST", url, true);    
  request.send(data);
});

// Gets the URL of the current tab so it is available for the POST request
chrome.tabs.query(
    {active:true},
    tabs=>{
        const tab=tabs[0];
        console.log("URL:", tab.url)
        var pageURL = tab.url
        document.getElementById('pageURL').setAttribute('value', tab.url)
    }
)