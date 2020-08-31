'''Author: Rhea Sanjan
Created date: 19th May 2018 

Simple linear regression without using any library'''


import numpy as np
import matplotlib.pyplot as plt
def estimate(x,y):
    n = np.size(x)
    m_x = np.mean(x)
    m_y =  np.mean(y)
    #SSxy and SSxx
    SS_xy = np.sum(y*x - n* m_x *m_y)
    SSxx = np.sum(x*x - n* m_x* m_x)
    b1 = SS_xy/SSxx
    b0 = m_y - b1*m_x
    return (b0,b1)
def plotReg(x,y,b):
    plt.scatter(x,y,color="m",marker="o",s=30)
    ypred = b[0] + b[1] * x
    plt.plot(x,ypred,color="g")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
def main():
    x = np.array([0,1,2,3,4,5,6,7,8,9])
    y = np.array([1,3,2,5,7,8,8,9,10,12])
    b = estimate(x,y)
    print "b0 = {} and b1 = {}" .format(b[0],b[1])
    plotReg(x,y,b)
if __name__ == "__main__":
    main()
