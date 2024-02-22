import pytest
from seawater_resistivity.seawater_resistivity_csv1 import calculate_resistivity

def test_calculation_with_known_input():
    # Test calculation 
    expected_result= 66.3614042
    result = calculate_resistivity(10,0.7)
    assert round(result, 7) == round(expected_result, 7)  
    

def test_zero_salinity():
    expected_result= 51.9885625
    result = calculate_resistivity(15,0.8)
    assert round(result, 7) == round(expected_result, 7)


