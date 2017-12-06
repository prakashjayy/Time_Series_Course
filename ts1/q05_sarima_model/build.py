# Default Imports
from greyatomlib.ts1.q01_load_data.build import load_data
from greyatomlib.ts1.q02_data_splitter.build import data_splitter
from statsmodels.tsa.statespace import sarimax



# Load the package for sarimax and use load_data() and data_splitter() function
df = load_data('../data/perrin-freres-monthly-champagne.csv')
X_train, X_valid = data_splitter(df)


## Your code here 
