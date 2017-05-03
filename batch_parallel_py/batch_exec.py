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
		opts, args = getopt.getopt(argv, "hs:t:r:m:a:f:",["angleStep=", "transStep=","rotatable=","movable=","strand=", "fold="])
	except getopt.GetoptError:
		print("batch_exec.py -s <angle_step> -t <translation_step> -r <rotatable> -m <movable> -a <strand> -f <fold>")
		sys.exit(1)
	for opt, arg in opts:
		if opt == "-h":
			print("batch_exec.py -s <angle_step> -t <translation_step> -r <rotatable> -m <movable> -a <strand> -f <fold>")
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


	try:
		if rotatable == 0 and movable == 0:
			print("You must make either strand rotatable or movable!")
			sys.exit(2)
		elif rotatable == 1 and movable == 0:
			if strand == 0:
				chosen_path = os.getcwd() + "/out_strand_rotate_0/"
			elif strand == 1:
				chosen_path = os.getcwd() + "/out_strand_rotate_1/"
			elif strand == 2:
				chosen_path = os.getcwd() + "/out_strand_rotate_2/"
			else:
				print("Invalid Option, setting to default!")
				chosen_path = os.getcwd() + "/out_strand_rotate_2/"
			root = chosen_path
			for i in range(0, 30, step):
				if strand >= 2:
					chosen_path = root + "BP1_OUT_Rotate_Angle_%d_both.pdb"%i
					os.system("python2 -OO myParsePDB.py -i BP1.pdb -o %s -a 2 -s %s -m 8 -t 0 -f %s" % (chosen_path,i,fold))
				elif strand in (0,1):
					chosen_path = root + "BP1_OUT_Rotate_Angle_%d_strand_%d.pdb"%(i,strand)
					os.system("python2 -OO myParsePDB.py -i BP1.pdb -o %s -a %d -s %s -m 8 -t 0 -f %s" % (chosen_path,strand,i,fold))
		elif rotatable == 0 and movable == 1:
			if strand == 0:
				chosen_path = os.getcwd() + "/out_strand_move_0/"
			elif strand == 1:
				chosen_path = os.getcwd() + "/out_strand_move_1/"
			else:
				print("Move should be controlled for one axis, setting to default!")
				chosen_path = os.getcwd() + "/out_strand_move_0/"
			root = chosen_path
			for i in frange(0, 5,trans):
				chosen_path = root + "BP1_OUT_Move_Trans_%s_strand_%d.pdb"%(str(i),strand)
				os.system("python2 -OO myParsePDB.py -i BP1.pdb -o %s -a 3 -s 2 -m %d -t %s -f %s" % (chosen_path,strand,i,fold))
		print("Completed!")
	except KeyboardInterrupt:
		print("Here is the KeyboardInterrupt Ctrl + C\n")
		quit()

if __name__ == "__main__":
	main(sys.argv[1:])
