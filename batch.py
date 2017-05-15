import os


for i in range(10):
	for j in range(10):
		for k in range(10):
			IR = "python_out_test_%d_%d_%d.out"%(i,j,k)
			os.system("python DataGenMoS2_ForceField.py -x %d -y %d -z %d -g 0 -p 0 -l 0 > %s"%(i,j,k,IR))
			XYZ = "python_out_test_%d_%d_%d.xyz"%(i,j,k)
			os.system("python std_out_to_xyz.py -i %s -o %s"%(IR, XYZ))
