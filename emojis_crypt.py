import os
import pandas as pd


print(os.getcwd())

df = pd.read_csv('emojis.csv')

print(df.head())

print(df.Emoji[1])