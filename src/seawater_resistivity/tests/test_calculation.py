import seawater_resistivity
import pytest

def test_resistivity_calculation():
    assert seawater_resistivity.resistivity(35, 25) == 18.855  # result: 18.855 Ohm-m

def test_resistivity_negative_temperature():
    # negative temperature
    with pytest.raises(ValueError):
        seawater_resistivity.resistivity(35, -5)  #raise ValueError

def test_resistivity_zero_salinity():
    # zero salinity
    assert seawater_resistivity.resistivity(0, 25) == 4.943  # result: 4.943 Ohm-m
