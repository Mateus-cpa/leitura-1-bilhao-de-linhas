num_linhas = 1_000_000

def processar_temperaturas(path_do_txt: str, num_linhas: int):
    print(f"Iniciando o processamento em PYTHON do arquivo com {num_linhas} linhas.")
    import time    
    start_time = time.time()  # Tempo de início
    from csv import reader
    from collections import defaultdict, Counter
    from tqdm import tqdm  # barra de progresso
    

    #from pathlib import Path


    # utilizando infinito positivo e negativo para comparar
    minimas = defaultdict(lambda: float('inf'))
    maximas = defaultdict(lambda: float('-inf'))
    somas = defaultdict(float)
    medicoes = Counter()

    with open(path_do_txt, 'r', encoding='utf-8') as file:
        _reader = reader(file, delimiter=';')
        # usando tqdm diretamente no iterador, isso mostrará a porcentagem de conclusão.
        for row in tqdm(_reader, total=num_linhas, desc="Processando Python"):
            nome_da_station, temperatura = str(row[0]), float(row[1])
            medicoes.update([nome_da_station])
            minimas[nome_da_station] = min(minimas[nome_da_station], temperatura)
            maximas[nome_da_station] = max(maximas[nome_da_station], temperatura)
            somas[nome_da_station] += temperatura

    print(f"Dados carregados em PYTHON com {num_linhas} linhas. Calculando estatísticas...")

    # calculando min, média e max para cada estação
    results = {}
    for station, qtd_medicoes in medicoes.items():
        mean_temp = somas[station] / qtd_medicoes
        results[station] = (minimas[station], mean_temp, maximas[station])

    print(f"Estatística calculada em PTYHON com {num_linhas} linhas. Ordenando...")
    # ordenando os resultados pelo nome da estação
    sorted_results = dict(sorted(results.items()))

    # formatando os resultados para exibição
    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}"
                         for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}
    
    
    time_elapsed = time.time() - start_time 

    print(f"Processamento no módulo PYTHON concluído em {time_elapsed:.3f} segundos.\n")

    return formatted_results, time_elapsed


if __name__ == "__main__":
    path_do_txt = "data/measurements.txt"

    resultados = processar_temperaturas(path_do_txt)
