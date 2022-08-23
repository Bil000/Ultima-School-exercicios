'''
5)	Criei um programa que calcule o peso ideal de uma pessoa. Para isso utilize as fórmulas da tabela:
Para Homens: (72.7 * altura) – 58
Para Mulheres: (62.1 * altura) – 44.7 

Sua aplicação deve identificar se a pessoa é Homem ou Mulher e então fazer o cálculo apropriado. 
Deve ser impresso se a pessoa é homem ou mulher,
juntamente com o peso ideal calculado.
'''

genero = input("Digite seu genero: ")
altura = float(input("Digite sua altura em metros: "))

if genero == "Homem" or genero == "homem":
    print(f'Sendo você um {genero}, seu peso ideal é {(72.7 * altura) - 58}')
elif genero == "Mulher" or genero == "mulher" :
    print(f'Sendo você um {genero}, seu peso ideal é {(62.1 * altura) - 44.7}')