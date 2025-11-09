import csv
from pathlib import Path
from collections import defaultdict

caminho = Path("C:/Users/rafad/Documents/Repositorios_Git/acelera/bootcamp_python/desafio-01/funcionarios.csv")

caminho_registros_validos = caminho.parent / "registros_validos.csv"
caminho_registros_invalidos = caminho.parent / "registros_invalidos.csv"
caminho_kpis = caminho / "kpis_funcionarios.csv"

def validar_registro(linha: list) -> list:
    if not linha[0].strip().isdigit():
        return "O campo ID deve conter apenas números."
    
    if any(char.isdigit() for char in linha[1]):
        return "O campo nome não pode conter dígitos."
    
    if not linha[1].strip():
        return "O campo nome não pode estar vazio."
    
    if linha[2] not in ['TI', 'Vendas', 'Financeiro', 'RH']:
        return "O departamento informado não é válido."
    
    try:
        salario = float(linha[3])
        if salario <= 0:
            return "O salário deve ser maior que zero."
    except ValueError:
        return "O valor informado para salário não é válido."
    
    try:
        percentual = float(linha[4])
        if not (0 <= percentual <= 1):
            return "O percentual deve estar entre 0 e 1."
    except ValueError:
        return "O valor informado para percentual não é válido."
    
    return None

BONUS_EXTRA = 1000

registros_validos = []
erros = []

with open(caminho, "r", encoding='utf-8') as f:
    leitor = csv.reader(f)
    cabecalho = next(leitor)
    
    for linha in leitor:
        erro = validar_registro(linha)
        if erro:
            erros.append((linha + [erro]))
        else:
            salario: float = float(linha[3])
            percentual: float = float(linha[4])
            bonus_final: float = BONUS_EXTRA + salario * percentual

            registros_validos.append(linha + [bonus_final])

with open(caminho_registros_validos, 'w', encoding='utf-8', newline='') as saida_validos:
    registro = csv.writer(saida_validos)
    registro.writerow(cabecalho + ["bonus_final"])
    registro.writerows(registros_validos)

with open(caminho_registros_invalidos, 'w', encoding="utf-8", newline='') as saida_erros:
    registro = csv.writer(saida_erros)
    registro.writerow(cabecalho + ["erro"])
    registro.writerows(erros)

registros = []

with open(caminho_registros_validos, "r", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        linha["salario"] = float(linha["salario"])
        linha["bonus_percentual"] = float(linha["bonus_percentual"])
        linha["bonus_final"] = float(linha["bonus_final"])
        registros.append(linha)

qtde_por_area = defaultdict(int)
for r in registros:
    qtde_por_area[r["area"]] +=1

print(qtde_por_area) 