search = document.getElementById("search-form")
button = document.getElementById("ycse410_opts_btn_cache")
search.addEventListener("submit", (event) => {
  event.preventDefault();
  button.innerHTML = "Loading"
  var data = new FormData(search);
  url = "http://127.0.0.1:5102/query"
  var request = new XMLHttpRequest();
  request.onreadystatechange = function() {
    if (request.readyState == 4) {
        if (request.status == 200) {
            button.innerHTML = "Search"
            videoID = data.get("url").split("?v=").pop()
            videoID = videoID.split("&")[0]
            query = videoID.concat("/", data.get("query"))
            result_url = "http://127.0.0.1:5102/results/"
            window.open(result_url.concat(query)).location;
        }
    }
  }
  request.open("POST", url, true);    
  request.send(data);
});