import pandas as pd
import numpy as np

df = pd.read_csv("src/seawater/input_data.csv")



def calculate_resistivity(temperature, salinity):
    
    value = df[(df['Temperature (deg C)'] == temperature) & (df['Salinity (%)'] == salinity)]
    
    if value.empty:
        conductance = value['Conductance 1/(ohm.cm)'].mean()
    else:
        conductance = value['Conductance 1/(ohm.cm)'].values[0] 
    
    resistivity = 1 / conductance
    
    return round(resistivity,3)

temperature = float(input("enter temperature value :"))
salinity = float(input("enter salinity value :")) 

result = calculate_resistivity(temperature, salinity)
print("Resistivity:", result)



