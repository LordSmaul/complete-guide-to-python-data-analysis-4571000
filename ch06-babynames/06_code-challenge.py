# Python code​​​​​​‌‌‌​​​​​‌​​​​‌​​‌‌‌‌‌​​​‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

import pandas as pd

def unisex(allnames):
    # Your code goes here.
    allnames = allnames.set_index(['sex', 'name'])
    boys = allnames.loc['M', :]
    girls = allnames.loc['F', :]

    unisex = pd.merge(boys, girls, on='name')
    unisex['total'] = unisex.number_x + unisex.number_y
    unisex['ratio'] = unisex.number_x / unisex.number_y

    unisex = unisex[(0.5 < unisex.ratio) & (unisex.ratio < 2)]

    return unisex.sort_values('total', ascending=False).head(10).total