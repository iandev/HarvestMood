#!/usr/local/bin/python2.7

import sys
import os
import argparse

user = password = lunch_msg = idle_msg = ""
cmd = []

parser = argparse.ArgumentParser()
parser.add_argument('-u', help='Harvest username')
parser.add_argument('-p', help='Harvest password')
parser.add_argument('-l', help='Lunch message')
parser.add_argument('-i', help='Idle message')

args = parser.parse_args()

if args.l == None:
	args.l = ""
if args.i == None:
	args.i = ""
	
if args.u != None and args.p != None:
	cmd.append("./get_harvest_tasks.py -u " + args.u + " -p " + args.p)
	cmd.append("./get_task_notes.py -l '" + args.l + "' -i '" + args.i + "'")
	cmd.append("./set_skype_mood.py")

	os.system(" | ".join(cmd))



