from csv import reader
from collections import defaultdict, Counter
from tqdm import tqdm  # barra de progresso
import time
from pathlib import Path


num_linhas = 1_000_000

def processar_temperaturas(path_do_txt: Path, num_linhas: int):
    print("Iniciando o processamento do arquivo.")
    start_time = time.time()  # Tempo de início

    # utilizando infinito positivo e negativo para comparar
    minimas = defaultdict(lambda: float('inf'))
    maximas = defaultdict(lambda: float('-inf'))
    somas = defaultdict(float)
    medicoes = Counter()

    with open(path_do_txt, 'r', encoding='utf-8') as file:
        _reader = reader(file, delimiter=';')
        # usando tqdm diretamente no iterador, isso mostrará a porcentagem de conclusão.
        for row in tqdm(_reader, total=num_linhas, desc="Processando"):
            nome_da_station, temperatura = str(row[0]), float(row[1])
            medicoes.update([nome_da_station])
            minimas[nome_da_station] = min(minimas[nome_da_station], temperatura)
            maximas[nome_da_station] = max(maximas[nome_da_station], temperatura)
            somas[nome_da_station] += temperatura

    print("Dados carregados. Calculando estatísticas...")

    # calculando min, média e max para cada estação
    results = {}
    for station, qtd_medicoes in medicoes.items():
        mean_temp = somas[station] / qtd_medicoes
        results[station] = (minimas[station], mean_temp, maximas[station])

    print("Estatística calculada. Ordenando...")
    # ordenando os resultados pelo nome da estação
    sorted_results = dict(sorted(results.items()))

    # formatando os resultados para exibição
    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}"
                         for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}
    
    
    end_time = time.time()  # Tempo de término

    time_elapsed = end_time - start_time 

    print(f"\nProcessamento no módulo python concluído em {time_elapsed:.2f} segundos.")

    return formatted_results, time_elapsed


if __name__ == "__main__":
    path_do_txt = "data/measurements.txt"

   

    resultados = processar_temperaturas(path_do_txt)


    #for station, metrics in resultados.items():
    #    print(station, metrics, sep=': ')

