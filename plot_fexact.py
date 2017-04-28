import os
import sys
import re
import numpy as np
import random
import getopt
import time
import matplotlib.pyplot as plt
import scipy


# ========================================= Main Function ============================================= #

def main(argv):
	input_file_name = ""
	output_file_name = ""
	kelvin = 300 # Default Value

	# ============== Getting input options from command line ============== #

	try:
		opts, args = getopt.getopt(argv, "hi:k:",["ifile=","kelvin="])
	except getopt.GetoptError:
		print("Passing invalid options in command line!")
		print("Usage: load_dat.py -i <ifile>")
		sys.exit(0)

	for opt, arg in opts:
		if opt == "-h":
			print("Usage: load_dat.py -i <ifile>")
			sys.exit(1)
		elif opt in ("-i", "--ifile"):
			input_file_name = arg
			output_file_name = re.split(r"([^\\]+)\.dat$",arg)[1] + "_out" + ".dat"
			if os.path.exists(os.getcwd()+"/"+output_file_name):
				os.system("rm %s"%os.getcwd()+"/"+output_file_name)
		elif opt in ("-k","--kevlin"):
			kelvin = int(arg)


	# ==================== Open the file to read ========================= #

	try:
		input_file = open(os.getcwd()+ "/" +input_file_name,"r")
	except IOError:
		print("Can't open the file %s: File not exist or broken!"%input_file_name)
		sys.exit(2)

	try:
		output_file = open(os.getcwd()+ "/" + output_file_name,"w")
	except IOError:
		print("Can't open the file %s: File not exist or broken!"%out_file_name)
		sys.exit(2)

	# ==================== Parse input file and get value ================= #

	all_lines = []
	for line in input_file:
		data_line = [float(data) for data in line.strip().split()]
		all_lines.append(np.array(data_line))
	data_lines = np.array(all_lines)
	last_column = len(data_lines[0])
	num_trails = len(data_lines[0]) // 2

	# ==================== Calculate work for each traj =================== #

	time_series = data_lines[:,0]
	standard_work = data_lines[:,1]

	# ====================== Plot the graphs ============================== #

	plt.figure(1)
	plt.plot(time_series, standard_work, "b")
	plt.show()
	plt.close()

	# ====================== Final and clean up =========================== #

	input_file.close()
	output_file.close()


if __name__ == "__main__":
	main(sys.argv[1:])
