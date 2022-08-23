from ast import Pass
from time import sleep
tempo = 0.8;
'''
Crie uma função que, ao receber um número inteiro, 
retorna se um número  é par ou ímpar (utilizando **kwargs).
'''
print("Questão (1)");
def inteiroOuNao(inteiro=11) :
    if (inteiro % 2) == 0:
        return print(f'{inteiro} é par!!');
    else : 
        return print(f'{inteiro} é impar!!');

print(inteiroOuNao(10));
print("-----------------------------------");

sleep(tempo);
'''
Crie de forma recursiva uma função que 
printe do número recebido até o zero.
'''
print("Questão (2)");
def recursidade(numero) :
    print(numero)
    if numero == 0:
      return 0;
    else : 
      return recursidade(numero - 1)
recursidade(5)
print("-----------------------------------");
sleep(tempo);
'''
Crie uma função de somatório que some todos os números que 
a mesma receber (usando *args ).
'''
print("Questão (3)");
def soma(*somatorio):
    print(sum(somatorio));

soma(10,65,90);
print("-----------------------------------");
sleep(tempo);
'''
Crie um programa com uma função que necessite de três argumentos,
e que forneça a soma desses três argumentos.
'''
print("Questão (4)");
def argumentosSomados(arg1,arg2,arg3):
    return arg1 + arg2 + arg3;

print(argumentosSomados(1,2,3));
print("-----------------------------------");
sleep(tempo);  
'''
Faça um programa com uma função que necessite de um argumento. 
A função deve retornar o valor de caractere ‘P’, se seu argumento for positivo,
e ‘N’, se seu argumento for zero ou negativo.
'''
print("Questão (5)");
def positivoOuNegativo(argumento):
    if argumento > 0 :
        return "P";
    elif argumento <= 0 :
        return "N";

print(positivoOuNegativo(1));
print("-----------------------------------");
sleep(tempo);
'''
Crie uma função que permita contar o número de 
vezes que aparece uma letra em uma string.
'''
print("Questão (6)");
def numeroDeStrings(string, contletras) :
    contador = 0;
    for letra in string :
      if letra == contletras :
          contador += 1
    return contador;
print(numeroDeStrings("oi, Me chamo Marcos", "o"))
print("-----------------------------------");
sleep(tempo);
'''
Escreva uma função que, dado o valor da conta de um restaurante,
calcule e exiba a gorjeta do garçom, considerando 10% do valor da conta.
'''
print("Questão (7)");

def gorgetaDoGarção(conta):
    gorgeta = conta * 0.10;
    return f'A gorgeta do garçom é R${gorgeta:.2f}.';

print(gorgetaDoGarção(500.00));
print("-----------------------------------");
sleep(tempo);
'''
Crie uma função que receba duas palavras e retorne True caso a primeira palavra seja
um prefixo da segunda. Exemplo: ’uf’ é prefixo de ’ufabc’.
’ufabc’ não é prefixo de ’uf’.
'''
print("Questão (8)");
def prefixo(string, prefixo) :
    tamanho = len(prefixo);
    if prefixo == string[:tamanho] :
          return True
    else :
        return False
    
print(prefixo('ufabc', "uf"))
print("-----------------------------------");
sleep(tempo);