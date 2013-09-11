#!/usr/local/bin/python2.7

import sys
import json
import argparse
sys.path.append('./PythonHarvest')
sys.path.append('./Requests')
import harvest

parser = argparse.ArgumentParser()
parser.add_argument('-u', help='Harvest username')
parser.add_argument('-p', help='Harvest password')

args = parser.parse_args()

h = harvest.Harvest("https://thirdmind.harvestapp.com", args.u, args.p)
today = h.get_today()
today_data = today()
print json.dumps(today_data['day_entries'])

