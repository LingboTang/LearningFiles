from multiprocessing.dummy import Pool as ThreadPool
import os
import time 

sub_paths = ("/out_move/", "/out_rotate/")

outpaths = [os.getcwd() + sub_path for sub_path in sub_paths]
for out_path in outpaths:
	os.system("rm -rf %s"%out_path)
	if not os.path.exists(out_path):
		os.makedirs(out_path)


exec_lines = ["python2 -OO batch_exec.py -s 2 -t 1 -r 1 -m 0 -a 0 -f 4 -d 3 -u 30 -n 5",\
			"python2 -OO batch_exec.py -s 2 -t 1 -r 1 -m 0 -a 1 -f 4 -d 3 -u 30 -n 5",\
			"python2 -OO batch_exec.py -s 2 -t 1 -r 1 -m 0 -a 2 -f 4 -d 3 -u 30 -n 5",\
			"python2 -OO batch_exec.py -s 2 -t 1 -r 0 -m 1 -a 0 -f 4 -d 3 -u 30 -n 5",\
			"python2 -OO batch_exec.py -s 2 -t 1 -r 0 -m 1 -a 1 -f 4 -d 3 -u 30 -n 5"]


pool = ThreadPool(5)

results = pool.map(os.system, exec_lines)
pool.close()
pool.join()