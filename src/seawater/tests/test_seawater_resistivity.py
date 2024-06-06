import pytest
from src.seawater.tests import seawater_resistivity_csv1
from seawater_resistivity_csv1 import calculate_resistivity

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



