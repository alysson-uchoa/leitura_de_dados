Este repositório compara a performance ao processar grandes volumes de dados (1 milhão de linhas) utilizando a biblioteca pandas em Python.

Ao calcular o total de vendas por vendedor, inicialmente utilizei um loop for com iterrows() e filtros individuais mostrou-se ineficiente, levando 140 segundos para encerrar.

Para otimizar, utilizei o método groupby() para calcular os totais e transformar os resultados em dicionários. Com essa abordagem, houve redução do tempo de execução para 0,87 segundos.
