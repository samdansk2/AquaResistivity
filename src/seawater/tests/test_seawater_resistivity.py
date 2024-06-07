import pytest
import sys
import os

current_dir = os.path.dirname(__file__)
seawater_dir = os.path.abspath(os.path.join(current_dir, '../../'))
if seawater_dir not in sys.path:
    sys.path.insert(0, seawater_dir)

from seawater_resistivity import calculate_resistivity

def test_calculation_with_known_input():
    # Test calculation 
    expected_result= 66.361
    result = calculate_resistivity(10,0.7)
    assert round(result, 3) == round(expected_result, 3)  
    
def test_zero_salinity():
    expected_result= 51.988
    result = calculate_resistivity(15,0.8)
    assert round(result, 3) == round(expected_result, 3)

def test_random():
    expected_result= 29.024
    result = calculate_resistivity(5,2)
    assert round(result, 3) == round(expected_result, 3)

def test_zero_temperature():
    expected_result = 100  
    result = calculate_resistivity(10, 0)
    assert round(result, 3) == round(expected_result, 3)




