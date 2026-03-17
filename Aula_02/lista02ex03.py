#Ler 4 valores inteiros diferentes e realizar as seguintes operações: verificar se os valores são realmente diferentes
#e mostrar uma mensagem de erro, caso contrário; mostrar o maior valor lido; mostrar o menor valor lido e mostrar o
#resultado da soma entre o segundo maior valor e o segundo menor.

numeros = []

while (len(numeros) < 4):
    num = int(input("Digite um valor inteiro diferente para eu te exibir o maior, o menor e a soma do segundo maior com o segundo menor: "))
    if num in numeros: print("Valor ja foi digitado, por favor digite um valor diferente.") 
    else: numeros.append(num)

numeros.sort() #ordenando a lista para facilitar na identificação dos números

print(f'\n O maior valor digitado é: {numeros[3]}')
print(f' O menor valor digitado é: {numeros[0]}')
print(f' A soma do segundo maior valor com o segundo menor é de: {numeros[1] + numeros[2]}')