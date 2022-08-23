'''
6) Um nutricionista está precisando de uma ajuda para calcular o IMC de seus pacientes.
Para calcular o IMC ele passou a seguinte fórmula: IMC = peso / ( altura )².
Crie um programa que faça o cálculo do IMC de uma pessoa (ele deve ser impresso na tela) e
classifique o IMC dessa pessoa de acordo com a tabela (também deverá ser impresso):

Valor do IMC	   Classificação
Abaixo de 18,5	   Pessoa abaixo do peso
Entre 18,5 e 25	   Pessoa com peso normal
Entre 25 e 30	   Pessoa acima do peso
Acima de 30	       Pessoa obesa
'''
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura em metros: "))

formulaIMC = peso / altura**2

if formulaIMC < 18.5 :
    print("Pessoa abaixo do peso")
elif formulaIMC >= 18.5 and formulaIMC <= 25 :
    print("Pessoa com peso normal")
elif formulaIMC > 25 and formulaIMC <= 30 :
    print("Pessoa acima do peso")
elif formulaIMC > 30 :
    print("Pessoa obesa")