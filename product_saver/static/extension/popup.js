document.addEventListener('DOMContentLoaded', function() {
    var checkPageButton = document.getElementById('checkPage');
    checkPageButton.addEventListener('click', function() {
  
      chrome.tabs.query({active: true}, function(tabs) {
        d = document;
        
        console.log("tabs: ", tabs);
        console.log("d: ", d);
        
      });
    }, false);
  }, false);