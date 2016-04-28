The basic usage is to ```npm install``` and then simply run ```./get_latest_extensions.sh```

This will
* navigate to the Chrome extensions "Get Started" web page to scrape the information of the top ~50 or so Chrome extensions
* download and extract each of the extensions into subdirectories within this project

These archives can then be tested in Firefox by loading about:debugging#addons and adding each manifest.json through the "Load Temporary Addons" dialog
* automated adding of these extensions to a profile may come in a bit
