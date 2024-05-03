# Cálculo IMC

alt = float(input('Insira sua altura (m): '))
massa = float(input('Insira seu peso (kg): '))

imc = round(massa / (alt**2), 2)

print(f'IMC: {imc}')