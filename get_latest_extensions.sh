#!/bin/bash
npm install
./node_modules/phantomjs/bin/phantomjs save_get_started.js
python grab_all.py
