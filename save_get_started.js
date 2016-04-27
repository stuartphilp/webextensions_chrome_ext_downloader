var page = require('webpage').create();
var fs = require('fs');
page.open('https://chrome.google.com/webstore/category/collection/get_started', function () {
    window.setTimeout(function () {

      var links = page.evaluate(function() {
          return [].map.call(document.querySelectorAll('a.a-u'), function(link) {
              return link.getAttribute('href');
          });
      });
      page.render('get_started.png');
      fs.write('ext_list.json', JSON.stringify(links), 'w');
      phantom.exit();
    }, 3000);
});
