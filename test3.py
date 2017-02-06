# test3.py

# TO DO:
# - Finish parameterizing the function with the range.

# Import Packages
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Initialize some stuff
loc, scale = 0., 100.
t = []
arraylen = 1000
bincount = 29

def plotComp(pdist,qdist,bincount):

    mybins = [r * (100./bincount) for r in range(0,bincount + 1)]
    # Create the histogram
    pcount, pbins = np.histogram(pdist,mybins)
    qcount, qbins = np.histogram(qdist,mybins)

    # Settings for plot
    pos = list(range(len(pcount)))
    width = 0.33

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
qsamp = pd.DataFrame(np.random.normal(70,10,arraylen), columns = ['Q'])



plotComp(psamp,qsamp,bincount)



