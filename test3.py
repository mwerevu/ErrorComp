# test3.py

# TO DO:
# - Finish parameterizing the function with the range.

# Import Packages
from numpy.linalg import norm
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import entropy
from math import sqrt

# Initialize some stuff
loc, scale = 0., 100.
t = []
arraylen = 1000
bincount = 29

def kld(P,Q):
    _P = np.array(P) / norm(P, ord=1)
    _Q = np.array(Q) / norm(Q, ord=1)
    return round(np.sum([v for v in _P * np.log2(_P/_Q) if (not np.isnan(v) and not np.isinf(v))]),12)

def jsd(P,Q):
    _P = np.array(P) / norm(P, ord=1)
    _Q = np.array(Q) / norm(Q, ord=1)
    M = 0.5 * (_P + _Q)
    return round(0.5 * (kld(_P,M) + kld(_Q,M)),12)

def rmse(P,Q):
    _P = np.array(P)
    _Q = np.array(Q)
    return round(sqrt(np.mean([np.power(_P - _Q,2)])),12)


def plotComp(pdist,qdist,bincount):

    mybins = [r * (100./bincount) for r in range(0,bincount + 1)]
    # Create the histogram
    pcount, pbins = np.histogram(pdist,mybins)
    qcount, qbins = np.histogram(qdist,mybins)

    #print(pcount)
    #print(qcount)
    jsd1 = jsd(pcount,qcount)
    print("jsd = %f" % jsd1)
    print("rjsd = %f" % sqrt(jsd1))
    rmse1 = rmse(pcount,qcount)
    print("rmse = %f" % rmse1)
    print("normed rmse = %f" % (rmse1/arraylen))
    
    # Settings for plot
    pos = list(range(len(pcount)))
    width = 0.25

    # Plotting the bars
    fig, ax = plt.subplots(figsize=(10,5))

    # Create plot for P
    plt.bar(
        pos,
        pcount,
        width,
        alpha=0.5,
        color='#EE3224',
        label="P"
        )

    # Create plot for Q
    plt.bar(
        [j + width for j in pos],
        qcount,
        width,
        alpha=0.5,
        color='#F78F1E',
        label="Q"
        )

    # Set Title
    stats = "Jensen-Shannon Divergence (JSD) = %f\n Root Mean Squared Error = %f" % (jsd1,rmse1)
    ax.set_title(stats)
    
    # Setting the x-axis and y-axis limits
    plt.xlim(min(pos)-width, max(pos)+width*4)
    plt.ylim([0, max(max(pcount),max(qcount))] )

    
    # Plot it
    plt.legend(['P','Q'])
    plt.grid()
    plt.show()





# Build out the dummy data structure
#psamp = pd.DataFrame(np.random.uniform(loc,scale,arraylen), columns = ['P'])
#qsamp = pd.DataFrame(np.random.uniform(loc,scale,arraylen), columns = ['Q'])
psamp = pd.DataFrame(np.random.normal(30,20,arraylen), columns = ['P'])
qsamp = pd.DataFrame(np.random.normal(40,10,arraylen), columns = ['Q'])



plotComp(psamp,qsamp,bincount)



