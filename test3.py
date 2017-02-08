# test3.py

# TO DO:


# Import Packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from diststats import *

# Initialize some stuff
loc, scale = 0., 100.
samples = 60
bincount = 29



def setBins(bincount,lbound,ubound):
    # Define the bins we will use.
    return [r * ((ubound-lbound)/bincount) for r in range(0,bincount + 1)]


def plotComp(pdist,qdist,bins):
    # Create the histogram
    pcount, pbins = np.histogram(pdist,bins)
    qcount, qbins = np.histogram(qdist,bins)

    jsd1 = jsd(pcount,qcount)
    print("jsd = %f" % jsd1)
    print("rjsd = %f" % sqrt(jsd1))
    rmse1 = rmse(pcount,qcount)
    print("rmse = %f" % rmse1)
    #print("normed rmse = %f" % (rmse1/np.sum(pcount)))
    
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
        color='#3539B8',
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
psamp = pd.DataFrame(np.random.uniform(loc,scale,samples), columns = ['P'])
qsamp = pd.DataFrame(np.random.uniform(loc,scale,samples), columns = ['Q'])
#psamp = pd.DataFrame(np.random.normal(30,20,samples), columns = ['P'])
#qsamp = pd.DataFrame(np.random.normal(40,10,samples), columns = ['Q'])


bins = setBins(bincount,loc,scale)
plotComp(psamp,qsamp,bins)



