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

def sample_data():
    data = {
        'Temperature (deg C)': [0, 10, 20, 30],
        'Salinity (%)': [0, 1, 2, 3],
        'Conductance 1/(ohm.cm)': [1, 2, 3, 4]
    }
    return pd.DataFrame(data)

def test_direct_lookup(sample_data):
    assert calculate_resistivity(10, 1, sample_data) == 0.5
    assert calculate_resistivity(20, 2, sample_data) == 1/3

def test_linear_interpolation(sample_data):
    assert calculate_resistivity(15, 1.5, sample_data) == 1 / 2.5

def test_nearest_neighbor_interpolation(sample_data):
    assert calculate_resistivity(100, 100, sample_data) == 1 / 4
    assert calculate_resistivity(-100, -100, sample_data) == 1 / 1

def test_edge_cases(sample_data):
    assert calculate_resistivity(0, 0, sample_data) == 1
    assert calculate_resistivity(30, 3, sample_data) == 1 / 4

def test_zero_temperature(sample_data):
    assert calculate_resistivity(0, 1, sample_data) == 1 / 1
    assert calculate_resistivity(0, 2, sample_data) == 1 / 1.5

def test_zero_salinity(sample_data):
    assert calculate_resistivity(20, 0, sample_data) == 1 / 2
    assert calculate_resistivity(10, 0, sample_data) == 1 / 1

def test_zero_temperature_and_salinity(sample_data):
    assert calculate_resistivity(0, 0, sample_data) == 1
    assert calculate_resistivity(0, 0.1, sample_data) == 1 / 1.1




