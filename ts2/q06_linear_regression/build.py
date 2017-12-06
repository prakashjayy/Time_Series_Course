# Default Imports
from greyatomlib.ts1.q01_load_data.build import load_data
from greyatomlib.ts1.q02_data_splitter.build import time_data_splitter
from greyatomlib.ts1.q05_feature_engineering.build import fe
from sklearn.linear_model import LinearRegression



# Load the package for sarimax and use load_data() and data_splitter() function
df = load_data('../data/elecdemand.csv')

## Your code here
