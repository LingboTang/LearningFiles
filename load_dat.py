import os
import sys
import re
import numpy as np
import random
import getopt
import time
import matplotlib.pyplot as plt
from scipy.interpolate import splrep, splev, spline, interp1d
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
colors = ["b","g","r","y","k"] * 2 

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
	Fexp = []
	F1 = []
	F2 = []
	texp = 0
	t1 = 0
	t2 = 0
	for i in range(len(works)):
		w = works[i]
		texp = texp + np.exp(-works[i] * beta)
		t1 = t1 + works[i]
		t2 = t2 + works[i] ** 2
		Fexp.append(- 1/beta * np.log(texp / 10))
		F1.append(t1 / 10)
		F2.append(t1 / 10 - t2 / 10 + t1 * t1 /100)
	Fexp = np.array(Fexp)
	F1 = np.array(F1)
	F2 = np.array(F2)
	return [Fexp,F1,F2]




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
		print("Usage: load_dat.py -i <ifile> -k <kelvin> -v <velocity>")
		sys.exit(0)

	for opt, arg in opts:
		if opt == "-h":
			print("Usage: load_dat.py -i <ifile> -k <kelvin> -v <velocity>")
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
	trajactories = [data_lines[:,col] for col in range(num_trails + 1) if col != 0]
	forces = [data_lines[:,col] for col in range(num_trails + 1, last_column)]

	# Works
	all_works_1 = []
	for i in range(num_trails):
		delta_distances = get_delta_dis(trajactories[i])
		ave_Fs = get_ave_forces(forces[i])
		work_of_each_traj = calculate_work(delta_distances, ave_Fs)
		all_works_1.append(work_of_each_traj)
	all_works_1 = np.array(all_works_1)

	# Method 1
	all_FEs = []
	for i in range(num_trails):
		FEs = jarzynski_equality_simul_1(all_works_1[i], Beta(KB,kelvin))
		all_FEs.append(FEs)
	all_FEs = np.array(all_FEs) 
	
	# Method 2
	all_FEs_2 = jarzynski_equality_simul_2(all_works_1[0], Beta(KB,kelvin))
	#for i in range(num_trails):
	#	FE2s = jarzynski_equality_simul_2(all_works_1[i], Beta(KB,kelvin))
	#	all_FEs_2.append

	'''ploting_vs = []
	for i in range(len(trajactories[0])):
		ploting_vs.append(np.array([trajactories[0][i], all_works_1[0][i]]))
	ploting_vs.sort(key=lambda pair: pair[0])
	ploting_vs = np.array(ploting_vs)'''

	'''for i in range(len(all_works_1[0])):
		line = str(trajactories[0][i]) + "      " + str(all_works_1[0][i]) + "\n"
		output_file.write(line)'''

	for i in range(len(all_works_1[0])):
		row_string = "%.6f"%trajactories[0][i]
		for j in range(num_trails):
			this_value = "%.6f"%all_works_1[j][i]
			row_string = row_string + "    " + this_value.rjust(4)
		row_string = row_string + "\n"
		output_file.write(row_string)



	# ====================== Plot the graphs ============================== #

	#x = trajactories[0]
	#y = all_works_1[0]
	#print(x.min())
	#print(x.max())
	#x_smooth = np.linspace(x.min(),x.max(), 10)
	#print(x_smooth)
	#try:
	#	with Timeout(3):
	#		y_smooth = spline(x, y, x_smooth)
	#except Timeout.Timeout:
	#	print("Timeout!")
	#	input_file.close()
	#	sys.exit(3)
	


	'''x = trajactories[0]
	y = all_works_1[0]

	sort_idx = np.argsort(x)
	x_sorted = x[sort_idx]
	y_sorted = y[sort_idx]
	

	order = 2
	spline = Bspline(x_sorted, y_sorted, order)
	y_smooth = spline(x_smooth)'''

	x = np.array([13.202, 13.234738, 12.999116,\
		12.86252,13.1157,13.357109,13.234004,\
		12.836279, 12.851597,13.110691])

	y = np.array([0.0, -0.051354,0.144464,\
		0.073965, 0.100197,-0.302885,\
		-0.045792, 0.036225,0.054264,0.105293])

	sort_idx = np.argsort(x)
	x_sorted = x[sort_idx]
	y_sorted = y[sort_idx]

	print(x_sorted)
	print(y_sorted)
	plt.figure(1)
	plt.plot(x_sorted, y_sorted, ".")
	plt.show()

	'''plt.figure(1)
	plt.plot(trajactories[0], all_works_1[0], "k")
	plt.show()
	plt.close()

	plt.figure(2)
	plt.plot(time_series, trajactories[0], "ro")
	plt.show()
	plt.close()

	plt.figure(3)
	plt.plot(time_series, forces[0], "go")
	plt.show()
	plt.close()

	plt.figure(4)
	plt.plot(trajactories[0], forces[0], "ko")
	plt.show()
	plt.close()

	plt.figure(5)
	plt.plot(trajactories[0], all_FEs[0], "b")
	plt.show()
	plt.close()

	plt.figure(6)
	plt.plot(trajactories[0],all_FEs_2[0],"bo")
	plt.show()
	plt.close()'''


	# ====================== Final and clean up =========================== #

	input_file.close()
	output_file.close()


if __name__ == "__main__":
	main(sys.argv[1:])
