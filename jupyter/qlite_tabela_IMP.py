import pandas as pd
import sqlite3

# 1. Carregar o CSV (especificando o separador ;)
# O pandas transforma o "Excel" num DataFrame (tabela na memória)
df = pd.read_csv('g61_Elearning_Certificates1.csv', sep=';')

# 2. Conectar à base de dados SQLite
con = sqlite3.connect('Elearning.db')

# 3. Enviar os dados para o SQLite
# Isso cria uma tabela chamada 'dados_originais' com todo o conteúdo
df.to_sql('dados_originais', con, if_exists='replace', index=False)

print("Dados importados com sucesso!")
con.close()