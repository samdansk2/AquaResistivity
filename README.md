# Introduction

Simple python library provides a strategy for determining the resistivity of seawater based on given temperature and salinity inputs.
The repository is equipped with a script for performing the calculation, as well as comprehensive tests to ensure reliability and accuracy.

## Files

 - **src/seawater/input_data.csv** : The input dataset containing temperature, salinity, and conductance values.
 - **calculate_resistivity.py** : The Python script for calculating resistivity.
 - **test_calculate_resistivity.py** : The test script for validating the resistivity calculation function.
 - **requirements.txt** : The list of required Python packages.

## Installation

1. Clone the repository
   * git clone repository url
   * cd repositoryname
2. Install required packages from requirements.txt file
   * pip install -r requirements.txt

## Create Conda Environment

create the conda environment in miniconda prompt for good logic flow
  * open miniconda prompt
  * naviagte to the repository location
    * cd location folder
  * conda create --name seawater-resistivity python=3.10
  * activate the environment
    * conda activate seawater-resistivity

## Usage

To calculate the resistivity of seawater, run the **calculate_resistivity.py** script. You can modify the temperature and salinity values as needed.
  * #### Testing

  To run the tests, execute the test_calculate_resistivity.py script. This script contains several test cases to validate the calculate_resistivity function, including :
    * Calculations using values directly from the dataset.
    * Calculations using values not present in the dataset.
    * Handling of extreme values.
    * Verification that a ValueError is raised for negative values.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions or suggestions, please contact at [samdanshaik8998@gmail.com].






