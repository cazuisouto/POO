#Ler o número do mês (1 – janeiro; 2 – fevereiro; ...; 12 – dezembro) e identificar o nome do mês e em que trimestre
#o mês está incluído.

meses = {'primeiro': [{1: 'janeiro'}, {2: 'fevereiro'}, {3: 'março'}], 
        'segundo': [{4: 'abril'}, {5: 'maio'}, {6: 'junho'}],
        'terceiro': [{7: 'julho'}, {8: 'agosto'}, {9: 'setembro'}],
        'quarto': [{10: 'outubro'}, {11: 'novembro'}, {12: 'dezembro'}]}

num = int(input("Digite o número do mês (1-12): "))

for trim in meses:
    for mes in meses[trim]:
        if num in mes:
            print(f'\nO mês de {mes[num]} é do {trim} trimestre do ano.')
        else: 
            print("Número do mês inválido. Por favor, digite um número entre 1 e 12.")


