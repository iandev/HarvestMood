#!/usr/bin/python

import sys
import json
sys.path.append('./PythonHarvest')
sys.path.append('./Requests')
import harvest
h = harvest.Harvest("https://thirdmind.harvestapp.com", sys.argv[1], sys.argv[2])
today = h.get_today()
today_data = today()
print json.dumps(today_data['day_entries'])

