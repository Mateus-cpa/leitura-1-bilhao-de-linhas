def create_duckdb(path_do_txt: str, num_linhas: int):
    import duckdb
    import time

    start_time = time.time()

    path_do_txt = path_do_txt

    query = """
        SELECT station,
            MIN(temperature) AS min_temperature,
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperature) AS max_temperature
        FROM read_csv('""" + path_do_txt + """', AUTO_DETECT=FALSE, sep=';', columns={'station':VARCHAR, 'temperature': 'DECIMAL(3,1)'})
        GROUP BY station
        ORDER BY station"""

    db_duck = duckdb.sql(query = query).show()
    

    time_elapsed = time.time() - start_time
    print(f"Duckdb demorou {time_elapsed:.3f} segundos para ler {num_linhas} linhas.")
    return db_duck,time_elapsed


if __name__ == "__main__":
    db = create_duckdb(path_do_txt='data\measurements_10000.txt', num_linhas= 10000)
    
