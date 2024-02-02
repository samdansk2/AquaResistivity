# Python program to find the resistivity of sea water for given salinity and temperature.
def resistivity(salinity,temperature):
    
    sp_conductance_from_table = 0.038065
    
    resistivity = 1 / sp_conductance_from_table
    
    return resistivity

salinity = 15
temperature = 20 

result = resistivity(salinity,temperature)

print("The Resistivity for the given salinity and temperature is :" ,result)