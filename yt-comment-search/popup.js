chrome.tabs.query(
    {active:true},
    tabs=>{
        const tab=tabs[0];
        console.log("URL:", tab.url)
        var pageURL = tab.url
        document.getElementById('pageURL').setAttribute('value', tab.url)
    }
)