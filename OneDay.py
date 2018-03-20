# -*- coding: utf-8 -*-


__author__ = 'Dag Stabell Storhaug'

import random
import numpy as np

"""This function runs one day of consumption of a house or a selection of houses.
Contains all values needed to simulate one day.

Parameters
----------
nr_houses: int
    Number of houses in simulation
x_vectors: np.array
    Array containing all appliances
seed: int
    seed used for random functions
"""
def one_day(nr_houses, x_vectors, seed=12345, rtp=False):
    random.seed(seed)

    #static pricing scheme
    if not rtp:
        price = np.array([
            0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
            0.5, 0.5, 0.5, 0.5, 1, 1, 1, 1, 0.5, 0.5, 0.5
        ])
    #real time pricing scheme, as determined by random numbers
    elif rtp:
        price = np.array([
            random.randint(0.2, 1), random.randint(0.2, 1),
            random.randint(0.2, 1), random.randint(0.2, 1),
            random.randint(0.2, 1), random.randint(0.2, 1),
            random.randint(0.2, 1), random.randint(0.2, 1),
            random.randint(0.2, 1), random.randint(0.2, 1),
            random.randint(0.2, 1), random.randint(0.2, 1),
            random.randint(0.2, 1), random.randint(0.2, 1),
            random.randint(0.2, 1), random.randint(0.2, 1),
            random.randint(0.2, 1), random.randint(0.8, 2),
            random.randint(0.8, 2), random.randint(0.8, 2),
            random.randint(0.8, 2), random.randint(0.2, 1),
            random.randint(0.2, 1), random.randint(0.2, 1)
        ])

    #When all parameters are set, create houses
    houses = np.zeros(nr_houses)
    for i in range(nr_houses):
        house = House() #TODO: sett inn parametre for House
        houses[i] = house

#Constructs the app constraints matrix, 'apps' is a list of Appliance objects
def construct_app_constraints(apps):
    app_constraints = np.zeros((len(apps)*24, (len(apps)*24)+24))
    i = 0
    for appliance in apps:
        app_constraints[i] = [1 for _ in np.linspace(i*24, (i+1)*23, 24)]


