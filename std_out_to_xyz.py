import re
import sys
import os
import getopt


def main(argv):
	input_f_name = ""
	output_f_name = ""
	Sulphur = "S"
	Mo = "Mo"

	try:
		opts,args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print("Usage: std_out_to_xyz.py -i <ifile> -o <ofile>")
		sys.exit(0)
	for opt, arg in opts:
		if opt == "-h":
			print("Usage: std_out_to_xyz.py -i <ifile> -o <ofile>")
			sys.exit(0)
		elif opt in ("-i", "--ifile"):
			input_f_name = arg
		elif opt in ("-o", "--ofile"):
			output_f_name = arg


	try:
		input_file = open(input_f_name, "r")
	except IOError:
		print("Can't open inputfile or inputfile does not exist: ", input_f_name)
		sys.exit(1)

	try:
		output_file = open(output_f_name, "w")
	except IOError:
		print("Can't open inputfile or inputfile does not exist: ", output_f_name)
		sys.exit(1)

	data = []
	for line in input_file:
		if len(line.strip()) == 0:
			continue
		else:
			data.append(line.strip().split())

	del data[data.index(["Bonds"]): ]
	for my_line in data:
		if "atoms" in my_line:
			output_file.write(my_line[0] + "\n")
			output_file.write("molybdinum-disulfide"+"\n")
		elif data.index(my_line) <= data.index(["Atoms"]):
			continue
		else:
			outstring = ""
			if my_line[1] == "1":
				outstring = Mo+" "+my_line[2]+" "+my_line[3]+" "+my_line[4]+ "\n"
			else:
				outstring = Sulphur+" "+my_line[2]+" "+my_line[3]+" "+my_line[4]+ "\n"
			output_file.write(outstring)


	input_file.close()
	output_file.close()	

if __name__ == "__main__":
	main(sys.argv[1:])
