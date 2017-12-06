# Default Imports
from greyatomlib.ts1.q01_load_data.build import load_data
from greyatomlib.ts1.q02_data_splitter.build import time_data_splitter
from greyatomlib.ts1.q05_feature_engineering.build import fe
from greyatomlib.ts1.q08_randomforest_regressor.build import randomforest_regressor
from sklearn.metrics import mean_squared_error
import math


# Load the package for sarimax and use load_data() and data_splitter() function
df = load_data('../data/elecdemand.csv')
df = fe(df)
time_frames = time_data_splitter(df, n=3)

fe_2_use = ["WorkDay", "hour", "month"]
train_index , valid_index = time_frames[2] ## Instead of cross_validation , lets just use one split

X_train, y_train = df[fe_2_use].values[train_index], df[fe_2_use].values[train_index]
X_valid, y_valid = df[fe_2_use].values[valid_index], df[fe_2_use].values[valid_index]

rf_model = randomforest_regressor(X_train, y_train)


# Your code here
