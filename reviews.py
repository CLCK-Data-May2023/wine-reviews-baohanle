# add your code here

# 

import pandas as pd
import zipfile

# with zipfile.ZipFile('data\winemag-data-130k-v2.csv.zip', 'r') as zip_ref:
#     zip_ref.extract('data\winemag-data-130k-v2.csv', 'data')

df = pd.read_csv('data\winemag-data-130k-v2.csv.zip')

country_count = df.country.value_counts().reset_index()
country_count.columns = ['country','count']

points = df.groupby('country').points.mean().round(1)
final = pd.merge(country_count, points, on='country')

# reviews = df.loc[:, ['country','count','points']]

final.to_csv('data/reviews-per-country.csv')

