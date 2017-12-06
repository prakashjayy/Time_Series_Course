# Fitting your first randomforest regression model

## Let's write a function `randomforest_regressor()` that
* Takes as input the features and target
* Fits a randomforest_regressor with default parameters model on it.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| X | DataFrame | compulsory | | Dataframe containing feature variables |
| y | Series/DataFrame | compulsory | | Target Variable |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| lm | sklearn.ensemble.RandomForestRegressor | Fitted RandomForest Regression model |
