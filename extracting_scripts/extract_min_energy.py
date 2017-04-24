import os
import sys

''' 
    Parse the files from the Iterative HFold output
    Find the keyword "energy:" in the file
    Extract the energy from the file as function return
'''
def extract_energy(filename):
    processing_file = open(filename, 'r')
    keyword = "energy:"
    tmpval=0.0
    for line in processing_file:
        line = line.split()
        if keyword in line:
            tmpval =float(line[1])
    return tmpval


def main(argv):
    
    # Global variables
    mins = []
    inputpath = ""

    # Getting the input from the command line
    try:
        inputpath = argv[-1]
    except Exception:
        print("python extract_min_energy.py -i <inputpath>")

    # You can customize your input here
    for root, dirs, files in os.walk("/home/lingbo/CPofAaronsData/exon_44_output/"):
        tmp_min = []
        # Calling the extract_energy file to collect energy values in each file
        ''' 
            TO DO:
            You can also store the corresponding file here. 
        '''
        for file in files:
            number = extract_energy(os.path.join(root,file))
            tmp_min.append(number)
        # Directly calling the built in min to find the minimum
        if (len(tmp_min) > 0):
            mins.append(min(tmp_min))
    print mins

if __name__ == "__main__":
    main(sys.argv[1:])