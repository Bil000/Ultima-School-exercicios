'''
7) Uma loja de móveis está com dificuldades de calcular algumas condições de pagamento de seus móveis. 
Eles possuem algumas regras e o seu trabalho é implementar uma aplicação que faça os cálculos de acordo com as regras:
Regras

À vista em dinheiro, recebe 15% de desconto
À vista no cartão de crédito, recebe 10% de desconto
Em duas vezes, preço normal de etiqueta sem juros
Mais de duas vezes, preço normal de etiqueta mais juros de 10%

O programa deve ter uma variável com o valor de etiqueta do produto,
uma variável com forma de pagamento e uma com o preço final após a aplicação de uma das regras.
'''

metodoDePagamento = input("Como deseja pagar: ")
valorEtiqueta = float(input("insira o valor da etiqueta em R$: "))

emDinheiro = valorEtiqueta * 0.15
descontoEmdinheiro = valorEtiqueta - emDinheiro

cartao = valorEtiqueta * 0.10
descontoNoCartao = valorEtiqueta - cartao

maisdeDuasVezes = valorEtiqueta * 0.1
final = valorEtiqueta + maisdeDuasVezes

if metodoDePagamento == "dinheiro" :
    print(descontoEmdinheiro)
elif metodoDePagamento == "cartão" or "cartao" :
    print(descontoNoCartao)
elif metodoDePagamento == "duas" :
    print(valorEtiqueta)
elif metodoDePagamento == "tres" :
    print(final)
    

