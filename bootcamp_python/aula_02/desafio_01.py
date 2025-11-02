### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

try: 
    nome = input("Digite seu nome: ").strip()
    
    if not nome:
        print("Você não digitou nenhum valor!")
        exit()

    elif nome.isdigit():
        print("Você digitou um numero ao inves de texto!")
        exit()   

    else:
        pass
except ValueError as e:
    print(f"Erro ao processar o nome {e}")
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário
try: 
    salario = float(input('Digite o seu salario: '))
    if salario <= 0:
        print("Você digitou um valor invalido para salário!")
        exit()
    else: 
        pass
except ValueError as e:
    print(f"O valor {e} digitado para salário está incorreto!")
    exit()

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try: 
    bonus = float(input('Digite o valor do bonus recebido: '))
    
except ValueError as e:
    print(f"O valor {e} digitado para bonus não está correto")
    exit()

# 4) Calcule o valor do bônus final

BONUS_EXTRA = float(1000)

total_do_salario = BONUS_EXTRA + ((bonus/100)* salario) + salario

print(f'{nome} o valor total do seu salário + bonus é de {total_do_salario:.2f}')


