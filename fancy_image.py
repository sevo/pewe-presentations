# toto je kod na vytvorenie fancy grafu, ktory nemusite podrobne studovat ak sa vam nechce. Dolezity je vysloedok, aby som na nom vysvetlil princip transformacie

from scipy.stats import norm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def breakpoints(alphabetSize):
        return list(map(norm.ppf, np.linspace(0,1,alphabetSize+1)[1:-1]))
    
def interval_centres(alphabetSize):
    return breakpoints(alphabetSize * 2)[::2]
    
def adjust_spines(ax, spines):
    for loc, spine in ax.spines.items():
        if loc in spines:
            spine.set_position(('outward', 10))  # outward by 10 points
            spine.set_smart_bounds(True)
        else:
            spine.set_color('none')  # don't draw spine

    # turn off ticks where there is no spine
    if 'left' in spines:
        ax.yaxis.set_ticks_position('left')
    else:
        # no yaxis ticks
        ax.yaxis.set_ticks([])

    if 'bottom' in spines:
        ax.xaxis.set_ticks_position('bottom')
    else:
        # no xaxis ticks
        ax.xaxis.set_ticks([])

def plot_fancy_image():
    plt.rcParams['figure.figsize'] = 9, 3

    fig, ax = plt.subplots(1, 1)

    symbol_num = 5
    brp = breakpoints(symbol_num)
    centres = interval_centres(symbol_num)
    lw = 1.4

    plt.vlines(brp, 0.005, list(map(norm.pdf, brp)), color='red', linewidth=lw)

    x = np.linspace(norm.ppf(0.0001), norm.ppf(0.9999), 100)
    ax.plot(x, norm.pdf(x), '-', color='black', linewidth=lw)

    hatched2 = np.linspace(-4, brp[0], 100)
    ax.fill_between(hatched2, norm.pdf(hatched2), facecolor="none", hatch="///", edgecolor="black", linewidth=0.0, alpha=0.5)

    hatched = np.linspace(brp[0], brp[1], 100)
    ax.fill_between(hatched, norm.pdf(hatched), facecolor="none", hatch='\\\\\\', edgecolor="black", linewidth=0.0, alpha=0.5)

    adjust_spines(ax, ['left', 'bottom'])
    # adjust_spines(ax, ['bottom'])

    letters = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    for i in range(symbol_num):
        ax.annotate(letters[i], xy=(centres[i], 0.05), horizontalalignment='center', verticalalignment='middle', backgroundcolor='w', 
                    fontsize='15', color='black', bbox=dict(color='white', alpha=0.7))

    ax.set_ylim([0, 0.45])