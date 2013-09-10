#!/usr/bin/python

import json
import sys

tasks = json.loads(sys.stdin.readline())
task = tasks[len(tasks)-1]
print task["notes"]