#!/usr/bin/python

import sys
sys.path.append('./Skype4Py')
import Skype4Py
skype = Skype4Py.Skype()
skype.Attach()
skype.CurrentUserProfile.MoodText = sys.stdin.readline()

