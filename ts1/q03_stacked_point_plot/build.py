# Default Imports
from greyatomlib.ts1.q01_load_data.build import load_data
from greyatomlib.ts1.q02_data_splitter.build import data_splitter
import seaborn as sns 


# Load the package for linear regression and use load_data() and data_splitter() function
df = load_data('../data/perrin-freres-monthly-champagne.csv')
X_train, X_valid = data_splitter(df)



X_train["year"] = X_train["Month"].dt.year
X_train["month"] = X_train["Month"].dt.strftime('%b')


# Your code here
