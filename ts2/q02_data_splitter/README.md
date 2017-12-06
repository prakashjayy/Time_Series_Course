# Split Data into train and validation - Setting up the analysis

Now that you have imported the data, lets split the data into train and validation

Why do we need to split the data ?
Tip: In practice, before predicting for future, We need to backtest our model performance. So first we need to split our data into train and validation. Build our model on train data and verify it on validation data

Why do we need to test our model performance on validation data and not on train data ?
Tip: Learn what does Over-fitting means


## Cross-Validation in TimeSeries
- Since timeseries has an order component, random train_test_split which works for most of the data science problems doesn't work here. We need a special function which split our data into n_series so that we can evaluate the model more effectively using cross_validation


## Write a function `time_data_splitter()` which returns the indexes of the train and valid as a list of tuples.


### Parameters:

Function should takes a dataframe and the number of splits required and outputs a list of tuples, with each tuple containing array of train and valid index locations of input data frame.

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| df | DataFrame | compulsory |  | Input Dataframe to split |
| n  | int | compulsory | | Number of splits |



### Returns:

| Return | dtype | description |
| --- | --- | --- |
| splits | list | A list of tuples, with each tuple containing train_indexes and validation_indexes |
