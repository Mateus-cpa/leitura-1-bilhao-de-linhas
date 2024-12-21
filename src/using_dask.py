def create_dask_df(path_do_txt: str, num_linhas: int):
    print(f"Iniciando o processamento do arquivo em DASK do arquivo com {num_linhas} linhas.")
    import time    
    start_time = time.time()
    import dask
    import dask.dataframe as dd


    

    dask.config.set({'dataframe.query-planning': True})
    # Configurando o Dask DataFrame para ler o arquivo CSV
    # Como o arquivo não tem cabeçalho, especificamos os nomes das colunas manualmente
    df = dd.read_csv(path_do_txt, sep=";", header=None, names=["station", "measure"])
    
    # Agrupando por 'station' e calculando o máximo, mínimo e média de 'measure'
    # O Dask realiza operações de forma lazy, então esta parte apenas define o cálculo
    grouped_df = df.groupby("station")['measure'].agg(['max', 'min', 'mean']).reset_index()

    # O Dask não suporta a ordenação direta de DataFrames agrupados/resultantes de forma eficiente
    # Mas você pode computar o resultado e então ordená-lo se o dataset resultante não for muito grande
    # ou se for essencial para a próxima etapa do processamento
    # A ordenação será realizada após a chamada de .compute(), se necessário

    # O cálculo real e a ordenação são feitos aqui
    result_df = grouped_df.compute().sort_values("station")

    time_elapsed = time.time() - start_time

    print(f"Processamento no módulo DASK concluído em {time_elapsed:.3f} segundos.\n")

    return result_df, time_elapsed

if __name__ == "__main__":
    
    df = create_dask_df(path_do_txt="data/measurements_10000.txt", num_linhas=10000)   

    print(df)
    
