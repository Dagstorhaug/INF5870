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
lighting = np.array([i/sum(_lighting) for i in _lighting])

_heating = np.array([9.6]*24)
heating = np.array([i/sum(_heating) for i in _heating])

tot_nonshiftable = lighting + heating

# Shiftable sum [kWh]
eletric_car = 9.9
cloth_dryer = 2.5
laundry_machine = 1.94
dishwasher = 1.44
tot_shiftable = eletric_car + cloth_dryer + laundry_machine + dishwasher

# brukes til å finne summen av vektoren
ones = np.ones((1,24))

# RTP [NOK/kWh]
tou_price = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 1,
         1, 1, 1, 0.5, 0.5, 0.5,
         0.5, 0.5, 0.5, 0.5, 0.5, 0.5,
         0.5, 0.5, 0.5, 0.5, 0.5, 0.5])
max_kwh = 4 # max usage pr hour

price_with_nonshiftables = tot_nonshiftable*tou_price

dayly_usage = linprog(price_with_nonshiftables,
                      A_eq=ones,
                      b_eq=tot_shiftable,
                      bounds=(0,max_kwh))
print(dayly_usage)