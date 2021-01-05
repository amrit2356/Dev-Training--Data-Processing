"""
Implementation of Dataframes and Series
"""

import pandas as pd

"""
Creation of Dataframes using Dictionary and Lists

"""

people = {
    "First" : ["Corey", "Jane", "John"],
    "Last" : ["Schafer", "Doe", "Doe"],
    "Email": ["abc@email.com","def@email.com","ghi@email.com"]
}

df = pd.DataFrame(people)
print(df)


print(type(df['Email']))