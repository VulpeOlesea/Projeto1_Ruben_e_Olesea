# Análise de Dados do Titanic com Python  

Este projeto foi desenvolvido no contexto da **UFCD 5417 - Programação para a WEB - Servidor (server-side)**. O objetivo principal foi analisar os fatores que influenciaram a sobrevivência dos passageiros do Titanic, utilizando um conjunto de dados real e aplicando técnicas de análise de dados com **Python**.

---

## **Descrição do Projeto**  

O projeto consistiu em explorar um conjunto de dados que contém informações detalhadas sobre os passageiros do Titanic, com o objetivo de identificar padrões relevantes relacionados às taxas de sobrevivência. A análise foi feita com base nas seguintes etapas:  

1. **Pré-processamento dos Dados**  
   - Identificação e tratamento de valores em falta.  
   - Criação de novas colunas, como o tamanho da família e a idade em milissegundos, para suportar análises detalhadas.  

2. **Análise Exploratória dos Dados**  
   - Visualização de padrões e tendências usando bibliotecas como **Pandas**, **Matplotlib** e **Seaborn**.  
   - Geração de gráficos para analisar variáveis como idade, classe, sexo, porto de embarque e presença de familiares a bordo.  

3. **Armazenamento em Base de Dados**  
   - Os dados foram armazenados em uma base de dados SQLite, assegurando a organização e a possibilidade de consultas estruturadas no futuro.  

---

## **Tecnologias Utilizadas**  

- **Python**: Linguagem principal para análise de dados.  
- **Pandas**: Manipulação e agregação de dados.  
- **Matplotlib/Seaborn**: Visualização gráfica.  
- **SQLite**: Armazenamento de dados em base de dados relacional.  

---

## **Como Executar o Projeto**  

1. Clone este repositório:  
   ```bash
   git clone https://github.com/VulpeOlesea/Projeto1_Ruben_e_Olesea.git
   cd Projeto1_Ruben_e_Olesea

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   
3. Execute o script principal para gerar os gráficos e armazenar os dados na base de dados:
   ```bash
   python project_1.py

  ---

## **Gráficos e Visualizações**  
Alguns exemplos das análises geradas incluem:
- **Distribuição de Sobreviventes por Classe e Sexo**
- **Relação entre Idade e Tarifa**

---

## **Conclusão**
Este projeto destacou como fatores como o tamanho da família, a classe socioeconómica e o local de embarque influenciaram as chances de sobrevivência no Titanic. A utilização de Python e suas bibliotecas permitiu realizar uma análise detalhada e gerar insights relevantes a partir dos dados históricos.

---

## **Anexos**
- [Relatório de trabalho em forma de site](https://vulpeolesea.github.io/Projeto-Titanic-_Ruben_e_Olesea/)
- [Código fonte do site no GitHub](https://github.com/VulpeOlesea/Projeto-Titanic-_Ruben_e_Olesea)
