#!/bin/bash

# $1: the extension id to download and extract
_id="$1"
mkdir $_id
cd $_id
curl -L "https://clients2.google.com/service/update2/crx?response=redirect&prodversion=49.0&x=id%3D${_id}%26installsource%3Dondemand%26uc" > extension.crx
unzip extension.crx
