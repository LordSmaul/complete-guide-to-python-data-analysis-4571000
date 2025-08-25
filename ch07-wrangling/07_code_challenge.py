# Python code​​​​​​‌‌‌​​​​​‌​‌​‌​​‌‌‌​‌​​​​​ below
# Use print("messages...") to debug your solution.

show_expected_result = True
show_hints = False

import pandas as pd

def rankcountries(medals):

    counts = medals.groupby('Medal').Country.value_counts().unstack(level=0).fillna(0)
    counts['Total'] = counts.sum(axis=1)

    return counts.sort_values(['Total', 'Gold', 'Silver', 'Bronze'], ascending=False).head(4)