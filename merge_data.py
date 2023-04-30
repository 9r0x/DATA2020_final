import pandas as pd

basic_df = pd.read_csv('data/pokemon_basic.csv')
extended_df = pd.read_csv('data/pokemon_extended.csv')
merged_df = pd.merge(basic_df,
                     extended_df,
                     left_on='Name',
                     right_on='pokemon_name')
merged_df.to_csv('data/pokemon_merged.csv', index=False)