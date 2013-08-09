#!/usr/bin/env python
# Simple Hello You how are you today?
import sys
import os
#import readline
namePerson=input()
nameOS=os.uname()
nameCWD=os.getcwd()
print('Hello {}, how are you doing today?\nYou are currently running {}, and your current working directory is {}.'.format(namePerson, nameOS, nameCWD))
