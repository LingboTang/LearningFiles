PDB Processing Files
====================

**This package would require numpy package**

1. **parallel_exec.py:**
   
   * This file contains a list of all command lines to execute **batch_exec.py** and a tuple of all separate output directory.
   
   * Each command line will be executed in different thread, they share one input reading file, but they will write output files in different directory, so multi-threading in this file is thread safe. If you want to change the number of threads that you are using in this file. Go to the line which contains `pool =  ThreadPool(num_of_thread)` to change thee value of `num_of_thread`. Dynamic threading is a different story, but this simple static threading is enough to boost up the performance.
   
   * The output directory will be in the format of `/out_move/` or `/out_rotate/`
   
   * The batch_exec.py can take plenty of options in command line as input, which gives you the flexibility to vary and alternate your parameters
   
   Now I will explain what you can change in this file to make your automation work robustly:
   
    * The `-s` or `--angleStep` is used for controlling the step size change of rotating angle, make sure the input unit is "degrees", but it will be convert to "radians" when doing calculation, so you don't need to worry about the unit change.
    
    * The "-t" or `--transStep` is used for controlling the step size change of the parallel moving for each strand, make sure the input is A.
    
    * The `-r` or `--rotatable` is used for determining if the molecule is rotatable or not. 
      
        * `0`: disabled
        
        * `1`: enabled
    
    * The `-m` or `--movable` is used for determining if the molecule strand is movable along its strand axis or not.
    
        * `0`: disabled
        
        * `1`: enabled
    
    * The `-a` or `--strand` is used for determining which strand is going to be processed.
    
        * `0`: process the first strand
        
        * `1`: process the second strand
        
        * `number_of_folds * 2`: process **all** strand

    * The `-f` or `--fold` is used for determining how many folds do we want to create from the original file.

        * `1`: One fold (original strands)

        * `2`: Two fold

    * The `-d` or `--inidis` is used for determining how much distance we want to move for each new folds

        * `3`: 3 unit

    * The `-u` or `--angleupper` is the upper bound of rotating angle you want to set for experiment

        * `30`: 30 degrees

    * The `-n` or `--transupper` is the upper bound of translation distance you want to set for experiment

        * `5`: 5 unit


    * I suggest you use less than 8 folds because the memory will expand 2 times after you create more folds.
        
    * It will delete and re-generate the legacy output directories at the start of the file for avoiding disk space overflow.
        
    **This script will force you to use the default options when you passed in invalid input.**
    
    **Usage Command Line Example:**
    
    `python2 -OO parallel_exec.py`

    `python2 -OO batch_exec.py -s 2 -t 1 -r 1 -m 0 -a 0 -f 4 -d 3 -u 30 -n 5`, now I locked python interpreter to python2, `-OO` is for compiler optimization.
   
2. **batch_exec.py:**

    This script will execute the main part of this package `myParsePDB.py`. It will take the input from `parallel_exec.py` and then it will pass the options to execute `myParsePDB.py` depends on the options passed in by `parallel_exec.py`. The output files are generated under each separated output directory. Because the generating process is running in loops (lower_bound, upper_bound, stepsize), each output file will contain the info only for that step. So the output file has a format: `<input_file_name>_OUT_Rotate_Angle_<angle>_strand_<strand>.pdb` or `<input_file_name>_OUT_Move_Trans_<translation>_strand_<strand>.pdb`.
    
    Now, I'll explain how to set the options if you want to change the command lines here:
    
    * The `-i` or `--ifile` will take the input file
    
    * The `-o` or `--ofile` will specify which output file it will write to.
    
    * The `-a` or `--axis` will specify which strand you want to process
    
      * `0`: first strand
      
      * `1`: second strand
      
      * `number_of_folds * 2`: all strands
      
      * `number_of_folds * 2 + 1`: None
    
    * The `-s` or `--step` will specify the exact step value to rotate (not step size), note this `-s` is distinct from the `-s` above.
    
    * The `-m` or `--movestrand` will specify which strand you want to move
    
      * `0`: first strand
      
      * `1`: second strand

      * `number_of_folds * 2`: none
      
    * The `-t` or `--translation` will specify the exact step value to translate along strand axis (notrstep size), note this `-t` is distinct from the `-t` above.

    * The `-f` or `--fold` will specify the number_of_folds we want to create

    * The `-d` or `--inidis` will specify the initial distance that we want to keep between each fold.
    
    **Usage Command Line Example:**
    
    `python2 -OO myParsePDB.py -i BP1.pdb -o <out_file> -a 3 -s 2 -m 1 -t 1 -f 4 -d 3`
    
3. **myParsePDB.py**

  * This code is commented in four blocks: `util functions`, `Parsing`, `Getting` and `Setting`.
  
  * Here are the list of some major util functions:
  
    * `rotation_matrix(axis, theta)`: takes arbitrary axis and rotating theta and returns a matrix that rotate objects counter-clockwise
    
    * `vector_move(point, dire, dis)`: takes a original data point, moving direction vector, moving distance scalar as parameters and returns a new data point.
    
    * `rotating_around_strand_axis(strand_op, static_axis, theta, out_coords)`: takes strand options, rotating axis (a list of central rotating axis for each fold), rotating theta, and initialized output coordinates as parameters and returns a new output coordinates.
    
    * `ceiling_to_three_digs(line, new_data, num_strands)`: Finalize all data lines, and ceiling the coordinates to 3 decimal places
    
    * `output_files_in_format(outlines,outfile)`: Align and adjust data lines returned from `ceiling_to_three_digs(line, new_data)` in *.pdb format.
 

My Advice to the future optimization
------------------------------------

1. Since `*.pdb` files can be represented as data frames with same format in each line except for the terminal line and end line, if you have time, you can just re-write another version using Bio.PDB module + pandas for simpler and convenient data manipulation, for exmample, you can append new strands as entire objects rather than append new strands line by line. I thought I can hash the table with super keys and increment the hash, but it just adds more complexity to the problem. `pd.append(dataFrame)` will do the job for you.

2. Re-write all list-like, tuple-like structures in numpy array or pandas data frame, they are simply faster than my implementation. The reason why I want to keep coordinates in tuple form is that I want to protect the value from unexpected changing before I want to change it. (It happens once, but I can't reproduce the error now)

3. If you have multi-processing program experience, I'm thinking dynamically throwing files and commands in thread pool (in `parallel_exec.py`) could do the job if huge amount of data is needed during I/O. Bash is fast, but it's not convenient to manipulate numerical arrays. 
    
    
    
