import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('titanic.csv')

print(df.head())

print("-"*150)

print(df.tail())

print("-"*150)

print(df.info())

print("-"*150)

print(df.describe())


