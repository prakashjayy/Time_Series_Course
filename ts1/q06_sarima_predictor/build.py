# Default Imports
from greyatomlib.ts1.q01_load_data.build import load_data
from greyatomlib.ts1.q02_data_splitter.build import data_splitter
from greyatomlib.ts1.q05_sarima_model.build import sarima
import pandas as pd
from sklearn.metrics import mean_squared_error
import math 


df = load_data('../data/perrin-freres-monthly-champagne.csv')
X_train, X_valid = data_splitter(df)

tss = pd.DataFrame(X_train["Sales"])
tss.column= ["Sales"]
tss.index = X_train["Month"].values


tss_valid = pd.DataFrame(X_valid["Sales"])
tss_valid.column= ["Sales"]
tss_valid.index = X_valid["Month"].values


sarima_model = sarima(tss)


# Your code here
