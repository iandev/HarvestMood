#!/usr/bin/python

import sys
sys.path.append('./Skype4Py')
import Skype4Py
skype = Skype4Py.Skype()
skype.Attach()

mood = sys.stdin.readline()
if skype.CurrentUserProfile.MoodText != mood:
	skype.CurrentUserProfile.MoodText = mood

