# Feature Engineering

## Let's write a function `fe()` that
* Takes as input the dataset and column name which contains time variable

### Parameters:

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| X | DataFrame | compulsory | | Dataframe containing feature variables |
| time_col | str | compulsory | | A string which represents the time column present in the data


## Function operations:
-----------------------
- Convert the time_col to datetime format using pandas to_datetime api
- Extract the **hour** from time_col (int)
- Extract the **month** from time_col (int)

### Returns:

| Return | dtype | description |
| --- | --- | --- |
| X | dataframe | A new data frame with created features |
