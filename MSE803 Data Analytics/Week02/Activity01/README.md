
# Beijing Multi-Site Air Quality Analysis

## Dataset Description
This project uses the Beijing Multi-Site Air Quality dataset from the UCI Machine Learning Repository. It contains hourly measurements of air pollutants and meteorological variables collected from multiple monitoring stations in Beijing between 2013 and 2017.

Each station’s data is provided as a separate CSV file. All files were combined into a single dataset for analysis.

## Data Structure
The dataset has 420,768 rows and 18 columns. It includes time variables (year, month, day, hour), air pollutants (PM2.5, PM10, SO2, NO2, CO, O3), meteorological variables (temperature, pressure, dew point, rainfall), wind information (direction and speed), and station name.

Most variables are numerical, while wind direction and station are categorical. Some columns contain missing values.

## Task-1
- Loaded all CSV files using pandas  
- Combined them into a single DataFrame  
- Displayed the first 5 rows  
- Identified column names and data types  
- Counted total rows and columns  

Final dataset shape:
- Rows: 420768  
- Columns: 18  

## Consistency Check
All CSV files have the same column structure. This was verified using the following code:

```python
import pandas as pd
import glob

files = glob.glob("PRSA_Data_*.csv")
columns_list = [set(pd.read_csv(file, nrows=1).columns) for file in files]

all_same = all(cols == columns_list[0] for cols in columns_list)
print(all_same)
