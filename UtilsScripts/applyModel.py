import numpy as np
import scipy
import pandas as pd
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Normalize points of data to plot in matplotlib
def pre_process_3dPlot(data,n):
    this_min = np.amin(data)
    this_max = np.amax(data)
    return (this_max-this_min)*np.random.rand(n) + this_min

# Predicting Model
def model(data):
    if (data[2] == "C"):
        return -0.2273*float(data[0]) -2.1145*float(data[1]) + 11.8885- 37.7764
    else:
        return -0.2273*float(data[0]) -2.1145*float(data[1]) - 37.7764


def main():
    # Parsing Data file
    newData = []
    f = open("/home/lingbo/Desktop/validate.arff","r")
    for line in f:
        newData.append(line.split())
    dataStartIndex = newData.index(["@DATA"])

    # Get Attributes
    attributes =  newData[1:dataStartIndex]
    for item in attributes:
        if len(item) == 0:
            attributes.remove(item)

    # Get Data
    Data = newData[dataStartIndex+1:]
    for item in Data:
        if len(item) == 0:
            Data.remove(item)

    # Close Input file
    f.close()
    
    # Predict data
    model_predicted = []
    for line in Data:
        model_predicted.append(model(line))
    DfA_1 = np.array([data[0] for data in Data if data[2]=="C"])
    DfA_2 = np.array([data[0] for data in Data if data[2]=="A"])
    C_type = [i for i in range(len(Data)) if Data[i][2] == "C"]
    A_type = [i for i in range(len(Data)) if Data[i][2] == "A"]
    y_1 = np.array(filter(lambda value: model_predicted.index(value) in C_type, model_predicted))
    y_2 = np.array(filter(lambda value: model_predicted.index(value) in A_type, model_predicted))
    plt.figure(1)
    plt.plot(DfA_1,y_1,"ro")
    plt.plot(DfA_2,y_2,"bo")
    plt.show()
    original_skip = [float(data[4]) for data in Data]
    y1 = np.array(filter(lambda value: original_skip.index(value) in C_type, original_skip))
    y2 = np.array(filter(lambda value: original_skip.index(value) in A_type, original_skip))
    plt.figure(2)
    plt.plot(DfA_1,y1,"ro")
    plt.plot(DfA_2,y2,"bo")
    plt.show()    
    DfA = np.array([float(data[0]) for data in Data])
    dG50 = np.array([float(data[1]) for data in Data])
    y = np.array(model_predicted)
    y_ = np.array(original_skip)
    plt.figure(3)
    plt.plot(DfA,y,"ro")
    plt.plot(DfA,y_,"bo")
    plt.show()
    plt.figure(4)
    plt.plot(y,y_,"o")

    # Plot Linear Surface in 3D to visualize the multi-variable linear regression
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    xs = pre_process_3dPlot(DfA,100)
    ys = pre_process_3dPlot(dG50,100)
    z = np.array(original_skip)
    zs = pre_process_3dPlot(z,100)
    this_z = np.array(model_predicted)
    ax.scatter(xs,ys,zs,"o")
    ax.set_xlabel('DfA')
    ax.set_ylabel('dG50')
    ax.set_zlabel('skipping')
    plt.show()
    

main()
