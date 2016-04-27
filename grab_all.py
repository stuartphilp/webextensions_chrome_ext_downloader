import json
import requests
import subprocess
from pprint import pprint

# sample
# response = requests.post('https://api.github.com/user/repos', data=json.dumps({'name': 'foo'}), auth=('user', 'pass'))
# assert response.status_code == 201


with open('ext_list.json') as data_file:
    extensions = json.load(data_file)

for ext in extensions:
  ext_name = ext.split("/")[-2]
  ext_id = ext.split("/")[-1]
  pprint("Grabbing extension {0}, ID {1}".format(ext_name, ext_id))
  subprocess.call("./chrome_ext_downloader.sh {0}".format(ext_id), shell=True)
