'''
1) O caixa no bar do Sr. João está cheio de diversas moedas. O Sr. João 
precisa fechar o caixa, mas está com dificuldade de fazer os cálculos 
do tanto de dinheiro que ele possui em moedas. Enquanto estava 
organizando ele conseguiu separar as moedas e contar a quantidade 
delas conforme a tabela:

Moeda       Quantidade
5 centavos  35
10 centavos 50
25 centavos 30
50 centavos 15
1 real      19

Crie uma aplicação que calcule a quantidade de reais (R$) 
que o Sr. João possui moedas no caixa. A aplicação deve imprimir o 
valor total em reais (R$), pode-se utilizar ponto flutuante para poder 
representar o valor com duas casas decimais no momento que for 
imprimir na tela o valor.
'''
from ast import If, Num
import string


real1 = 100;
moedasCentavos5 = (5 * 35) / real1;
moedasCentavos10 = (10 * 50) / real1;
moedasCentavos25 = (25 * 30) / real1;
moedasCentavos50 = (50 * 15) / real1;
real2 = (100 * 19) / real1;

resultado = moedasCentavos5 + moedasCentavos10 + moedasCentavos25 + moedasCentavos50 + real2;
print(f'O total em moedas foi em torno de R$ {resultado:.2f}.');

'''
2) Um freelancer está com dificuldade para calcular qual o valor 
cobrar por um projeto que está estimado em 80 horas. 
Após pensar e revisitar o preço de alguns projetos que cobrou 
no passado ele montou a seguinte fórmula: valor inicial + quantidade de horas estimadas * valor
da hora + 15% do valor calculado. Sua tarefa  
é criar um programa que faça essa conta para o freelancer. Considere que o valor
inicial sempre será 1000,00 R$ e o valor da hora cobrada é de 20,45 R$. A aplicação
deve imprimir o valor calculado pelo projeto considerando duas casas decimais na
formatação do valor. Dica: Olhar a ordem como as operações da fórmula devem ser realizadas.
'''
horaEstimada = int(input("insira a quantidade de horas estimada: ")); '''insira 80'''
valorInicial = 1000;
horaCobrada = 20.45;
valorInicialDesconto = 1000 * 0.15; 

contaFinal = valorInicial + (horaEstimada * horaCobrada) + valorInicialDesconto ; 
print(f' O valor a vir ser cobrado pelo projeto, é de R$ {contaFinal:.2f}');

'''
3) A recepção de uma nave espacial recebe as pessoas com uma mensagem 
de boas vindas de acordo com o nome que elas forneceram ao fazer o cadastro na recepção. 
Crie uma aplicação que imprima a mensagem de boas vindas de acordo com 
a lista de nomes na lista: nomes = [‘Elysson’, ‘Giulia’, ‘Willian’, ‘Gileno’] com a 
seguinte mensagem “Bem vindo, NOME_PESSOA!! Seja bem vindo a nave Imperial dos Siths.”. 
Crie um programa que faça a interpolação da string de boas vindas, substituindo o NOME_PESSOA pelo
nome lido da lista e imprimindo a frase de boas vindas com o nome substituindo.
'''
nomes = ['Elysson', 'Giulia', 'Willian', 'Gileno'];

for nome in nomes:
    print('Bem vindo, {NOME_PESSOA}!!,'.format(NOME_PESSOA = nome),
    'Seja bem vindo a nave Imperial dos Siths.');
 
''' 
4) Criei um programa que possua as variáveis A, B e C.
Imprima o resultado de A + B caso ele seja menor do que C, caso contrário imprima que o valor é 
menor. Teste a aplicação com alguns valores nas variáveis sugeridas.
'''
letraA = 2;
letraB = 5;
letraC = 10;

somaAB = letraA + letraB;

if somaAB < letraC:
    print(somaAB);
    
else: print(somaAB, " é maior que ", letraC);

'''
5) Criei um programa que calcule o peso ideal de uma pessoa. 
Para isso utilize as fórmulas da tabela:
Para Homens: (72.7 * altura) – 58
Para Mulheres: (62.1 * altura) – 44.7 

Sua aplicação deve identificar se a pessoa é Homem ou Mulher
e então fazer o cálculo apropriado. Deve ser impresso se a pessoa é homem ou mulher, 
juntamente com o peso ideal calculado.
'''
gênero = input("insira 'homem' ou 'mulher'(letras minusculas)");
altura = float(input("insira sua altura em Metros"));

if gênero == "homem":
    pesoIdeal = (72.7 * altura) - 58;
    print(f'Seu peso ideal é {pesoIdeal:.2f}');
elif gênero == "mulher":
    pesoIdeal = (62.1 * altura) - 44.7;
    print(f'Seu peso ideal é {pesoIdeal:.2f}');

'''
6) Um nutricionista está precisando de uma ajuda para calcular o IMC de seus pacientes. 
Para calcular o IMC ele passou a seguinte fórmula: IMC = peso / ( altura )². 
Crie um programa que faça o cálculo do IMC de uma pessoa (ele deve ser impresso na tela)
 e classifique o IMC dessa pessoa de acordo com a tabela (também deverá ser impresso):


Valor do IMC     Classificação
Abaixo de 18,5   Pessoa abaixo do peso
Entre 18,5 e 25  Pessoa com peso normal
Entre 25 e 30    Pessoa acima do peso
Acima de 30      Pessoa obesa
'''
peso = float(input("insira seu peso"));
altura = float(input("insira sua altura em Metros"));

IMC = peso / (altura)**2;
if IMC < 18.5:
    print(f'Seu imc é {IMC:.2f}, isso significa que você está abaixo do peso');
elif IMC >= 18.5 and IMC <= 25 :
    print(f'Seu imc é {IMC:.2f}, isso significa que você está com o peso normal');
elif IMC > 25 and IMC <= 30 :
    print(f'Seu imc é {IMC:.2f}, isso significa que você está acima do peso');
elif IMC > 30 :
    print(f'Seu imc é {IMC:.2f}, isso significa que você está obeso');

'''
7) Uma loja de móveis está com dificuldades de calcular algumas condições de 
pagamento de seus móveis. Eles possuem algumas regras e o seu trabalho é implementar
uma aplicação que faça os cálculos de acordo com as regras:
Regras
À vista em dinheiro, recebe 15% de desconto
À vista no cartão de crédito, recebe 10% de desconto
Em duas vezes, preço normal de etiqueta sem juros
Mais de duas vezes, preço normal de etiqueta mais juros de 10%

O programa deve ter uma variável com o valor de etiqueta do produto, 
uma variável com forma de pagamento e uma com o preço final após a 
aplicação de uma das regras.
'''
valorEtiqueta = 1000.00;

metodoDePagamento = input("insira o metodo de pagamento");

valorAvista = valorEtiqueta * 0.15;
ValorComDesconto1 = valorEtiqueta - valorAvista;

valorCartão = valorEtiqueta * 0.10;
ValorComDesconto2 = valorEtiqueta - valorCartão;

duasVezes = valorEtiqueta / 2;

if metodoDePagamento == "Valor a vista":
    print(f'O preço final é de R${ValorComDesconto1:.2f}');

elif metodoDePagamento == "Valor no cartão":
    print(f'O preço final é de R${ValorComDesconto2:.2f}');

elif metodoDePagamento == "Pagar em duas vezes":
    print(f'O preço final parcelado é R${duasVezes:.2f}');

elif metodoDePagamento == "Pagar mais de duas vezes":
 numeroDeParcelas = float(input("insira o número de parcelas"));
 maisDeDuasVezes = valorEtiqueta / numeroDeParcelas;
 contaIntermediaria = maisDeDuasVezes * 0.10;
 ValorComDesconto3 = maisDeDuasVezes - contaIntermediaria;
 print(f'O preço final parcelado é R${ValorComDesconto3:.2f}');

 '''
 Alguns alunos de uma universidade criaram uma “criptografia” para se comunicarem entre eles 
 durante o tempo que estão longe da universidade. Essa criptografia é baseada em códigos que, 
 quando convertidos, formam as letras de uma palavra. Esses números são informados em uma lista de 
 caracteres e são separados pela string ‘-1’ conforme o exemplo abaixo:


Nessa sequência teríamos o número 79 representando um caractere e o número 73 representando
outro caractere da mensagem. Para saber a letra será necessário percorrer essa lista e ir 
concatenando os números antes de identificar um separador (‘-1’) para então identificar qual letra o 
código numérico representa. Por exemplo: A primeira iteração da lista será lido o primeiro número 
‘7’, adicionamos ele em uma variável (sugestão de nome: codigo_letra),
Na segunda interação será lido o número ‘9’ que será concatenado na mesma variável variável 
(usando o += com strings) Na terceira iteração iremos identificar que é o caractere que separa
as letras da mensagem, converter o código numérico para uma letra usando o 
código: palavra += chr(int(codigo_letra)) (esse código utiliza funções, iremos estudar mais 
a respeito ao longo do curso). Após converter a variável deve ser limpa para que possamos continuar
 a ler as demais letras. Será repetido todos os passos acima para a segunda letra

Para o exemplo acima, a primeira letra é o caractere “O” e a segunda letra será o 
caractere “I” formando a palavra “OI”. Sua tarefa será criar uma aplicação que percorra a sequência:
mensagem_criptografada = 
['8', '5', '-1', '7', '6', '-1', '8', '4', '-1', '7', '3', '-1', '7', '7', '-1', '6', '5', '-1']
Faça a concatenação dos códigos numéricos conforme o exemplo acima e ao final imprima qual 
a palavra formada. Após fazer a aplicação, pesquise por códigos ASCII 😉
'''
mensagemCriptografada = ['85', '-1', '76', '-1', '84',
 '-1', '73', '-1', '77', '-1', '65', '-1']
codigoLetra = ''
for mensagem in mensagemCriptografada: 
    if mensagem =="-1":
        print(chr(int(codigoLetra)))
        codigoLetra = ''
    else :
         codigoLetra = codigoLetra + mensagem
print(codigoLetra)


         




























