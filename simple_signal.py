import sys
import os
import time

try:
	while True:
		print("I'm infinite, come and get me!")
		os.system("python myParsePDB.py -i BP1.pdb -o BP1_testout.pdb -a 2 -s 2 -m 2 -t 0")
except KeyboardInterrupt:
	print("Ctrl + C mother fucker!")
	sys.exit(0)