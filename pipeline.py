#import src.create_measurements as create_files
import src.using_python_old as old_python
import src.using_python as new_python
from src.using_pandas import create_df_with_pandas as pandas
from src.using_polars import create_polars_df as polars
from src.using_duckdb import create_duckdb as duck

import pandas as pd
import matplotlib.pyplot as plt


#create_files.main()

lista_num_linhas = [10000,100000,1000000]#,10000000,100000000] #adicionar Bilhão após testes ,1000000000]

df_tempos_de_execucao = pd.DataFrame(columns=['num_linhas', 'metodo', 'tempo (s)'])


for num_linhas in lista_num_linhas:
    dict_to_append = []
    path = f"data/measurements_{num_linhas}.txt"

    # Processa os dados e obtém os tempos
    dados_op, tempo_op = old_python.processar_temperaturas(path_do_txt=path)
    dados_np, tempo_np = new_python.processar_temperaturas(path_do_txt=path, num_linhas=num_linhas)
    df_final, tempo_pd = pandas(path_do_txt=path, num_linhas=num_linhas)
    df_polars, tempo_pl = polars(path_do_txt=path, num_linhas=num_linhas)
    db_duck, tempo_dk = duck(path_do_txt=path, num_linhas=num_linhas)


    # Cria um novo DataFrame com os resultados da iteração e concatena com o DataFrame principal
    
    dict_to_append.append({'num_linhas': num_linhas, 'metodo': 'método antigo python', 'tempo (s)': tempo_op})
    dict_to_append.append({'num_linhas': num_linhas, 'metodo': 'método novo python', 'tempo (s)': tempo_np})
    dict_to_append.append({'num_linhas': num_linhas, 'metodo': 'pandas', 'tempo (s)': tempo_pd})
    dict_to_append.append({'num_linhas': num_linhas, 'metodo': 'polars', 'tempo (s)': tempo_pl})
    dict_to_append.append({'num_linhas': num_linhas, 'metodo': 'duckdb', 'tempo (s)': tempo_dk})

    df_to_append = pd.DataFrame(dict_to_append) #transforma dicionário em dataframe
    df_tempos_de_execucao = pd.concat([df_tempos_de_execucao,df_to_append])
    df_tempos_de_execucao.reset_index()

print(df_tempos_de_execucao)

# Organiza dataframe para montar o gráfico
grouped = df_tempos_de_execucao.groupby('metodo')

# Gera gráfico de linha
fig, ax = plt.subplots()

# Plota cada linha:
for name, group in grouped:
    ax.plot(group['num_linhas'], group['tempo (s)'], label=name)
    for x, y in zip(group['num_linhas'], group['tempo (s)']):
        ax.annotate(f"{y:.3f}", (x, y), textcoords="offset points", xytext=(0,10), ha='center')

# Configurando o gráfico
ax.set_xlabel('Número de Linhas', fontsize=14)
ax.set_ylabel('Tempo de Execução (segundos)', fontsize=14)
ax.set_title('Comparação de Desempenho', fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='lower right')
ax.set_yscale('log') # Escala logarítmica no eixo y 
ax.set_xscale('log') # Escala logarítmica no eixo x
plt.savefig('results/gráfico_comparativo.png', dpi=300)
plt.show()