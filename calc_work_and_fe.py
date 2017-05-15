import os
import sys
import re
import numpy as np
import random
import getopt
import time
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, pchip, splmake, splev, spline, interp1d
import signal

# ========================================= Exception ================================================= #

class Timeout():

	class Timeout(Exception):
		pass

	def __init__(self,sec):
		self.sec = sec

	def __enter__(self):
		signal.signal(signal.SIGALRM, self.raise_timeout)
		signal.alarm(self.sec)

	def __exit__(self, *args):
		signal.alarm(0)

	def raise_timeout(self, *args):
		raise Timeout.Timeout()


# ========================================= Global Parameter ========================================== #
KB = 1.98722e-3

# ========================================= Util Functions ============================================ #

def Beta(k,temp):
	return 1 /(k * temp)

def get_step_distances(traj):
	distances = []
	for i in range(len(traj)):
		if i == 0:
			dis = 0
		else:
			dis = traj[i] - traj[0]
		distances.append(dis)
	return np.array(distances)

def get_delta_dis(traj):
	delta_distances = []
	for i in range(len(traj)):
		if i == 0:
			delta_dis = 0
		else:
			delta_dis = traj[i] - traj[i-1]
		delta_distances.append(delta_dis)
	return np.array(delta_distances)

def get_delta_forces(forces):
	delta_Fs = []
	for i in range(len(forces)):
		if i == 0:
			delta_F = 0
		else:
			delta_F = forces[i] - forces[i-1]
		delta_Fs.append(delta_F)
	return np.array(delta_Fs)

def get_ave_forces(forces):
	ave_Fs = []
	for i in range(len(forces)):
		if i == 0:
			ave_F = 0
		else:
			ave_F = (forces[i] + forces[i-1]) / 2
		ave_Fs.append(ave_F)
	return np.array(ave_Fs)

# FE means free energy, assume the initial FE is 0

def calculate_work(distances, forces):
	works = []
	work = 0
	for i in range(len(forces)):
		work = work +  forces[i] * distances[i]
		works.append(work)
	return np.array(works)

def jarzynski_equality_simul_1(works, beta):
	FEs = []
	for i in range(len(works)):
		FEs.append(- 1 / beta * np.log(np.exp(-beta*works[i])))
	return np.array(FEs)

def jarzynski_equality_simul_2(works, beta):
	FEs = []
	FE = 0
	for i in range(len(works)):
		w = works[i]
		FE = w/10 - 1/2 * beta * ((w**2) / 10 - w**2 / 10)
		FEs.append(FE)
	FEs = np.array(FEs)
	return FEs


def column_wise_vec(data, col):
	return np.array([row[col] for row in data])


# ========================================= Main Function ============================================= #

def main(argv):
	input_file_name = ""
	output_file_name = ""
	kelvin = 300 # Default Value
	velocity = 0.01

	# ============== Getting input options from command line ============== #

	try:
		opts, args = getopt.getopt(argv, "hi:k:v:",["ifile=","kelvin=","velocity="])
	except getopt.GetoptError:
		print("Passing invalid options in command line!")
		print("Usage: calc_work_and_fe.py -i <ifile> -k <kelvin> -v <velocity>")
		sys.exit(0)

	for opt, arg in opts:
		if opt == "-h":
			print("Usage: calc_work_and_fe.py -i <ifile> -k <kelvin> -v <velocity>")
			sys.exit(1)
		elif opt in ("-i", "--ifile"):
			input_file_name = arg
			output_file_name = re.split(r"([^\\]+)\.dat$",arg)[1] + "_out" + ".dat"
			if os.path.exists(os.getcwd()+"/"+output_file_name):
				os.system("rm %s"%os.getcwd()+"/"+output_file_name)
		elif opt in ("-k","--kevlin"):
			kelvin = float(arg)
		elif opt in ("-v","--velocity"):
			velocity = float(arg)


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
	trajectories = [data_lines[:,col] for col in range(num_trails + 1) if col != 0]
	forces = [data_lines[:,col] for col in range(num_trails + 1, last_column)]

	# Works

	# Reference Work
	all_works_2 = []
	v_smooth = np.linspace(13.0, 33.0, 20001)
	delta_distances = get_delta_dis(v_smooth) 
	for i in range(num_trails):
		work_of_each_traj = calculate_work(delta_distances, forces[i])
		all_works_2.append(work_of_each_traj)
	all_works_2 = np.array(all_works_2)

	# Method 1
	all_FEs = []
	for i in range(num_trails):
		FEs = jarzynski_equality_simul_1(all_works_2[i], Beta(KB,kelvin))
		all_FEs.append(FEs)
	all_FEs = np.array(all_FEs) 
	
	# Method 2
	all_FEs_2 = []
	for i in range(num_trails):
		FEs_2 = jarzynski_equality_simul_2(all_works_2[i], Beta(KB, kelvin))
		all_FEs_2.append(FEs_2)
	all_FEs_2 = np.array(all_FEs_2)


	for i in range(len(all_works_2[0])):
		row_string = ""
		for j in range(num_trails):
			this_value = "%.6f"%trajectories[j][i]
			row_string = row_string + "    " + this_value.rjust(9)
		for j in range(num_trails):
			this_value = "%.6f"%all_works_2[j][i]
			row_string = row_string + "    " + this_value.rjust(9)
		row_string = row_string + "\n"
		output_file.write(row_string)



	# ====================== Plot the graphs ============================== #


	plt.figure(1)
	for i in range(num_trails):
		plt.plot(v_smooth, all_works_2[i])
	plt.suptitle("Trajectory vs Work")
	plt.show()
	plt.close()

	plt.figure(2)
	for i in range(num_trails):
		plt.plot(time_series, trajectories[i])
	plt.suptitle("Time vs Trajectory")
	plt.show()
	plt.close()

	plt.figure(3)
	for i in range(num_trails):
		plt.plot(time_series, forces[i])
	plt.suptitle("Time vs Force")
	plt.show()
	plt.close()

	plt.figure(4)
	for i in range(num_trails):
		plt.plot(trajectories[i], forces[i])
	plt.suptitle("Trajectory vs Force")
	plt.show()
	plt.close()

	plt.figure(5)
	for i in range(num_trails):
		plt.plot(v_smooth, all_FEs[i])
	plt.suptitle("Trajectory vs Method 1 FE")
	plt.show()
	plt.close()

	plt.figure(6)
	for i in range(num_trails):
		plt.plot(v_smooth,all_FEs_2[i])
	plt.suptitle("Trajectory vs Method 2 FE")
	plt.show()
	plt.close()


	# ====================== Final and clean up =========================== #

	input_file.close()
	output_file.close()


if __name__ == "__main__":
	main(sys.argv[1:])
