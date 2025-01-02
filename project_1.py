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

print("-"*150)

df['Age'] = df['Age'].fillna(0) # valores nulos de 'Age' com 0
df['Cabin'] = df['Cabin'].fillna('N/A') #valores nulos de 'Cabin' com "N/A"0.0
df['Fare'] = df['Fare'].fillna(0) # Preencher valores nulos de 'Fare' com 0

def calcular_milissegundos(idade):
    if idade == 0:
        return 0
    nascimento = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc) - datetime.timedelta(days=idade * 365.25)
    epoch = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
    return int((nascimento - epoch).total_seconds() * 1000)

df['Idade_Milissegundos'] = df['Age'].apply(calcular_milissegundos)

print(df.head())

print("-"*150)

survival_rate_by_sex = df.groupby('Sex')['Survived'].mean().reset_index()
survival_rate_by_sex['Survival Rate by Age'] = survival_rate_by_sex['Survived'] * 100
survival_rate_by_sex = survival_rate_by_sex[['Sex', 'Survival Rate by Age']]
print(survival_rate_by_sex)

print("-"*150)


survival_rate_by_class = df.groupby('Pclass')['Survived'].mean().reset_index()
survival_rate_by_class['Survival Rate by Class'] = (survival_rate_by_class['Survived'] * 100).round(2)
survival_rate_by_class = survival_rate_by_class[['Pclass', 'Survival Rate by Class']]
print(survival_rate_by_class)

print("-"*150)

