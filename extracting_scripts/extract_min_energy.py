import os

def extract_min_energy(filename):
    processing_file = open(filename, 'r')
    keyword = "energy:"
    tmpval=0.0
    for line in processing_file:
        line = line.split()
        if keyword in line:
            tmpval =float(line[1])
    return tmpval


def main():
    mins = []
    for root, dirs, files in os.walk("/home/lingbo/CPofAaronsData/"):
        tmp_min = []
        for file in files:
            number = extract_min_energy(os.path.join(root,file))
            tmp_min.append(number)
        if (len(tmp_min) > 0):
            mins.append(min(tmp_min))
    print mins


main()