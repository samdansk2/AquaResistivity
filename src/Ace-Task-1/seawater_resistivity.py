import os
from assetutilities.common.yml_utilities import ymlInput

inputfile = 'src\seawater_resistivity\seawater_resistivity.yml'
# inputfile = 'src\seawater_resistivity\seawater_resistivity1.yml'

if os.path.isfile(inputfile):
    print("File exist")
else:
    print("File not exist")
    raise FileNotFoundError

cfg = ymlInput(inputfile, updateYml=None)

def resistivity(salinity, temperature):
    '''
    Python program to find the resistivity of sea water for given salinity and temperature.
    '''
    sp_conductance_from_table = cfg['variables']['sp_conductance_from_table']

    resistivity = 1 / sp_conductance_from_table

    return resistivity

salinity = cfg['variables']['salinity']
temperature = cfg['variables']['temperature']

result = resistivity(salinity,temperature)

print(f"The Resistivity for the given salinity, {salinity} and temperature, {temperature} is : {round(result,2)}")
