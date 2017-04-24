**Introduction: **

There are three different ways I created to extract the minimum free energy structure from Iterative HFold output. They are written in pure bash, C and python. Iterative HFold will produce the pseudoknotted secondary structure for given exons and oligos combinations. Depends on which language you are more familliar with, you can choose the one you want to use

(1) Python: This is a simplest and the most readable version. It contains a extract_energy(filename) function such that it will return and you can give an inputpath through command line.

Sample Usage: `python extract_min_energy.py -i <inputpath>`

(2) Pure bash: This is simple but a bit verbose than the python version. It has two sub routine, first extract the value from give files in the given directory. Then compare the value in the collection array. Make sure you grant the access for this script by:

sudo chmod +x <this_script.sh>


Sample Usage: `./extract_min_energy_pure_bash.sh`


(3) C: This is the most complicated version. It contains a C file `C_extract_min_energy.c` that only extract the energy value in one given file, and a `Makefile` to compile the C file with optimization options. Then `batch_exon_files_C_extract.sh` will go through the given input path and execute the C file on each file. The only advantage using this is when more data is added to our current data so that you can use threading or optimization options to speed up your execution.

Sample Usage: `./batch_exon_files_C_extract.sh`
