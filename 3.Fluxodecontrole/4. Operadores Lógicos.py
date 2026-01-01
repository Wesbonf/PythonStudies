height = int(input("Qual é a sua altura (cm)? "))
credits = int(input("Quantos créditos você tem? "))

if height >= 137 and credits >= 10:
    print("Aproveite o passeio!")
elif credits >= 10 and height < 137:
    print("Você não é alto o suficiente para cavalgar")
elif height >= 137 and credits < 10:
    print("Você não tem créditos suficientes")
else:
    print("Você não atende a nenhum dos requisitos")
