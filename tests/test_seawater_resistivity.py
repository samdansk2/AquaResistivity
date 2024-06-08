import pytest
import sys
import os
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

current_dir = os.path.dirname(__file__)
seawater_dir = os.path.abspath(os.path.join(current_dir, '../../'))
if seawater_dir not in sys.path:
    sys.path.insert(0, seawater_dir)

from src.seawater_resistivity import calculate_resistivity

def test_non_df_value():
    temperature = 30  
    salinity = 4.0    
    assert calculate_resistivity(temperature, salinity) == 18.672

def test_negative_value():
    temperature = 10
    salinity = -5   
    try:
        calculate_resistivity(temperature, salinity)
    except ValueError:
        print("ValueError raised for negative values.")
    else:
        raise AssertionError("Value error not for non negative values.")

def test_zero_temp():
    temperature = 0   
    salinity = 2    
    assert calculate_resistivity(temperature, salinity) == 33.462

def test_random_input():
    temperature = 20  
    salinity = 3.0    
    assert calculate_resistivity(temperature, salinity) == 18.672

def test_with_zero():  
    temperature = 0   
    salinity = 0    
    assert calculate_resistivity(temperature, salinity) == 543.774

    print("All tests pass!")



