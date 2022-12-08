chrome.runtime.onMessage.addListener(({ type, name }) => {
  if (type === "totalComments") {
    chrome.storage.local.set({ name });
    console.log("received comment number" + name)
    sendResponse({confirm: "totalComments set in storage"})
  }
});

chrome.action.onClicked.addListener((tab) => {
  chrome.storage.local.get(["totalComments"], ({ name }) => {
    chrome.tabs.sendMessage(tab.id, { name });
  });
});