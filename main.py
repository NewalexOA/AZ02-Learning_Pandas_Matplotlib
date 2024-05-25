import pandas as pd
from statistics import Statistics

df = pd.read_csv('data.csv', index_col='Фамилия')

stats = Statistics(df)
stats.print_stats()
