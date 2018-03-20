# -*- coding: utf-8 -*-

"""

"""

__author__ = 'Dag Stabell Storhaug'
__email__ = 'dag.storhaug@nmbu.no'


import matplotlib.pyplot as plt
import numpy as np
plt.style.use('seaborn-colorblind')


#Creates a stacked bargraph. putting the values of the np.array 'nonshift' at
# the bottom and the values of np.array 'shift' on top.
def power_plots(shift=None, nonshift=None, shiftnames=None,
                     nonshiftnames=None, price=None):
    f, (consumptionfig) = plt.subplots(1, 1)
    if shift:
        length = len(shift[0])
    elif nonshift:
        length = len(nonshift[0])
    elif price is not None:
        length = len(price)
    bins = np.arange(0, length)
    width = 0.9
    bottom = np.zeros(length)

    #iterate over shiftable and nonshiftable appliances to create stacked
    # bars for the chart.
    if nonshift:
        for i in range(len(nonshift)):
            consumptionfig.bar(bins, nonshift[i], width=width, bottom=bottom,
                               label=nonshiftnames[i])
            bottom = np.add(bottom, nonshift[i])
    if shift:
        for i in range(len(shift)):
            consumptionfig.bar(bins, shift[i], width=width, bottom=bottom,
                               label=shiftnames[i])
            bottom = np.add(bottom, shift[i])

    consumptionfig.set(
        title='Consumption of households',
        xlabel='Hour',
        xticks=bins,
        ylabel='Consumption, kWh'
        )

    #retrieving labels to make a neat legend
    handles, labels = consumptionfig.get_legend_handles_labels()
    consumptionfig.legend(handles, labels)

    #Making the figure pretty
    consumptionfig.tick_params(axis="both", which="both", bottom="off",
                               top="off", labelbottom="on", left="off",
                               right="off", labelleft="on")
    consumptionfig.spines["top"].set_visible(False)
    consumptionfig.spines["bottom"].set_visible(False)
    consumptionfig.spines["right"].set_visible(False)
    consumptionfig.spines["left"].set_visible(False)
    consumptionfig.set_axisbelow(True)
    consumptionfig.grid(b=True, which='major', axis='y', color='#cccccc',
                        linestyle='--')

    if price is not None:
        pricefig = consumptionfig.twinx()
        pricefig.step(bins, price, color='black')
        pricefig.set(ylabel='Price, NOK/kWh')
        pricefig.spines["top"].set_visible(False)
        pricefig.spines["bottom"].set_visible(False)
        pricefig.spines["right"].set_visible(False)
        pricefig.spines["left"].set_visible(False)
        consumptionfig.set_axisbelow(True)


    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    shiftable = [np.random.rand(24), np.random.rand(24)]
    nonshiftable = [np.random.rand(24), np.random.rand(24)]
    shiftablenames = ['shiftable', 'shiftable']
    nonshiftablenames = ['nonshiftable', 'nonshiftable']
    price = np.random.rand(24)
    power_plots(shift=shiftable, nonshift=nonshiftable,
                shiftnames=shiftablenames, nonshiftnames=nonshiftablenames,
                price=price)

