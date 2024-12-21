#from multiprocessing import Pool, cpu_count
#from tqdm import tqdm  # importa o tqdm para barra de progresso
import pandas as pd

num_linhas = 1_000  # Total de linhas conhecido
path_do_txt = "data/measurements_1000.txt"  # Certifique-se de que este é o caminho correto para o arquivo


"""def process_chunk(chunk):
    # Agrega os dados dentro do chunk usando Pandas
    aggregated = chunk.groupby('station')['measure'].agg(['min', 'max', 'mean']).reset_index()
    return aggregated"""

def create_df_with_pandas(path_do_txt, num_linhas, chunksize=10_000):
    
    import time
    print(f"Iniciando o processamento do arquivo em PANDAS do arquivo com {num_linhas} linhas.")
    start_time = time.time()

    import pandas as pd
    #Constantes
    #chunksize = 100_000_000  # Define o tamanho de cada parte da subdivisão do dataframe
    #CONCURRENCY = cpu_count()

    
    print(f'Processando arquivo PANDAS com {num_linhas} linhas...')
    final_dfs = []
    for chunk in pd.read_csv(path_do_txt, sep=';', header=None, names=['station', 'measure'], chunksize=chunksize):
        final_df = chunk.groupby('station').agg(['min','max','mean']).reset_index().sort_values('station')
        final_dfs.append(final_df)
    
    final_aggregated_df = pd.concat(final_dfs)

    time_elapsed = time.time() - start_time

    print(f"Processamento no módulo PANDAS concluído em {time_elapsed:.3f} segundos.\n")

    return final_aggregated_df, time_elapsed

if __name__ == "__main__":
    
    final_aggregated_df, time_elapsed = create_df_with_pandas(path_do_txt, num_linhas)

 
