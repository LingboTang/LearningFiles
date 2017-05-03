#!/usr/bin/python

import os
import sys
import time
import getopt

def frange(x, y, jump):
  while x < y:
    yield x
    x += jump


def main(argv):
	step = 2 #default
	trans = 1 #default
	rotatable = 0 #default
	movable = 0 #default
	strand = 0
	chosen_path = ""

	try:
		opts, args = getopt.getopt(argv, "hs:t:r:m:a:f:d:u:n:",["angleStep=", "transStep=","rotatable=","movable=","strand=", "fold=", "inidis=", "angleupper=", "transupper="])
	except getopt.GetoptError:
		print("batch_exec.py -s <angle_step> -t <translation_step> -r <rotatable> -m <movable> -a <strand> -f <fold> -d <inidis>")
		sys.exit(1)
	for opt, arg in opts:
		if opt == "-h":
			print("batch_exec.py -s <angle_step> -t <translation_step> -r <rotatable> -m <movable> -a <strand> -f <fold> -d <inidis>")
			sys.exit()
		elif opt in ("-s", "--angleStep"):
			step = int(arg)
		elif opt in ("-t", "--transStep"):
			trans = float(arg)
		elif opt in ("-r", "--rotatable"):
			rotatable = int(arg)
		elif opt in ("-m", "--movable"):
			movable = int(arg)
		elif opt in ("-a", "--strand"):
			strand = int(arg)
		elif opt in ("-f", "--fold"):
			fold = int(arg)
		elif opt in ("-d", "--inidis"):
			inidis = float(arg)
		elif opt in ("-u", "--angleupper"):
			angle_upper = int(arg)
		elif opt in ("-n", "--transupper"):
			trans_upper = float(arg)


	try:
		if rotatable == 0 and movable == 0:
			print("You must make either strand rotatable or movable!")
			sys.exit(2)
		elif rotatable == 1 and movable == 0:
			if strand in range(fold*2 + 1):
				chosen_path = os.getcwd() + "/out_rotate/"
			else:
				print("Invalid Option, setting to default!")
				sys.exit(3)
			root = chosen_path
			for i in range(0, angle_upper, step):
				if strand >= 8:
					chosen_path = root + "BP1_OUT_Rotate_Angle_%d_all.pdb"%i
					os.system("python2 -OO myParsePDB.py -i BP1.pdb -o %s -a %s -s %s -m %s -t 0 -f %s -d %f" % (chosen_path, fold*2, i, fold*2, fold, inidis))
				elif strand in range(fold * 2):
					chosen_path = root + "BP1_OUT_Rotate_Angle_%d_strand_%d.pdb"%(i,strand)
					os.system("python2 -OO myParsePDB.py -i BP1.pdb -o %s -a %d -s %s -m %s -t 0 -f %s -d %f" % (chosen_path, strand, i, fold*2, fold, inidis))
		elif rotatable == 0 and movable == 1:
			if strand in range(fold * 2):
				chosen_path = os.getcwd() + "/out_move/"
			else:
				print("Move should be controlled for one axis, setting to default!")
				sys.exit(4)
			root = chosen_path
			for i in frange(0, trans_upper, trans):
				chosen_path = root + "BP1_OUT_Move_Trans_%s_strand_%d.pdb"%(str(i),strand)
				os.system("python2 -OO myParsePDB.py -i BP1.pdb -o %s -a %s -s 2 -m %d -t %s -f %s -d %f" % (chosen_path, fold*2 + 1, strand, i, fold, inidis))
		print("Completed!")
	except KeyboardInterrupt:
		print("Here is the KeyboardInterrupt Ctrl + C\n")
		quit()

if __name__ == "__main__":
	main(sys.argv[1:])