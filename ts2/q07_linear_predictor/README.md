# Your very first prediction - Using fitted linear regression model

## Let's write a function `linear_predictor()` that
* Takes in a fitted linear model and makes a prediction on validation dataset
* It also calculates Root Mean square error on the validation dataset

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| lm | sklearn.linear_model.LinearRegression | compulsory | | Fitted Linear Regression model |
| X_train | numpy.ndarray/Pandas Dataframe | compulsory | | Train input feature values |
| y_train | numpy array | compulsory | | Train Target Variable |
| X_valid | numpy.ndarray/Pandas Dataframe | compulsory | | Valid input feature values |
| y_valid | numpy array | compulsory | | valid Target Variable |

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| y_pred | numpy.ndarray | Predicted values |
| rmse | numpy.float64 | Root Mean square error |
