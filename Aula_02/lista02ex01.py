# 1. Ler quatro números inteiros, calcular a soma dos números pares e a soma dos números ímpares

numeros = []
somaimpar = 0
somapar = 0

for i in range(4):
    num = int(input("Digite seu numero pra eu te mostrar as somas de numeros pares e impares: "))
    if num % 2 == 0: somapar += num
    else: somaimpar += num

print(f'\nA soma de todos os números impares é de: {somaimpar}.')
print(f'A soma de todos os números pares é de: {somapar}.')