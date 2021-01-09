#!/usr/bin/python3
# Author: Arif Khan (https://twitter.com/payloadartist)
# Data extracted from Chaos (by ProjectDiscovery)

import argparse
import glob
from multiprocessing.pool import ThreadPool
import os
import requests
import zipfile

parser = argparse.ArgumentParser(description='If needed, specify output directory or, file name. Example: ./targets_extract.py -o assets.txt to store to ./output/assets.txt, optionally specify directory (./targets_extract.py -d mydir). Also, you can increase number of processes with -c flag to make it even faster.')
parser.add_argument('-d','--directory', default='output',
                    help='Specify an output directory [Default: ./output]')
parser.add_argument('-o','--output',
                    default='all.txt',
                    help='Specify an output file name [Default: all.txt]')
parser.add_argument('-c', '--processes',
                    default='30', type=int,
                    help='Specify number of processes for faster extraction [Default: 30]')
args = parser.parse_args()

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
Multi-process for faster performance (30 processes run by default)
"""

def zip_collect(data):
 if data['bounty'] == True:
  download_url(data['URL'], './{}.zip'.format(data['name']))
  with zipfile.ZipFile('{}.zip'.format(data['name']), 'r') as zip_ref:
    zip_ref.extractall('./')
  os.remove('{}.zip'.format(data['name'])) # Clean up zip files after extraction

collect_th = ThreadPool(processes=args.processes)
collect_th.map(zip_collect, response.json()) 

"""
Put them together into a single text file - all.txt
Optionally, after completion of process remove all residual files - rm *.txt *.zip, except 'all.txt'
Remove duplicates if any -> cat all.txt | sort -u > all_clean.txt
"""

with open('all_0.txt', 'w') as out:
  for file in glob.glob('*.txt'):
    if file != 'all_0.txt':
      with open(file, 'r') as inf:
        out.write(inf.read())
        """
        A word of caution - Not suggested if you have other text files in the same directory,
        this removes all *.txt files except all.txt, for cleanup. In case you don't want that,
        add a '#' and comment out the line below
        """
      os.remove(file) # clean up residual txt files (optional) from directory

if not os.path.isdir(args.directory):
    os.mkdir(args.directory)

os.system("cat all_0.txt | sort | uniq > {}/{}".format(args.directory, args.output))
os.remove("all_0.txt")
