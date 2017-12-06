# Fitting your first gradientboosting regression model

## Let's write a function `gradientboosting_regressor()` that
* Takes as input the features and target
* Fits a gradientboosting_regressor with default parameters model on it.

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| X | DataFrame | compulsory | | Dataframe containing feature variables |
| y | Series/DataFrame | compulsory | | Target Variable |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| lm | sklearn.ensemble.GradientBoostingRegressor | Fitted GradientBoosting Regression model |
