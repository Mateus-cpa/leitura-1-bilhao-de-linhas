import src.using_python_old as old_python
import src.using_python as new_python


path = "data/measurements.txt"

dados_op, tempo_op = old_python.processar_temperaturas(path_do_txt = path)
dados_np, tempo_np = new_python.processar_temperaturas(path_do_txt = path)
