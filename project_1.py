import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

df = pd.read_csv('titanic.csv')

print(df.head())

print("-"*150)

print(df.tail())

print("-"*150)

print(df.info())

print("-"*150)

print(df.describe())

# tratamento de dados
df['Age'] = df['Age'].fillna(0) # Preencher valores nulos de 'Age' com 0
df['Cabin'] = df['Cabin'].fillna('N/A') # Preencher valores nulos de 'Cabin' com "N/A"
df['Fare'] = df['Fare'].fillna(0) # Preencher valores nulos de 'Fare' com 0

def calcular_milissegundos(idade):
    if idade == 0:
        return 0
    nascimento = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc) - datetime.timedelta(days=idade * 365.25)
    epoch = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
    return int((nascimento - epoch).total_seconds() * 1000)

df['Idade_Milissegundos'] = df['Age'].apply(calcular_milissegundos)

print(df.head())



