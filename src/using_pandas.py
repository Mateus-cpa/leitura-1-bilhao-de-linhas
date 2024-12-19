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
    import pandas as pd
 
    #Constantes
    #chunksize = 100_000_000  # Define o tamanho de cada parte da subdivisão do dataframe
    #CONCURRENCY = cpu_count()

    import time

    print("Iniciando o processamento do arquivo.")
    start_time = time.time()

    """    total_chunks = num_linhas // chunksize + (1 if num_linhas % chunksize else 0)
    results = []

    # Regula Barra de progresso
    if total_chunks > num_linhas:
        total_bar_progress = num_linhas
    else:
        total_bar_progress = total_chunks

    with pd.read_csv(path_do_txt, sep=';', header=None, names=['station', 'measure'], chunksize=chunksize) as reader:        
        # Envolvendo o iterador com tqdm para visualizar o progresso
        with Pool(CONCURRENCY) as pool:
            for chunk in tqdm(reader, total=total_chunks, desc="Processando"):
                # Processa cada chunk em paralelo
                result = pool.apply_async(process_chunk, (chunk,))
                results.append(result)
    


            results = [result.get() for result in results]

    final_df = pd.concat(results, ignore_index=True)"""
    print(f'Processando arquivo com {num_linhas} linhas...')
    final_dfs = []
    for chunk in pd.read_csv(path_do_txt, sep=';', header=None, names=['station', 'measure'], chunksize=chunksize):
        final_df = chunk.groupby('station').agg(['min','max','mean']).reset_index().sort_values('station')
        final_dfs.append(final_df)
    
    final_aggregated_df = pd.concat(final_dfs)

    time_elapsed = time.time() - start_time

    print(f"Tempo de processamento em pandas durou: {time_elapsed:.2f} segundos")

    return final_aggregated_df, time_elapsed

if __name__ == "__main__":
    
    final_aggregated_df, time_elapsed = create_df_with_pandas(path_do_txt, num_linhas)

 
