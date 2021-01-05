"""
Introduction to Pandas - Loading Data into Pandas
"""
import pandas as pd


"""
To load data from a csv file, we use the read_csv() method.
"""
path = '02_Pandas_Training/00_Data/developer_survey_2020/survey_results_public.csv'
df = pd.read_csv(path)
# print(df)

# To view the basic schematics of the data 
rows, col = df.shape
print('No of Rows: {} and Columns: {}'.format(rows,col))

# To view details schematics of the data
print(df.info())

pd.set_option('display.max_columns',61)
pd.set_option('display.max_rows',61)

# Loading the schema of the dataset. 
schema_path = '02_Pandas_Training/00_Data/developer_survey_2020/survey_results_schema.csv'
schema_df = pd.read_csv(schema_path)
print(schema_df)


# To see the first 5 rows, use df.head() method.
print(df.head())

# To see the last 5 rows, use df.head() method.
print(df.tail())
