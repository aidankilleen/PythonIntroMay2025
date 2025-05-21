# pandas_investigation.py

import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Carol'], 
    'Age': [35, 45, 22], 
    'City': ['Cork', 'Dublin', 'Limerick']
}

df = pd.DataFrame(data)

print (df)

print (df['Name'])

print (df[['Name', 'City']])

# filtering
print (df[df['Age'] > 30])


# add columns
df['Junior'] = df['Age']<30

print (df)

# create a df from a csv / json file

df = pd.read_json("sales.json")

df.to_csv('sales.csv', index=False)




#print (df)
#pivot_table = df.pivot(index=['id'], columns=['colour'], values=['quantity'])
#print (pivot_table)








