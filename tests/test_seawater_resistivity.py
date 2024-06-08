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

def test_calculate_resistivity():
    
    temperature = 25  
    salinity = 3.5    
    assert calculate_resistivity(temperature, salinity) == 18.672
    
    temperature = 15  
    salinity = 4.0    
    assert calculate_resistivity(temperature, salinity) == 20.856
    
    
    temperature = 20  
    salinity = 3.0    
    assert calculate_resistivity(temperature, salinity) == 18.672
    
    
    temperature = 0   
    salinity = 0    
    assert calculate_resistivity(temperature, salinity) == 543.774
    
    print("All tests pass!")

test_calculate_resistivity()



