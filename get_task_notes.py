#!/usr/local/bin/python2.7

import json
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', help='Lunch message')
parser.add_argument('-i', help='Idle message')

args = parser.parse_args()

tasks = json.loads(sys.stdin.readline())
msg = ""

if len(tasks) > 0:
	task = tasks[len(tasks)-1]
	msg = task["notes"]
else:
	msg = args.i

print msg