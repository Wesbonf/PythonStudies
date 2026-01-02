PESOS_PARA_USD =  0.00026
SOLES_PARA_USD = 0.30
REAIS_PARA_USD = 0.18


PESOS = int(input("Quanto você tem em pesos?: "))
SOLES = int(input("Quanto você tem em soles?: "))
REAIS = int(input("Quanto você tem em reais?: ")) 


CONV_PESOS = PESOS_PARA_USD * PESOS
CONV_SOLES = SOLES_PARA_USD * SOLES
CONV_REAIS = REAIS_PARA_USD * REAIS

TOTAL_USD = CONV_PESOS + CONV_SOLES + CONV_REAIS

print(f"Você tem um total de ${TOTAL_USD:.2f} USD")