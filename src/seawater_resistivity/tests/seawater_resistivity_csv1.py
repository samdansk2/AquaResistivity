# %%
import pandas as pd


# %%
df = pd.read_csv("src/seawater_resistivity/input_data.csv")
df

# %%
df.head(10)

# %%
df.tail(10)

# %%
def calculate_resistivity(temperature, salinity):
    # checking for temperature and salinity values with input
    value = df[(df['Temperature (deg C)'] == temperature) & (df['Salinity (%)'] == salinity)]
    
    if value.empty:
        value = df
        conductance = value['Conductance 1/(ohm.cm)'].mean()
    else:
        conductance = value['Conductance 1/(ohm.cm)'].values[0] 
    
    resistivity = 1 / conductance
    
    return resistivity

temperature = int(input("enter temperature value :"))
salinity = float(input("enter salinity value :")) 

result = calculate_resistivity(temperature, salinity)
print("Resistivity:", round(result, 3))



