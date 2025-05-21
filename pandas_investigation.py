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

pivot = pd.pivot_table(
    df,
    index="product",
    columns="colour",
    values="quantity",
    aggfunc="sum",  # Sum quantities if there are duplicates
    fill_value=0    # Optional: replace NaN with 0
)

pivot['Totals'] = pivot.sum(axis=1)
print (pivot)

totals_row = pivot.sum(axis=0).to_frame().T
totals_row.index = ["Totals"]
print (totals_row)

# combine the pivot with the totals
pivot_with_totals = pd.concat([pivot, totals_row])

print (pivot_with_totals)







#pivot_table = df.pivot(index=['id'], columns=['colour'], values=['quantity'])

# pivot['Total'] = pivot.sum(axis=1)

# totals_row = pivot.sum(axis=0).to_frame().T
# totals_row.index = ['Grand Total']

# pivot_with_totals = pd.concat([pivot, totals_row])

# print (pivot_with_totals)

#df.to_csv('sales.csv', index=False)




#print (df)
#pivot_table = df.pivot(index=['id'], columns=['colour'], values=['quantity'])
#print (pivot_table)








