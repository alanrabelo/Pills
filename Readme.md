* Objetivo 

Segmentar imagens de pílulas ilícitas: separar pílulas do fundo.

#### Segmentação por contornos (Pílulas Circulares)

+ Implementar detecção de círculos pela transformada de Hough
+ Verificar se cada imagem possui uma pílula de forma circular
  + Identificar o centro e o raio desse círculo
+ Identificar os parâmetros necessários para ajustar 
  corretamente o método de segmentação proposto. 
+ Apresentar os resultados em termos de Precisão e Acurácia (Pesq.).


#### Segmentação por regiões

##### Crescimento de regiões
+ Propor um método para obtenção de sementes
  ++ Deve funcionar para imagens com uma ou mais pílulas
  ++ Baseado no nível de cinza
  ++ Semente na borda

+ Propor um critério de similaridade para agregação de pixels.
+ Identificar os parâmetros necessários para ajustar corretamente o método de segmentação proposto. 


##### K-Médias

+ Identificar os parâmetros necessários para ajustar corretamente o método de segmentação proposto. 


#### Cálculo de características dos objetos segmentados

+ Característica (Atributo)
  + Área média das pílulas
  + Razão Área/Perímetro
  + Circularidade (pesquisar)
  + Desvio padrão do nível de cinza

+ Apresentar Comparativo dessas Características com cada método de segmentação
  + Uma boa forma de apresentar é na forma de gráficos.


#### Entrega

+ Equipes: 3 alunos (máx)
+ Data : 06 de agosto de 2018
+ Itens:
  + Relatório: deve conter discussões sobre as escolhas de valores dos parâmetros e sua relação com a qualidade dos resultados obtidos, incluir exemplos. 
  + Imagens processadas. 

