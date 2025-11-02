### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
nome = False
salario_padrao = False
bonus = False

while nome is not True:
    try: 
        nome = input("Digite seu nome: ").strip()
        
        if not nome:
            print("Você não digitou nenhum valor!")

        elif nome.isdigit():
            print("Você digitou um valor invalido para o campo nome!")

        else:
            nome = True
    except ValueError as e:
        print(f"Erro ao processar o nome {e}")
        exit()

# 2) Solicita ao usuário que digite o valor do seu salário
while salario_padrao is not True: 
    try: 
        salario = float(input('Digite o seu salario: '))
        if salario <= 0:
            print("Você digitou um valor invalido para salário!")
        else: 
            salario_padrao = True
    except ValueError as e:
        print(f"O valor {e} digitado para salário está incorreto!")

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
while bonus is not True:    
    try: 
        bonus_informado = float(input('Digite o valor do bonus recebido: '))
        if bonus_informado < 0:
            print("o valor digitado para bonus não pode ser menor que 0")
        else:
            bonus = True
        
    except ValueError as e:
        print(f"O valor {e} digitado para bonus não está correto")

# 4) Calcule o valor do bônus final

BONUS_EXTRA = float(1000)

if bonus_informado == 0:
    resultado = BONUS_EXTRA + salario
    print(f'o Valor total do seu bonus é de {resultado:.2f} ')
else:
    resultado = BONUS_EXTRA + (bonus_informado/100*salario) + salario
    print(f'o Valor total do seu bonus é de {resultado:.2f}')


