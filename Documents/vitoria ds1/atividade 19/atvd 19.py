# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.
def calcular_fatorial(n):
    if n < 0:
        return "Fatorial não definido para números negativos."
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

# Receber o número do usuário
numero = int(input("Digite um número inteiro: "))
resultado = calcular_fatorial(numero)

print(f"O fatorial de {numero} é: {resultado}")
