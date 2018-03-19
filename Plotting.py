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
def consumption_plot(shift, nonshift):
    f, (consumptionfig) = plt.subplots(1, 1)
    bins = np.arange(0, len(shift))
    width = 0.60
    p1 = consumptionfig.bar(bins, nonshift, width)
    p2 = consumptionfig.bar(bins, shift, width, bottom=nonshift)

    consumptionfig.set(
        title='Consumption of households',
        xlabel='Hour',
        xticks=bins,
        ylabel='Consumption, kWh'
        )

    consumptionfig.legend((p1[0], p2[0]), ('Nonshiftable appliances',
                                           'Shiftable appliances'))

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
    plt.tight_layout()
    plt.show()



def plot_price(price):
    f, (pricefig) = plt.subplots(1, 1)
    pricefig.set(
        title='Price of energy in neighborhood',
        xlabel='Hour',
        ylabel='Price, NOK/kWh'
    )

    pricefig.plot(price)
    # Making the figure pretty
    pricefig.tick_params(axis="both", which="both", bottom="off",
                               top="off", labelbottom="on", left="off",
                               right="off", labelleft="on")
    pricefig.spines["top"].set_visible(False)
    pricefig.spines["bottom"].set_visible(False)
    pricefig.spines["right"].set_visible(False)
    pricefig.spines["left"].set_visible(False)
    pricefig.set_axisbelow(True)
    pricefig.grid(b=True, which='major', axis='y', color='#cccccc',
                        linestyle='--')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    shiftable = np.random.rand(24)
    nonshiftable = np.random.rand(24)
    consumption_plot(shiftable, nonshiftable)
