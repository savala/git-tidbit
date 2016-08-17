#!/usr/bin/env python

'''
	fortune.py

	attempts to call fortune, 
	prompts user to install if they don't already have it
'''

import subprocess
from distutils.spawn import find_executable

def __fortune_installed():
	return find_executable('fortune') is not None

def get_tidbit():
	if not __fortune_installed():
		raise ImportError("fortune is not installed. Use your favorite package manager to install it for more fun tidbits!")
	return subprocess.check_output('fortune').strip()		

if __name__=='__main__':
	print get_tidbit()
