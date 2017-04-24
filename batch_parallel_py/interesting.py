import time
import os

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'

	def disable(self):
		self.HEADER = ''
		self.OKBLUE = ''
		self.OKGREEN = ''
		self.WARNING = ''
		self.FAIL = ''
		self.ENDC = ''

def main():
	step_indicator = ""
	arrow = bcolors.FAIL+">>"+bcolors.ENDC
	for step in range(0,10000,100):
		step_percentage = float(step)/10000.0 * 100
		step_str = "%.2f"%step_percentage
		step_str = bcolors.WARNING + step_str+"%"+ bcolors.ENDC
		if step % 300 == 0:
			step_indicator += "="
		print("step_percentage: %s%s%s" % (bcolors.OKBLUE+step_indicator+bcolors.ENDC,arrow, step_str))
		time.sleep(0.05)
		os.system("clear")
	print("Completed!")

main()