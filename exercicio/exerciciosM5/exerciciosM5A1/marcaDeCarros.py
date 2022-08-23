'''
Para a atividade desta semana, você deverá criar um interator que irá interar os dados da API (Application Interface) da tabela FIPE 
e retornar os carros de uma determinada marca de veículos (essa deverá ser passada para a classe que fará o papel de interator no momento da 
instanciação, neste caso use o ID de uma marca).

Para trazer esses dados, será necessário interagir com a API da FIPE disponível nesse endereço: https://deividfortuna.github.io/fipe/. Dicas:

Para listar as marcas use a URL:  https://parallelum.com.br/fipe/api/v1/carros/marcas dessa forma serão listadas todas as marcas que a API possui.
Escolha uma para ser usada na próxima etapa, grave o ID dela para ser usado no seu código.
Nesta etapa use a marca selecionada para poder retornar os veículos que essa marca possui usando 
a URL: https://parallelum.com.br/fipe/api/v1/carros/marcas/{ID_MARCASELECIONADA}/modelos
Ao chamar esse endpoint, será retornada uma resposta que possui um nó, no formato JSON, com os modelos dos veículos que ela possui.
Seu interator deverá inteirar em cada um desses modelos e trazer informações do nome e ID do veículo da marca selecionada.
Essa atividade possui um grau de dificuldade um pouco maior e será necessário pesquisar como usar a biblioteca de JSON
(que já vem com a linguagem) e as requests (necessário instalar). Caso encontre muitas dificuldades, marque um horário 
para que um tutor possa te ajudar : )
'''

import requests
import json
site = requests.get("https://parallelum.com.br/fipe/api/v1/carros/marcas")
