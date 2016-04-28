import os
import json
import subprocess
import shutil
from pprint import pprint

with open('ext_list.json') as data_file:
    extensions = json.load(data_file)


path = "./extensions"
shutil.rmtree(path)
os.mkdir(path, 0755)
os.chdir(path)

for ext in extensions:
  ext_name = ext.split("/")[-2]
  ext_id = ext.split("/")[-1]
  pprint("=====================")
  pprint("Grabbing extension {0}, ID {1}".format(ext_name, ext_id))
  pprint("=====================")
  subprocess.call("../chrome_ext_downloader.sh {0}".format(ext_id), shell=True)
  pprint("=====================")
  pprint("DONE")
  pprint("=====================")
