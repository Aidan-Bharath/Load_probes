import numpy as np
import glob
import matplotlib.pyplot as plt
import multiprocessing

####################################################

def loaddata(filename):

    print filename
    location = np.loadtxt(filename,skiprows=18)
    x = location[:,0]
    y = location[:,1]
    print x.shape, y.shape

    plt.scatter(x,y,s=0.01)
    plt.savefig(filename)

    x = None
    y = None


def averdata(filename):

    print filename
    location = np.loadtxt(filename,skiprows=18)
    x = location[:, 0]
    y = location[:, 1]
    startind = np.where(x>=5.613e4+6)[0][0]
    endind = np.where(x<=5.613e4+7)[0][-1]
    x = x[startind: endind]
    y = y[startind: endind]

    n = x.shape[0]
    m = y.shape[0]

    points = 10

    xaxis = n/points
    sliceBeg = (xaxis*points)
    x = np.delete(x, np.s_[sliceBeg:])

    yaxis = m/points
    sliceBeg = (yaxis*points)
    y = np.delete(y, np.s_[sliceBeg:])

    avgx = x.reshape(len(x)/points,-1)
    avgy = y.reshape(len(y)/points,-1)
    print avgx.shape

    avg_x = avgx.sum(axis=1)/len([0])
    avg_y = avgy.sum(axis=1)/len([0])
    avg_x.shape

    #plt.scatter(avg_x, avg_y, s=0.01)
    plt.plot(avg_x, avg_y)
    plt.savefig(filename)

    x = None
    y = None
    avgx = None
    avgy = None
    avg_x = None
    avg_y = None

#####################################################

file = './L*'

list = glob.glob(file)

pool=multiprocessing.Pool()

#pool.map(loaddata,list)
pool.map(averdata,list)


