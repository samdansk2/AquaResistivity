import pandas as pd
import numpy as np
from scipy.interpolate import griddata

df = pd.read_csv("src/seawater/input_data.csv")

def calculate_resistivity(temperature, salinity):
    
    if temperature < 0 or salinity < 0:
        raise ValueError("Temperature and salinity must be non-negative values.")
    
    value = df[(df['Temperature (deg C)'] == temperature) & (df['Salinity (%)'] == salinity)]
    
    if value.empty:
        points = df[['Temperature (deg C)', 'Salinity (%)']].values
        values = df['Conductance 1/(ohm.cm)'].values
        conductance = griddata(points, values, (temperature, salinity), method='linear')
        
        # If interpolation result is NaN use nearest neighbor
        if np.isnan(conductance):
            conductance = griddata(points, values, (temperature, salinity), method='nearest')
        
    else:
        conductance = value['Conductance 1/(ohm.cm)'].values[0] 
    
    resistivity = 1 / conductance
    
    return round(resistivity,3)

temperature = np.random.choice(df['Temperature (deg C)'])
salinity = np.random.choice(df['Salinity (%)'])


result = calculate_resistivity(temperature, salinity)
print("Resistivity:", result)



