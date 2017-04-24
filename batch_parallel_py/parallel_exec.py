from multiprocessing.dummy import Pool as ThreadPool
import os
import time 

sub_paths = ("/out_strand_rotate_0_move_0/","/out_strand_rotate_1_move_0/",\
			"/out_strand_rotate_0_move_1/","/out_strand_rotate_1_move_1/",\
			"/out_strand_rotate_0/","/out_strand_rotate_1/","/out_strand_rotate_2/",\
			"/out_strand_move_0/", "/out_strand_move_1/")

outpaths = [os.getcwd() + sub_path for sub_path in sub_paths]
for out_path in outpaths:
	os.system("rm -rf %s"%out_path)
	if not os.path.exists(out_path):
		os.makedirs(out_path)

#time.sleep(0.1)

exec_lines = ["python batch_exec.py -s 2 -t 1 -r 1 -m 0 -a 0",\
			"python batch_exec.py -s 2 -t 1 -r 1 -m 0 -a 1",\
			"python batch_exec.py -s 2 -t 1 -r 1 -m 0 -a 2",\
			"python batch_exec.py -s 2 -t 1 -r 0 -m 1 -a 0",\
			"python batch_exec.py -s 2 -t 1 -r 0 -m 1 -a 1"]


pool = ThreadPool(5)

results = pool.map(os.system, exec_lines)
pool.close()
pool.join() 