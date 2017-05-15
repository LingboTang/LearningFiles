#!/bin/bash

batch_x=10
batch_y=10
batch_z=10

for k in $(seq 0 $batch_z)
	do
	for j in $(seq 0 $batch_y)
		do
		for i in $(seq 0 $batch_x)
			do
			test_ir="python_out_test_${i}_${j}_${k}.out"
			test_xyz="python_out_test_${i}_${j}_${k}.xyz"
			python DataGenMoS2_ForceField.py -x $i -y $j -z $k -g 0 -p 0 -l 0 > $test_ir
			python std_out_to_xyz.py -i $test_ir -o $test_xyz
			done
		done
	done
