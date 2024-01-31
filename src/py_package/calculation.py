# Python program to find the resistivity of sea water for a given salinity and temperature.
def resistivity(salinity,temperature):
    base_conductance = 1.0
    alpha = 0.0191  
    beta = 0.00625  

    sp_cond = base_conductance * (1 + alpha * salinity - beta * (temperature - 25))
    
    resistivity = 1 / sp_cond
    
    return resistivity

salinity = int(input(" enter salinity value in (ppt)"))
temperature =int(input("enter temperature in (°C)"))

result = resistivity(salinity,temperature)

print("The Resistivity for the given salinity and temperature is " ,result)