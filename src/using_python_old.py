from csv import reader
from collections import defaultdict
import time

from pathlib import Path

def processar_temperaturas(path_do_txt: Path):
    print("Iniciando o processamento do arquivo.")
    start_time = time.time()  # Tempo de início

    temperatura_por_station = defaultdict(list)

    """
        Exemplo de como vai ficar a variável temperatura_por_station
        temperatura_por_station = {
            'Hamburg': [12.0],
            'Bulawayo': [8.9],
            'Palembang': [38.8],
            'St. John's': [15.2],
            'Cracow': [12.6],
            'Bridgetown': [26.9],
            'Istanbul': [6.2, 23.0], # Note que Istanbul tem duas entradas
            'Roseau': [34.4],
            'Conakry': [31.2],
        }
        O uso de defaultdict do módulo collections é uma escolha conveniente 
        Sem o defaultdict, o código para adicionar uma temperatura iria parecer com isso:
        if nome_da_station not in temperatura_por_station:
            temperatura_por_station[nome_da_station] = []
        temperatura_por_station[nome_da_station].append(temperatura)
        Com defaultdict, isso é simplificado para:
        temperatura_por_station[nome_da_station].append(temperatura)
    """

    with open(path_do_txt, 'r', encoding="utf-8") as file:
        _reader: reader = reader(file, delimiter=';')
        for row in _reader:
            nome_da_station, temperatura = str(row[0]), float(row[1])
            temperatura_por_station[nome_da_station].append(temperatura)

    print("Dados carregados. Calculando estatísticas...")

    # Dicionário para armazenar os resultados calculados
    results = {}

    # Calculando min, média e max para cada estação
    for station, temperatures in temperatura_por_station.items():
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        results[station] = (min_temp, mean_temp, max_temp)

    print("Estatística calculada. Ordenando...")
    # Ordenando os resultados pelo nome da estação
    sorted_results = dict(sorted(results.items()))

    # Formatando os resultados para exibição
    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}" for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    end_time = time.time()  # Tempo de término

    time_elapsed = end_time - start_time
    print(f"Processamento no módulo python_old concluído em {time_elapsed:.2f} segundos.")

    return formatted_results, time_elapsed

if __name__ == "__main__":

    # 1M 0.38 segundos
    # 10M 3.96 segundos.
    path_do_txt: Path = Path("data/measurements.txt")
    # 100M > 5 minutos.
    resultados = processar_temperaturas(path_do_txt)