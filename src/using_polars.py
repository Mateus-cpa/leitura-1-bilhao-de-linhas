
# Created by Koen Vossen, 
# Github: https://github.com/koenvo
# Twitter/x Handle: https://twitter.com/mr_le_fox
# https://x.com/mr_le_fox/status/1741893400947839362?s=20

def create_polars_df(path_do_txt, num_linhas: int):
    print(f'Iniciando processamento em POLARS com {num_linhas} linhas.')
    import time

    start_time = time.time()
    
    import polars as pl

    pl.Config.set_streaming_chunk_size(4000000)

    df_polars = pl.scan_csv(path_do_txt, 
                            separator=";", 
                            has_header=False, 
                            new_columns=["station", "measure"], 
                            schema={"station": pl.String, "measure": pl.Float64})
    df_polars = df_polars.group_by(by="station")
    print(f'Processando arquivo em POLARS com {num_linhas} linhas.')

    df_polars = df_polars.agg(
            max = pl.col("measure").max(),
            min = pl.col("measure").min(),
            mean = pl.col("measure").mean())
    df_polars = df_polars.sort("by") #pois a coluna 'station' deixou de ser acessível após agrupado
    df_polars = df_polars.collect(streaming=True)
    
    time_elapsed = time.time() - start_time
    print(f"Processamento no módulo POLARS concluído em {time_elapsed:.3f} segundos.\n")
    return (df_polars, time_elapsed)

if __name__ == "__main__":
    
    df, time = create_polars_df(path_do_txt='data\measurements_10000.txt', num_linhas = 10000)
    
    print(time)
