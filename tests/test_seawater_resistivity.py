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

def test_linear_interpolation():
    assert calculate_resistivity(15, 1.5) == 1 / 2.5

def test_nearest_neighbor_interpolation():
    assert calculate_resistivity(100, 100) == 1 / 4
    assert calculate_resistivity(-100, -100) == 1 / 1

def test_edge_cases():
    assert calculate_resistivity(0, 0) == 1
    assert calculate_resistivity(30, 3) == 1 / 4

def test_zero_temperature():
    assert calculate_resistivity(0, 1) == 1 / 1
    assert calculate_resistivity(0, 2) == 1 / 1.5

def test_zero_salinity():
    assert calculate_resistivity(20, 0) == 1 / 2
    assert calculate_resistivity(10, 0) == 1 / 1

def test_zero_temperature_and_salinity():
    assert calculate_resistivity(0, 0) == 1
    assert calculate_resistivity(0, 0.1) == 1 / 1.1




