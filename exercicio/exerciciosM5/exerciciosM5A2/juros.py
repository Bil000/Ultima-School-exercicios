'''
Para a atividade dessa semana, vamos trabalhar com a seguinte situação:

Uma pessoa do seu time de desenvolvimento está escrevendo várias funções que calculam diferentes formas de gerar juros.
Veja abaixo o exemplo de uma das funções:


Ela pediu para você escrever um decorator chamado decorator_imprimir,
que será usado para a função chamada imprima os parâmetros: capital, taxa e tempo, além do resultado da função.

Ao executar a função juros_simples, teríamos o seguinte resultado:

Com isso, será criada uma função decoradora (decorator) chamada decorator_imprimir que, ao ser usada com qualquer função parecida com a juros_simples 
(isto é, uma função que receba 3 parâmetros – capital, taxa, tempo), seja retornado um valor numérico correspondente ao juros.
'''
def decoratorImprimir(func):
   def interno(capital, taxa, tempo) :
      print('CAPITAL: {} TAXA: {} TEMPO: {}'.format(capital, taxa, tempo))
      print("RESULTADO: {:.1f}".format(func(capital, taxa, tempo)))
   return interno

@decoratorImprimir
def jurosSimples(capital, taxa, tempo) :
   return capital * (taxa / 100) * tempo

jurosSimples(100,3,4)





    