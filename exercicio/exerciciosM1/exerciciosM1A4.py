
'''
Atividade compreensiva do módulo
Nesta semana, a última do Módulo 1, vamos criar uma CLI (Command Line Interface) aplicando os conceitos aprendidos nas últimas 4 aulas. 
Instruções: 
Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:
Entregar o menor número de notas;
É possível sacar o valor solicitado com as notas disponíveis;
Saldo do cliente infinito;
Quantidade infinita de notas (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
Notas disponíveis: R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00;
Exemplos:
Valor do saque: R$ 30,00 – Resultado Esperado: entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
Valor do saque: R$ 80,00 – Resultado Esperado: entregar 1 nota de R$50,00, 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
'''

def notas(valor):
    cedulas = []

    cem = valor // 100
    resto = valor % 100
    cedulas.append(cem)
    
    cinquenta = resto // 50
    resto = resto % 50
    cedulas.append(cinquenta)

    vinte = resto // 20
    resto = resto % 20
    cedulas.append(vinte)
     
    dez = resto // 10
    cedulas.append(dez)
    
    return cedulas
    



saque = int(input("indique o valor a ser sacado: "))
cedulas = notas(saque)

print("entregar {} notas de 100, {} notas de 50, {} notas de 20 e {} notas de 10" .format(cedulas[0],cedulas[1],cedulas[2],cedulas[3]))
    
    

