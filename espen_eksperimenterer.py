# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:33:51 2018

@author: espen
"""
import numpy as np
from scipy.optimize import linprog

# Sjekk denne lenken:
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.linprog.html

# Non-shiftables [kWh]
_lighting = np.array([0,0,0,0,0,0,
            0,0,0,0,1,1,
            1,1,1,1,1,1,
            1,1,1,0,0,0])
lighting = [i/sum(_lighting) for i in _lighting]

_heating = np.array([9.6]*24)
heating = [i/sum(_heating) for i in _heating]

# Shiftable sum [kWh]
eletric_car = 9.9

# brukes til å finne summen av vektoren
ones = np.ones((1,24))

# RTP [NOK/kWh]
price = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 1,
         1, 1, 1, 0.5, 0.5, 0.5,
         0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
         0.5, 0.5, 0.5, 0.5, 0.5, 0.5])


linprog(price, A_eq=ones, b_eq=eletric_car)