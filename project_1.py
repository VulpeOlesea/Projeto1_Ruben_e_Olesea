import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import sqlite3

# Carregamento de dados de um ficheiro CSV
df = pd.read_csv('titanic.csv')

# ------------------ #
#      ANALISE       #
# ------------------ #

# Mostrar as primeiras 5 linhas
print("# Mostrar as primeiras 5 linhas #\n")
print(df.head())

print("-"*150)

# Mostrar as últimas 5 linhas
print("# Mostrar as últimas 5 linhas #\n")
print(df.tail())

print("-"*150)
# ---------------------------------------------------------- #
# Informações gerais sobre o conjunto de dados
print("# Informações gerais sobre o conjunto de dados #\n")
print(df.info())

print("-"*150)

# Estatísticas descritivas para dados numéricos
print("# Estatísticas descritivas para dados numéricos #\n")
print(df.describe())

print("-"*150)
# ---------------------------------------------------------- #
# Identificar valores nulos
df['Age'] = df['Age'].fillna(0) # Valores nulos de 'Age' com 0
df['Cabin'] = df['Cabin'].fillna('N/A') # Valores nulos de 'Cabin' com "N/A"0.0
df['Fare'] = df['Fare'].fillna(0) # Preencher valores nulos de 'Fare' com 0

# ---------------------------------------------------------- #
def calculate_milliseconds(age):
    """
    Calcula o número de milissegundos decorridos desde a época Unix (1 de janeiro de 1970)
    até uma data fornecida.

    Param:
    - age (int): A idade em anos para calcular a data de nascimento relativa à época Unix.
    Return:
    - int: O número de milissegundos decorridos desde 1 de janeiro de 1970 até a data correspondente.
    """
    if age == 0:
        return 0
    birthday = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc) - datetime.timedelta(days=age * 365.25)
    epoch = datetime.datetime(1970, 1, 1, tzinfo=datetime.timezone.utc)
    return int((birthday - epoch).total_seconds() * 1000)

# Criar uma coluna chamada Idade_Milissegundos
print("# Criar uma nova coluna chamada Idade_Milissegundos #\n")
df['Age_Milliseconds'] = df['Age'].apply(calculate_milliseconds)

print(df.head())

print("-"*150)
# ---------------------------------------------------------- #
# Calcular a taxa de sobrevivência por sexo (Sex)
print("# Calcular a taxa de sobrevivência por sexo (Sex) #\n")
survivals_by_sex = df.groupby('Sex')['Survived'].mean().reset_index()
survivals_by_sex['Survival Rate by Age'] = survivals_by_sex['Survived'] * 100
survivals_by_sex = survivals_by_sex[['Sex', 'Survival Rate by Age']]
print(survivals_by_sex)

print("-"*150)
# ---------------------------------------------------------- #
# Calcular a taxa de sobrevivência por classe (Pclass)
print("# Calcular a taxa de sobrevivência por classe (Pclass) #\n")
survival_by_class = df.groupby('Pclass')['Survived'].mean().reset_index()
survival_by_class['Survival Rate by Class'] = (survival_by_class['Survived'] * 100).round(2)
survival_by_class = survival_by_class[['Pclass', 'Survival Rate by Class']]
print(survival_by_class)

print("-"*150)
# ---------------------------------------------------------- #
# Calcular a taxa de sobrevivência por faixa etária (Age Group)
filtered_df_no_null_data = df[df['Age'] > 0].copy()

filtered_df_no_null_data.loc[:, 'Age Group'] = pd.cut(
    filtered_df_no_null_data['Age'],
    bins=[0, 18, 65, filtered_df_no_null_data['Age'].max()],
    labels=['Young', 'Adult', 'Senior'],
    right=False
)

print("# Calcular a taxa de sobrevivência por faixa etária (Age Group) #\n")
survival_by_age_group = filtered_df_no_null_data.groupby('Age Group', observed=False)['Survived'].mean().reset_index()
survival_by_age_group['Survival Rate'] = (survival_by_age_group['Survived'] * 100).round(2)

survival_by_age_group = survival_by_age_group[['Age Group', 'Survival Rate']]

print(survival_by_age_group)

print("-"*150)
# ---------------------------------------------------------- #
# Calcular a tarifa média por classe e sexo:
print("# Calcular a tarifa média por classe e sexo #\n")
filtered_fare = df[df['Fare'] > 0]

# Tarifa media por classe e sexo
fare_mean_by_class_sex = filtered_fare.groupby(['Pclass', 'Sex'])['Fare'].mean().reset_index()

# Tarifa media total por sexo
fare_by_sex = filtered_fare.groupby('Sex')['Fare'].mean().reset_index()
fare_by_sex.rename(columns={'Fare': 'Average Fare'}, inplace=True)

# Tarifa media por classe (homens e mulheres juntos)
fare_mean_by_class = filtered_fare.groupby('Pclass')['Fare'].mean().reset_index()
fare_mean_by_class.rename(columns={'Fare': 'Average Fare'}, inplace=True)

fare_mean_by_class_sex['Average Fare'] = fare_mean_by_class_sex['Fare'].round(2)
fare_mean_by_class_sex = fare_mean_by_class_sex[['Pclass', 'Sex', 'Average Fare']]

fare_mean_by_class['Average Fare'] = fare_mean_by_class['Average Fare'].round(2)
fare_mean_by_class['Sex'] = 'Both'

# DataFrame para os totais por sexo
fare_total = pd.DataFrame({
    'Pclass': ['Total', 'Total'],
    'Sex': fare_by_sex['Sex'],
    'Average Fare': fare_by_sex['Average Fare'].round(2)
})

# Concatenar todas as tabelas
fare_final = pd.concat([fare_mean_by_class_sex, fare_mean_by_class, fare_total], ignore_index=True)

print(fare_final)

print("-"*150)
# ---------------------------------------------------------- #
# Correlações entre a tarifa (Fare) e a sobrevivência
print("# Correlações entre a tarifa (Fare) e a sobrevivência #\n")
fare_survival_correlation = df[['Fare', 'Survived']].corr()
correlation = fare_survival_correlation.loc['Fare', 'Survived'].round(2)
print(correlation)

print("-"*150)
# ------------------ #
# GRAFICOS           #
# ------------------ #

# Grafico distribuição de sobreviventes
# Por classe e sexo
survivors_by_class_sex = df.groupby(['Pclass', 'Sex'])['Survived'].sum().reset_index()

# Distribuição de Sobreviventes por Classe e Sexo
plt.figure(figsize=(6,8))
sns.barplot(data=survivors_by_class_sex, x='Pclass', y='Survived', hue='Sex')
plt.title('Distribuição de Sobreviventes por Classe e Sexo')
plt.xlabel('Classe')
plt.ylabel('Numero de sobreviventes')
plt.legend(title='Sexo')
plt.show()

# Relação entre Idade e Tarifa
plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived', palette='muted')
plt.title('Relação entre Idade e Tarifa')
plt.xlabel('Idade')
plt.ylabel('Tarifa')
plt.legend(title='Sobreviveu')
plt.show()

# Histogramas para visualizar a distribuição de Age,Fare,e Survived
# Distribuição de Idade (Age)
plt.figure(figsize=(8,6))
sns.histplot(data=df, x='Age', bins=30, kde=True, color='green')
plt.title('Distribuição de Idade')
plt.xlabel('Idade')
plt.ylabel('Quantidade')
plt.show()

# Distribuição da Tarifa (Fare)
plt.figure(figsize=(8,6))
sns.histplot(data=df, x='Fare', bins=30, kde=True, color='green')
plt.title('Distribuição da Tarifa')
plt.xlabel('Tarifa')
plt.ylabel('Quantidade')
plt.show()

# Distribuição de Sobreviventes (Survived)
plt.figure(figsize=(6,4))
sns.countplot(data=df, x='Survived', hue='Survived', palette='muted')
plt.title('Distribuição de Sobreviventes')
plt.xlabel('Sobreviveu')
plt.ylabel('Quantidade')
plt.xticks([0, 1], ['Não', 'Sim'])
plt.show()

# ------------------------- #
# Exportação dos resultados #
# ------------------------- #

df.to_excel('titanic_milliseconds.xlsx', index=False)

# ------------------------- #
#         Data base         #
# ------------------------- #

# Conectar à base de dados SQLite
conn = sqlite3.connect('titanic.db')
cursor = conn.cursor()

# Criar a tabela "passengers"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passengers (
        PassengerId INTEGER PRIMARY KEY,
        Survived INTEGER,
        Pclass INTEGER,
        Name TEXT,
        Sex TEXT,
        Age REAL,
        SibSp INTEGER,
        Parch INTEGER,
        Ticket TEXT,
        Fare REAL,
        Cabin TEXT,
        Embarked TEXT,
        Age_Milliseconds INTEGER
    )
''')

# Inserir os dados do DataFrame 'df' na tabela "passengers"
df.to_sql('passengers', conn, if_exists='replace', index=False)

# Mostrar os 5 primeiros registos da tabela "passengers"
print("# Mostrar os 5 primeiros registos da tabela 'passengers' #\n")
cursor.execute('SELECT * FROM passengers LIMIT 5')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Fechar a conexão com a base de dados
conn.close()

# ------------------------- #
#     Análise Adicional     #
# ------------------------- #

