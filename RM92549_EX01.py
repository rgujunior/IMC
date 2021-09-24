peso = float(input("Por favor informe seu peso: "))
altura = float(input("Por favor informe sua altura: "))
imc = float

imc = peso / (altura * altura)

if imc < 16.00:
    print("seu IMC é de: {:.2f} Categoria: Baixo peso Grau III".format(imc))
elif imc <= 16.99:
    print("seu IMC é de: {:.2f} Categoria: Baixo peso Grau II".format(imc))
elif imc <= 18.49:
    print("seu IMC é de: {:.2f} Categoria: Baixo peso Grau I".format(imc))
elif imc <= 24.99:
    print("seu IMC é de: {:.2f} Categoria: Peso ideal".format(imc))
elif imc <= 29.99:
    print("seu IMC é de: {:.2f} Categoria: Sobrepeso".format(imc))
elif imc <= 34.99:
    print("seu IMC é de: {:.2f} Categoria: Obesidade Grau I".format(imc))
elif imc <= 39.99:
    print("seu IMC é de: {:.2f} Categoria: Obesidade Grau II".format(imc))
else:
    print("seu IMC é de: {:.2f} Categoria: Obesidade Grau III".format(imc))
