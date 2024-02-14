import pytest
from seawater_resistivity.seawater_resistivity_csv1 import calculate_resistivity


def test_calculation_with_known_input():
    # Test calculation 
    result = calculate_resistivity(10,0.7)  
    assert result == 66.666 

def test_negative_temperature():
    with pytest.raises(ValueError):
        calculate_resistivity(20,1.7)  # raise a ValueError

def test_zero_salinity():
    result = calculate_resistivity(15,0.8)  
    assert result == 51.988

