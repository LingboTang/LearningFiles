#!/usr/bin/python

import os
import re
import math
import sys
import getopt
import numpy as np

class idSeq:

	def __init__(self, Id):
		self.id = Id

	def incre(self):
		self.id += 1
		return self.id

	def s_incre(self, step):
		self.id += step
		return self.id


def gap_filter(gap):
	sw = 0
	if type(gap) == int:
		if gap == 0:
			sw = 1
		else:
			sw = 0
		return sw
	elif type(gap) == list:
		if all(item == 0 for item in gap):
			sw = 1
		else:
			sw = 0
		return sw

def seq_incre(i):
	if i == 1:
		return i
	else:
		return i+1


def main(argv):

	dup_x = 2
	dup_y = 2
	dup_z = 2
	x_gap = 0
	y_gap = 0
	z_gap = 0

	try:
		opts,args = getopt.getopt(argv, "hx:y:z:g:p:l:",["dup_x=","dup_y=","dup_z=","xgap=","ygap=","zgap="])
	except getopt.GetoptError:
		print("Usage: DataGenMoS2_ForceField.py -x <dup_x> -y <dup_y> -z <dup_z> -g <xgap> -p <ygap> -l <zgap>")
		sys.exit(0)
	for opt, arg in opts:
		if opt == "-h":
			print("Usage: DataGenMoS2_ForceField.py -x <dup_x> -y <dup_y> -z <dup_z> -g <xgap> -p <ygap> -l <zgap>")
			sys.exit(0)
		elif opt in ("-x", "--dup_x"):
			dup_x = int(arg)
		elif opt in ("-y", "--dup_y"):
			dup_y = int(arg)
		elif opt in ("-z", "--dup_z"):
			dup_z = int(arg)
		elif opt in ("-g", "--xgap"):
			x_gap = int(arg)
		elif opt in ("-p", "--ygap"):
			y_gap = int(arg)
		elif opt in ("-l", "--zgap"):
			z_gap = int(arg)


	a = np.sqrt(3)
	b = 3
	c = 2
	x_box = a*dup_x + x_gap
	y_box = b*dup_y + y_gap
	z_box = 20.1368

	x_sw = gap_filter(x_gap)
	y_sw = gap_filter(y_gap)
	corner_sw = gap_filter([x_gap,y_gap])


	Number_Of_Bonds = -2*dup_x -4*dup_y +12*dup_x*dup_y +2*dup_x*y_sw +4*dup_y*x_sw
	Number_Of_Angles = 7*dup_x*dup_y +14*(dup_x-1)*dup_y +5*dup_x*(dup_y-1) +4*(dup_x-1)*(dup_y-1) +y_sw*(dup_x*5+(dup_x-1)*4) +x_sw*(dup_y*14+(dup_y-1)*4) +corner_sw*4


	print(str(dup_x*dup_y*dup_z*6) + " " + "atoms") 
	print("%d angles"%Number_Of_Angles)
	print("%d bonds"%Number_Of_Bonds)
	print("2 atom types")
	print("3 angle types")
	print("1 bond types")
	print("0.0    %5f xlo xhi"%x_box)
	print("0.0    %5f ylo yhi"%y_box)
	print("0.0    %5f zlo zhi"%z_box)
	print("Masses")
	print("1    95.9400")
	print("2    32.0600")
	print("Atoms")

	ID = idSeq(0)
	for k in range(dup_z):
		for j in range(dup_y):
			for i in range(dup_x):
				print(str(ID.incre()) +" 2 " + str(a/2 + i*a) +" "+ str(0.5 + j*b) + " "+ str(1+k*c) + " 1 "+ " 1 ") 
				print(str(ID.incre()) +" 2 " + str(a/2 + i*a) +" "+ str(0.5 + j*b) + " "+ str(2+k*c) + " 1 "+ " 1 ")
				print(str(ID.incre()) +" 2 " + str(0 + i*a) +" "+ str(2.0 + j*b) + " " + str(1+k*c) + " 1 "+ " 1 ")
				print(str(ID.incre()) +" 2 " + str(0 + i*a) +" "+ str(2.0 + j*b) + " " + str(2+k*c) + " 1 "+ " 1 ")
				print(str(ID.incre()) +" 1 " + str(0 + i*a) +" "+ str(1.0 + j*b) + " " + str(1.5+k*c)+ " 1 "+ " 1 ")
				print(str(ID.incre()) +" 1 " + str(a/2 + i*a) +" "+ str(2.5 + j*b) + " "+ str(1.5+k*c) + " 1 "+ " 1 ")

	print("Bonds")

	ID = idSeq(0)
	for j in range(dup_x*dup_y):
		print(str(ID.incre()) + " 1 " + str(1+6*j) + " " + str(5+6*j) + " #CellIn")
		print(str(ID.incre()) + " 1 " + str(2+6*j) + " " + str(5+6*j) + " #CellIn")
		print(str(ID.incre()) + " 1 " + str(3+6*j) + " " + str(5+6*j) + " #CellIn")
		print(str(ID.incre()) + " 1 " + str(4+6*j) + " " + str(5+6*j) + " #CellIn")
		print(str(ID.incre()) + " 1 " + str(3+6*j) + " " + str(6+6*j) + " #CellIn")
		print(str(ID.incre()) + " 1 " + str(4+6*j) + " " + str(6+6*j) + " #CellIn")

	i = idSeq(0)
	step = idSeq(0)
	for k in range(dup_y):
		for j in range(dup_x-1):
			print(str(ID.incre()) + " 1 " + str(1+ 6*i.id + step.id) + " " + str(11+6*i.id+step.id) +" #CellOutx")
			print(str(ID.incre()) + " 1 " + str(2+ 6*i.id + step.id) + " " + str(11+6*i.id+step.id) +" #CellOutx")
			print(str(ID.incre()) + " 1 " + str(6+ 6*i.id + step.id) + " " + str(9+6*i.id+step.id) +" #CellOutx")
			print(str(ID.incre()) + " 1 " + str(6+ 6*i.id + step.id) + " " + str(10+6*i.id+step.id) +" #CellOutx")
			i.incre()
		step.s_incre(6)

	for j in range((dup_y-1)*dup_x):
		print(str(ID.incre()) + " 1 " + str(6+j*6) +" " + str(6*dup_x+1+j*6) +" #CellOuty")
		print(str(ID.incre()) + " 1 " + str(6+j*6) +" " + str(6*dup_x+2+j*6) +" #CellOuty")

	if y_gap == 0:
		for j in range(dup_x):
			print(str(ID.incre()) + " 1 " + str(1+j*6) + " " + str(dup_x*(dup_y-1)*6+6+j*6) + " #TopBot")
			print(str(ID.incre()) + " 1 " + str(2+j*6) + " " + str(dup_x*(dup_y-1)*6+6+j*6) + " #TopBot")

	if x_gap == 0:
		for j in range(dup_y):
			print(str(ID.incre()) + " 1 " + str(3+j*dup_x*6) + " " + str(dup_x*6 + j*dup_x*6) + " #RightLeft")
			print(str(ID.incre()) + " 1 " + str(4+j*dup_x*6) + " " + str(dup_x*6 + j*dup_x*6) + " #RightLeft")
			print(str(ID.incre()) + " 1 " + str(5+j*dup_x*6) + " " + str(dup_x*6 -5 + j*dup_x*6) + " #RightLeft")
			print(str(ID.incre()) + " 1 " + str(5+j*dup_x*6) + " " + str(dup_x*6 -4 + j*dup_x*6) + " #RightLeft")

	print("Angles")

	ID = idSeq(0)
	for j in range(dup_x*dup_y):
		print(str(ID.incre()) + " 1 " + str(1+j*6) +" "+ str(5+j*6) + " " + str(2+j*6) +" #A1_Theta")
		print(str(ID.incre()) + " 1 " + str(3+j*6) +" "+ str(5+j*6) + " " + str(4+j*6) +" #A1_Theta")
		print(str(ID.incre()) + " 1 " + str(3+j*6) +" "+ str(6+j*6) + " " + str(4+j*6) +" #A1_Theta")
		print(str(ID.incre()) + " 2 " + str(1+j*6) +" "+ str(5+j*6) + " " + str(3+j*6) +" #A1_phi")
		print(str(ID.incre()) + " 2 " + str(2+j*6) +" "+ str(5+j*6) + " " + str(4+j*6) +" #A1_phi")
		print(str(ID.incre()) + " 3 " + str(5+j*6) +" "+ str(3+j*6) + " " + str(6+j*6) +" #A1_psi")
		print(str(ID.incre()) + " 3 " + str(5+j*6) +" "+ str(4+j*6) + " " + str(6+j*6) +" #A1_psi")

	i = idSeq(0)
	step = idSeq(0)
	for k in range(dup_y):
		for j in range(dup_x-1):
			print(str(ID.incre()) + " 1 " + str(1+i.id*6 +step.id) + " " + str(11+i.id*6+step.id) + " "+ str(2+i.id*6+step.id) + " #A2_theta")
			print(str(ID.incre()) + " 1 " + str(9+i.id*6 +step.id) + " " + str(6+i.id*6+step.id) + " "+ str(10+i.id*6+step.id) + " #A2_theta")
			print(str(ID.incre()) + " 2 " + str(1+i.id*6 +step.id) + " " + str(11+i.id*6+step.id) + " "+ str(7+i.id*6+step.id) + " #A2_phi")
			print(str(ID.incre()) + " 2 " + str(2+i.id*6 +step.id) + " " + str(11+i.id*6+step.id) + " "+ str(8+i.id*6+step.id) + " #A2_phi")
			print(str(ID.incre()) + " 2 " + str(1+i.id*6 +step.id) + " " + str(11+i.id*6+step.id) + " "+ str(9+i.id*6+step.id) + " #A2_phi")
			print(str(ID.incre()) + " 2 " + str(2+i.id*6 +step.id) + " " + str(11+i.id*6+step.id) + " "+ str(10+i.id*6+step.id) + " #A2_phi")
			print(str(ID.incre()) + " 2 " + str(3+i.id*6 +step.id) + " " + str(6+i.id*6+step.id) + " "+ str(9+i.id*6+step.id) + " #A2_phi")
			print(str(ID.incre()) + " 2 " + str(4+i.id*6 +step.id) + " " + str(6+i.id*6+step.id) + " "+ str(10+i.id*6+step.id) + " #A2_phi")
			print(str(ID.incre()) + " 3 " + str(5+i.id*6 +step.id) + " " + str(1+i.id*6+step.id) + " "+ str(11+i.id*6+step.id) + " #A2_psi")
			print(str(ID.incre()) + " 3 " + str(5+i.id*6 +step.id) + " " + str(2+i.id*6+step.id) + " "+ str(12+i.id*6+step.id) + " #A2_psi")
			print(str(ID.incre()) + " 3 " + str(3+i.id*6 +step.id) + " " + str(6+i.id*6+step.id) + " "+ str(9+i.id*6+step.id) + " #A2_psi")
			print(str(ID.incre()) + " 3 " + str(4+i.id*6 +step.id) + " " + str(6+i.id*6+step.id) + " "+ str(10+i.id*6+step.id) + " #A2_psi")
			print(str(ID.incre()) + " 3 " + str(6+i.id*6 +step.id) + " " + str(9+i.id*6+step.id) + " "+ str(12+i.id*6+step.id) + " #A2_psi")
			print(str(ID.incre()) + " 3 " + str(6+i.id*6 +step.id) + " " + str(10+i.id*6+step.id) + " "+ str(12+i.id*6+step.id) + " #A2_psi")
			i.incre()
		step.s_incre(6)

	for j in range(dup_x*(dup_y-1)):
		print(str(ID.incre()) + " 1 " + str(6*dup_x+1+j*6) +" " + str(6+j*6) + " "+ str(6*dup_x+2+j*6) + " #B1_Theta")
		print(str(ID.incre()) + " 2 " + str(3+j*6) +" " + str(6+j*6) + " "+ str(6*dup_x+1+j*6) + " #B1_phi")
		print(str(ID.incre()) + " 2 " + str(4+j*6) +" " + str(6+j*6) + " "+ str(6*dup_x+2+j*6) + " #B1_phi")
		print(str(ID.incre()) + " 3 " + str(6+j*6) +" " + str(6*dup_x+1+j*6) + " "+ str(6*dup_x+5+j*6) + " #B1_psi")
		print(str(ID.incre()) + " 3 " + str(6+j*6) +" " + str(6*dup_x+2+j*6) + " "+ str(6*dup_x+5+j*6) + " #B1_psi")

	i = idSeq(0)
	step = idSeq(0)
	for k in range(dup_y-1):
		for j in range(dup_x-1):
			print(str(ID.incre()) + " 2 " + str(9+i.id*6+step.id) + " " + str(6+i.id*6+step.id) +" " + str(6*dup_x+1+i.id*6+step.id) + " #b2_phi")
			print(str(ID.incre()) + " 2 " + str(10+i.id*6+step.id) + " " + str(6+i.id*6+step.id) +" " + str(6*dup_x+2+i.id*6+step.id) + " #b2_phi")
			print(str(ID.incre()) + " 3 " + str(6+i.id*6+step.id) + " " + str(6*dup_x+1+i.id*6+step.id) +" " + str(6*dup_x+11+i.id*6+step.id) + " #b2_psi")
			print(str(ID.incre()) + " 3 " + str(6+i.id*6+step.id) + " " + str(6*dup_x+2+i.id*6+step.id) +" " + str(6*dup_x+11+i.id*6+step.id) + " #b2_psi")
			i.incre()
		step.s_incre(6)

	if (y_gap == 0):
		for j in range(dup_x):
			print(str(ID.incre()) + " 1 " + str(1+j*6) +" "+str(dup_x*(dup_y-1)*6+6+j*6) + " " + str(2+j*6) + " #TB1_Theta")
			print(str(ID.incre()) + " 2 " + str(1+j*6) +" "+str(dup_x*(dup_y-1)*6+6+j*6) + " " + str(dup_x*(dup_y-1)*6+3+j*6) + " #TB1_phi")
			print(str(ID.incre()) + " 2 " + str(2+j*6) +" "+str(dup_x*(dup_y-1)*6+6+j*6) + " " + str(dup_x*(dup_y-1)*6+4+j*6) + " #TB1_phi")
			print(str(ID.incre()) + " 3 " + str(5+j*6) +" "+str(1+j*6) + " " + str(dup_x*(dup_y-1)*6+6+j*6) + " #TB1_psi")
			print(str(ID.incre()) + " 3 " + str(5+j*6) +" "+str(2+j*6) + " " + str(dup_x*(dup_y-1)*6+6+j*6) + " #TB1_psi")

		for j in range(dup_x-1):
			print(str(ID.incre()) + " 2 " + str(1+j*6) +" "+str(dup_x*(dup_y-1)*6+6+j*6) + " " + str(dup_x*(dup_y-1)*6+9+j*6) + " #TB2_phi")
			print(str(ID.incre()) + " 2 " + str(1+j*6) +" "+str(dup_x*(dup_y-1)*6+6+j*6) + " " + str(dup_x*(dup_y-1)*6+10+j*6) + " #TB2_phi")
			print(str(ID.incre()) + " 3 " + str(11+j*6) +" "+str(1+j*6) + " " + str(dup_x*(dup_y-1)*6+6+j*6) + " #TB2_psi")
			print(str(ID.incre()) + " 3 " + str(11+j*6) +" "+str(2+j*6) + " " + str(dup_x*(dup_y-1)*6+6+j*6) + " #TB2_psi")

	if (x_gap == 0):
		for j in range(dup_y):
			print(str(ID.incre()) + " 1 " + str((dup_x-1)*6+1+j*dup_x*6) + " " +str(5+j*dup_x*6) + " " + str((dup_x-1)*6+2+j*dup_x*6) + " #RL1_Theta")
			print(str(ID.incre()) + " 1 " + str(3+j*dup_x*6) + " " +str((dup_x-1)*6+6+j*dup_x*6) + " " + str(4+j*dup_x*6) + " #RL1_Theta")
			print(str(ID.incre()) + " 2 " + str((dup_x-1)*6+1+j*dup_x*6) + " " +str(5+j*dup_x*6) + " " + str(1+j*dup_x*6) + " #RL1_phi")
			print(str(ID.incre()) + " 2 " + str((dup_x-1)*6+2+j*dup_x*6) + " " +str(5+j*dup_x*6) + " " + str(2+j*dup_x*6) + " #RL1_phi")
			print(str(ID.incre()) + " 2 " + str((dup_x-1)*6+1+j*dup_x*6) + " " +str(5+j*dup_x*6) + " " + str(3+j*dup_x*6) + " #RL1_phi")
			print(str(ID.incre()) + " 2 " + str((dup_x-1)*6+2+j*dup_x*6) + " " +str(5+j*dup_x*6) + " " + str(4+j*dup_x*6) + " #RL1_phi")
			print(str(ID.incre()) + " 2 " + str((dup_x-1)*6+3+j*dup_x*6) + " " +str((dup_x-1)*6+6+j*dup_x*6) + " " + str(3+j*dup_x*6) + " #RL1_phi")
			print(str(ID.incre()) + " 2 " + str((dup_x-1)*6+4+j*dup_x*6) + " " +str((dup_x-1)*6+6+j*dup_x*6) + " " + str(4+j*dup_x*6) + " #RL1_phi")
			print(str(ID.incre()) + " 3 " + str((dup_x-1)*6+5+j*dup_x*6) + " " +str((dup_x-1)*6+1+j*dup_x*6) + " " + str(5+j*dup_x*6) + " #RL1_psi")
			print(str(ID.incre()) + " 3 " + str((dup_x-1)*6+5+j*dup_x*6) + " " +str((dup_x-1)*6+2+j*dup_x*6) + " " + str(5+j*dup_x*6) + " #RL1_psi")
			print(str(ID.incre()) + " 2 " + str((dup_x-1)*6+6+j*dup_x*6) + " " +str(3+j*dup_x*6) + " " + str(6+j*dup_x*6) + " #RL1_psi")
			print(str(ID.incre()) + " 2 " + str((dup_x-1)*6+6+j*dup_x*6) + " " +str(4+j*dup_x*6) + " " + str(6+j*dup_x*6) + " #RL1_psi")
			print(str(ID.incre()) + " 2 " + str((dup_x-1)*6+6+j*dup_x*6) + " " +str(3+j*dup_x*6) + " " + str(5+j*dup_x*6) + " #RL1_psi")
			print(str(ID.incre()) + " 2 " + str((dup_x-1)*6+6+j*dup_x*6) + " " +str(4+j*dup_x*6) + " " + str(5+j*dup_x*6) + " #RL1_psi")

		for j in range(dup_y-1):
			print(str(ID.incre()) + " 2 " + str(3+j*dup_x*6) + " " +str((dup_x-1)*6+6+j*dup_x*6) + " " + str((dup_x-1)*6+1+(j+1)*dup_x*6) + " #RL2_phi")
			print(str(ID.incre()) + " 2 " + str(4+j*dup_x*6) + " " +str((dup_x-1)*6+6+j*dup_x*6) + " " + str((dup_x-1)*6+1+(j+1)*dup_x*6) + " #RL2_phi")
			print(str(ID.incre()) + " 3 " + str((dup_x-1)*6+6+j*dup_x*6) + " " +str((dup_x-1)*6+1+(j+1)*dup_x*6) + " " + str(5+(j+1)*dup_x*6) + " #RL2_psi")
			print(str(ID.incre()) + " 3 " + str((dup_x-1)*6+6+j*dup_x*6) + " " +str((dup_x-1)*6+2+(j+1)*dup_x*6) + " " + str(5+(j+1)*dup_x*6) + " #RL2_psi")

	if (x_gap == 0 and y_gap == 0):
		print(str(ID.incre()) + " 2 " + "5 " + str((dup_x-1)*6+1) + " " + str(dup_x*dup_y*6) +" #Corner_phi")
		print(str(ID.incre()) + " 2 " + "5 " + str((dup_x-1)*6+2) + " " + str(dup_x*dup_y*6) +" #Corner_phi")
		print(str(ID.incre()) + " 3 " + str((dup_x-1)*6+1) + " " + str(dup_x*dup_y*6) + " " + str(3+dup_x*(dup_y-1)*6) +" #Corner_psi")
		print(str(ID.incre()) + " 3 " + str((dup_x-1)*6+2) + " " + str(dup_x*dup_y*6) + " " + str(4+dup_x*(dup_y-1)*6) +" #Corner_psi")


if __name__ == "__main__":
	main(sys.argv[1:])