#!/usr/bin/python3
# Author: Arif Khan (https://twitter.com/payloadartist)
# Data extracted from Chaos (by ProjectDiscovery)

import glob
from multiprocessing.pool import ThreadPool
import os
import requests
import zipfile

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
    'accept': '*/*',
}

response = requests.get('https://chaos-data.projectdiscovery.io/index.json', headers=headers)

"""
Downloader for zip files
"""

def download_url(url, save_path, chunk_size=128):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)

"""
Zip collector
Download zip files. Extract them into .txt files
Multi-threaded (30 threads run by default)
"""

def zip_collect(data):
 if data['bounty'] == True:
  download_url(data['URL'], './{}.zip'.format(data['name']))
  with zipfile.ZipFile('{}.zip'.format(data['name']), 'r') as zip_ref:
    zip_ref.extractall('./'.format(data['name']))

collect_th = ThreadPool(processes=30)
collect_th.map_async(zip_collect, response.json()) 

"""
Put them together into a single text file - all.txt
Optionally, after completion of process remove all residual files - rm *.txt *.zip, except 'all.txt'
Remove duplicates -> cat all.txt | sort -u > all_clean.txt
"""

with open('all.txt', 'w') as out:
  for file in glob.glob('*.txt'):
      with open(file, 'r') as inf:
        out.write(inf.read())
      if file != 'all.txt': # clean up residual files (optional) from directory
        os.remove(file)
        os.remove(file.rstrip('txt')+'zip') # also remove zip files
