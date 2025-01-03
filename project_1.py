import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

df = pd.read_csv('titanic.csv')

# ------------------ #
# ANALISE            #
# ------------------ #

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

def calculate_milliseconds(age):
    if age == 0:
        return 0
    birthday = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc) - datetime.timedelta(days=age * 365.25)
    epoch = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
    return int((birthday - epoch).total_seconds() * 1000)

df['Age_Milliseconds'] = df['Age'].apply(calculate_milliseconds)

print(df.head())

print("-"*150)

survivals_by_sex = df.groupby('Sex')['Survived'].mean().reset_index()
survivals_by_sex['Survival Rate by Age'] = survivals_by_sex['Survived'] * 100
survivals_by_sex = survivals_by_sex[['Sex', 'Survival Rate by Age']]
print(survivals_by_sex)

print("-"*150)


survival_by_class = df.groupby('Pclass')['Survived'].mean().reset_index()
survival_by_class['Survival Rate by Class'] = (survival_by_class['Survived'] * 100).round(2)
survival_by_class = survival_by_class[['Pclass', 'Survival Rate by Class']]
print(survival_by_class)

print("-"*150)

filtered_df_no_null_data = df[df['Age'] > 0].copy()

filtered_df_no_null_data.loc[:, 'Age Group'] = pd.cut(
    filtered_df_no_null_data['Age'],
    bins=[0, 18, 65, filtered_df_no_null_data['Age'].max()],
    labels=['Young', 'Adult', 'Senior'],
    right=False
)

survival_by_age_group = filtered_df_no_null_data.groupby('Age Group', observed=False)['Survived'].mean().reset_index()
survival_by_age_group['Survival Rate'] = (survival_by_age_group['Survived'] * 100).round(2)

survival_by_age_group = survival_by_age_group[['Age Group', 'Survival Rate']]

print(survival_by_age_group)

print("-"*150)

filtered_fare = df[df['Fare'] > 0]

# tarifa media por classe e sexo
fare_mean_by_class_sex = filtered_fare.groupby(['Pclass', 'Sex'])['Fare'].mean().reset_index()

# tarifa media total por sexo
fare_by_sex = filtered_fare.groupby('Sex')['Fare'].mean().reset_index()
fare_by_sex.rename(columns={'Fare': 'Average Fare'}, inplace=True)

#tarifa media por classe (homens e mulheres juntos)
fare_mean_by_class = filtered_fare.groupby('Pclass')['Fare'].mean().reset_index()
fare_mean_by_class.rename(columns={'Fare': 'Average Fare'}, inplace=True)

fare_mean_by_class_sex['Average Fare'] = fare_mean_by_class_sex['Fare'].round(2)
fare_mean_by_class_sex = fare_mean_by_class_sex[['Pclass', 'Sex', 'Average Fare']]

fare_mean_by_class['Average Fare'] = fare_mean_by_class['Average Fare'].round(2)
fare_mean_by_class['Sex'] = 'Both'

#DataFrame para os totais por sexo
fare_total = pd.DataFrame({
    'Pclass': ['Total', 'Total'],
    'Sex': fare_by_sex['Sex'],
    'Average Fare': fare_by_sex['Average Fare'].round(2)
})

# Concatenar todas as tabelas
fare_final = pd.concat([fare_mean_by_class_sex, fare_mean_by_class, fare_total], ignore_index=True)

print(fare_final)

print("-"*150)

fare_survival_correlation = df[['Fare', 'Survived']].corr()
correlation = fare_survival_correlation.loc['Fare', 'Survived'].round(2)
print(correlation)

# ------------------ #
# GRAFICOS           #
# ------------------ #

# grafico distribuição de sobreviventes
# por classe e sexo
survivors_by_class_sex = df.groupby(['Pclass', 'Sex'])['Survived'].sum().reset_index()

plt.figure(figsize=(6,8))
sns.barplot(data=survivors_by_class_sex, x='Pclass', y='Survived', hue='Sex')
plt.title('Distribution of survivors by class and sex')
plt.xlabel('Class')
plt.ylabel('Number of survivors')
plt.legend(title='Sex')
plt.show()

