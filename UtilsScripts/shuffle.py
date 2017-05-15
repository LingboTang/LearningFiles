import random

def main():
    x = []
    y = []
    for i in range(300):
        if (i<200):
            y.append("C")
        x.append("A")
    for i in range(200):
        x.append(y[i])
    random.shuffle(x)
    print(x)    

main()
