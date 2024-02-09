# %%
import pandas as pd


# %%
df = pd.read_csv("C:/Users/Samdan Shaik/Desktop/seawater/input_data.csv")
df

# %%
df.head(10)

# %%
df.tail(10)

# %%
df.describe()

# %%
def calculate_resistivity(temperature, salinity):
    # Filtering the DataFrame based on the provided temperature and salinity
    value = df[(df['Temperature (deg C)'] == temperature) & (df['Salinity (%)'] == salinity)]
    
    if value.empty:
        filtered_data = df
        conductance = value['Conductance 1/(ohm.cm)'].mean()
    else:
        conductance = value['Conductance 1/(ohm.cm)'].values[0] 
    
    resistivity = 1 / conductance
    
    return resistivity

temperature = 20
salinity = 0.8 

result = calculate_resistivity(temperature, salinity)
print("Resistivity:", round(result, 3))

# %%
print(df.columns)



