ph = float(input("Digite o valor de PH: "))

if ph > 7:
    print('Básico')
elif ph < 7:
    print('Ácido')
else:
    print('Neutro')