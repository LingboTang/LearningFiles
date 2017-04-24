#!/usr/bin/python

import re
import os
import sys
import math
import numpy as np
import getopt

# ===================================== Util Functions ============================== #

def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = np.asarray(axis)
    axis = axis/math.sqrt(np.dot(axis, axis))
    a = math.cos(theta/2.0)
    b, c, d = -axis*math.sin(theta/2.0)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
    return np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
                     [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
                     [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])


def calc_euclidean_distance(p1, p2):
	return math.sqrt((p2.x - p1.x) **2 + (p2.y - p1.y) **2 + (p2.z - p1.z) **2)


def toRadians(degrees):
	return degrees * math.pi / 180


def vector_move(point, dire, dis):
	base_point = np.array(point)
	base_dir = np.array(dire)
	new_point = base_point + dis*base_dir
	return new_point


# Set one of the strand static, and rotate the other strand
def rotating_around_strand_axis(strand_op, static_axis, theta, out_coords, in_coords):
	if strand_op == 0:
		new_strand = []
		for coordinate in in_coords[strand_op]:
			new_strand.append(tuple(np.dot(rotation_matrix(static_axis,theta),coordinate)))
		out_coords.append(new_strand)
		out_coords.append(in_coords[1])
	elif strand_op == 1:
		new_strand = []
		out_coords.append(in_coords[0])
		for coordinate in in_coords[strand_op]:
			new_strand.append(tuple(np.dot(rotation_matrix(static_axis,theta),coordinate)))
		out_coords.append(new_strand)
	elif strand_op == 2:
		new_strand = []
		for point in in_coords[0]:
			new_strand.append(tuple(np.dot(rotation_matrix(static_axis,theta),point)))
		out_coords.append(new_strand)
		new_strand = []
		for point in in_coords[1]:
			new_strand.append(tuple(np.dot(rotation_matrix(static_axis, -theta),point)))
		out_coords.append(new_strand)
	else:
		out_coords = in_coords
	return out_coords

def normalize_vector(vec):
	norm = math.sqrt(vec[0] ** 2 + vec[1] ** 2 + vec[2] ** 2)
	vec = (vec[0]/norm, vec[1]/norm, vec[2]/norm)
	return vec


def flatten_strand(array):
	flattened = []
	for strand in array:
		for item in strand:
			flattened.append(item)
	return flattened


def ceiling_to_three_digs(line, new_data):
	for i in range(len(line)):
		for j in range(3):
			line[i][j+5] = str(math.ceil(new_data[i][j] * 1000) / 1000.0)
	line.insert(len(line)//2,["TER"])
	line.append(["TER"])
	line.append(["END"])


def output_files_in_format(outlines,outfile):
	for outline in outlines:
		if len(outline) > 1:
			atom_group = outline[2]
			if len(atom_group) == 1:
				outline2 = " "+atom_group+"  "
			elif len(atom_group) == 2:
				outline2 = " "+atom_group+" "
			elif len(atom_group) == 3:
				outline2 = " "+atom_group
			else:
				outline2 = atom_group
			formatted = outline[0]+outline[1].rjust(7)+outline2.rjust(5)+\
						outline[3].rjust(4)+outline[4].rjust(6)+outline[5].rjust(12)+\
						outline[6].rjust(8)+outline[7].rjust(8)+outline[8].rjust(6)+\
						outline[9].rjust(6)
			outfile.write(formatted+"\n")
		else:
			outfile.write(outline[0]+"\n")



def main(argv):

	# Global Settings
	inputfN = ""
	rotating_theta = 0.0
	translation = 0
	strand_axis = []
	moving_axis = []

	# ======================================= Parsing ===================================================== #

	# Pre-processing pass given input and output files
	try:
		opts, args = getopt.getopt(argv, "hi:o:a:c:s:m:t:", ["ifile=","ofile=","axis=","change=","step=","movestrand=","translation="])
	except getopt.GetoptError:
		print("myParsePDB.py -i <inputfile> -o <outputfile> -a <axis> -c <change_distance> -s <step> -m <movestrand> -t <translation>")
		sys.exit(2)
	for opt, arg in opts:
		if opt == "-h":
			print("myParsePDB.py -i <inputfile> -o <outputfile> -a <axis> -c <change_distance> -s <step> -m <movestrand> -t <translation>")
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfN = arg
		elif opt in ("-o", "--ofile"):
			outputN = arg
		elif opt in ("-a", "--axis"):
			strand_op = int(arg)
		elif opt in ("-c", "--change"):
			delta_dis = float(arg)
		elif opt in ("-s","--step"):
			rotating_theta = float(arg)
			rotating_theta = toRadians(rotating_theta)
		elif opt in ("-m", "--movestrand"):
			movestrand = int(arg)
		elif opt in ("-t", "--translation"):
			translation = float(arg)
	

	# Open the input and output files, if they are not exist or due to access reason
	# Throw the IOERROR and Leave
	try:
		inputFile = open(inputfN, "r")
	except IOError:
		print("Can't open inputfile or inputfile does not exist: ", inputfN)
		sys.exit(0)


	# Open the output files in a new output folder and 
	# Store all file names in a list for batch processing
	try:
		myOF = open(outputN, "w")
	except IOError:
		print("Error Creating file!")
		sys.exit(1)


	#==========================================Getting==================================#

	# Get the each line data
	strand = []
	strands = []
	outlines = []
	for line in inputFile:
		line = line.strip()
		if line.startswith("TER"):
			line = line.split()
			strands.append(strand)
			strand = []
		elif line.startswith("END"):
			line = line.split()
			break
		else:
			line = line.split()
			outlines.append(line)
			keyPair = {}
			keyPair["Residue_Num"] = int(line[4])
			keyPair["Atom"] = line[2]
			keyPair["Atom_Coord"] = (float(line[5]),float(line[6]),float(line[7]))
			strand.append(keyPair)

	medians =[]
	for strand in strands:
		strand_median = (strand[0]["Residue_Num"]+strand[-1]["Residue_Num"] -1)/2
		medians.append(strand_median)


	# Calculate the distance between median CA
	main_edges = []
	for i in range(len(strands)):
		main_edge = [x["Atom_Coord"] for x in strands[i] if x["Atom"] == "CA"]
		main_edges.append(main_edge)

	# Calculate the strand axis using the start and end Carbon Alpha
	start_point_0 = main_edges[0][0]
	end_point_0 = main_edges[0][1]
	start_point_1 = main_edges[1][1]
	end_point_1 = main_edges[1][0]
	strand_axis = [tuple(np.array(end_point_0) - np.array(start_point_0)),tuple(np.array(end_point_1)-np.array(start_point_1))]


	# Because our axis is not accurately initialized, we also need to store the Central Index
	# for the final adjustment (When you rotate, your central vector changed)
	filtered_strands = []
	stored_indexs = []
	for i in range(len(strands)):
		filtered_strand = [x["Atom_Coord"] for x in strands[i] if x["Residue_Num"] == medians[i] and x["Atom"] == "CA"]
		stored_index = [strands[i].index(x) for x in strands[i] if x["Residue_Num"] == medians[i] and x["Atom"] == "CA"]
		stored_indexs.append(stored_index[0])
		filtered_strands.append(filtered_strand)


	central_vector = (filtered_strands[0][0][0] - filtered_strands[1][0][0],
						filtered_strands[0][0][1] - filtered_strands[1][0][1],
						filtered_strands[0][0][2] - filtered_strands[1][0][2])

	central_norm = math.sqrt(central_vector[0] ** 2 + central_vector[1] ** 2 + central_vector[2] ** 2)
	normalized_vector = (central_vector[0]/central_norm,
						central_vector[1]/central_norm,
						central_vector[2]/central_norm)

	# Calculate the original distance
	for i in range(len(filtered_strands[0])):
		origin_dis = np.linalg.norm(np.array(filtered_strands[0][i]) - np.array(filtered_strands[1][i]))

	#=================================== Setting =====================================================#

	# Rotate the entire strand around standard axis in Cartesian Coordinates
	#
	Coordinates = []
	for i in range(len(strands)):
		Coordinate = [x["Atom_Coord"] for x in strands[i]]
		Coordinates.append(Coordinate)


	# Move the second strand by a certain distance
	#for i in range(len(Coordinates[1])):
	#	Coordinates[1][i] = tuple(vector_move(Coordinates[1][i], normalized_vector, delta_dis))

	start_mid = tuple((np.array(start_point_0) + np.array(start_point_1))/2)
	end_mid = tuple((np.array(end_point_0) + np.array(end_point_1))/2)
	mid_rotation_axis = np.array(end_mid) - np.array(start_mid)
	mid_rotation_axis = normalize_vector(mid_rotation_axis)

	outCoords = []
	#outCoords = Coordinates
	outCoords = rotating_around_strand_axis(strand_op, mid_rotation_axis, rotating_theta, outCoords, Coordinates)
	if movestrand not in (0,1):
		pass
	else:
		for i in range(len(outCoords[movestrand])):
			outCoords[movestrand][i] = tuple(vector_move(outCoords[movestrand][i],strand_axis[movestrand], translation))


	# Final Adjustment for rotations
	if movestrand not in(0,1):
		adjusting_center_0 = outCoords[0][stored_indexs[0]]
		adjusting_center_1 = outCoords[1][stored_indexs[1]]
		adjusting_vec = tuple(np.array(adjusting_center_0)-np.array(adjusting_center_1))
		adjusting_norm_vec = normalize_vector(adjusting_vec)
		end_dis = np.linalg.norm(np.array(adjusting_center_0) - np.array(adjusting_center_1))
		changed_dis = origin_dis-end_dis
		if (strand_op == 0):
			for i in range(len(outCoords[0])):
				outCoords[0][i] = tuple(vector_move(outCoords[0][i], adjusting_norm_vec, changed_dis))
		else:
			for i in range(len(outCoords[1])):
				outCoords[1][i] = tuple(vector_move(outCoords[1][i], adjusting_norm_vec, -changed_dis))


	# Finish and clean up
	inputFile.close()
	outCoords = flatten_strand(outCoords)
	ceiling_to_three_digs(outlines, outCoords)
	output_files_in_format(outlines,myOF)
	myOF.close()

	
if __name__ == "__main__":
	main(sys.argv[1:])
