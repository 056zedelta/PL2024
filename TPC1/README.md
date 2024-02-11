# TPC1: Processamento de informação de .CSV

# Aluno

**Nome:** Luís Caetano

**Número:** 100893

## Descrição

Neste primeiro trabalho de casa, pretende-se, através de um ficheiro CSV, em primeiro lugar lê-lo e processá-lo. Isto sem recurso ao módulo CSV do Python. Após isto ser concluído é pedido que seja possível realizar três operações estatísticas: A lista ordenada alfabeticamente das modalidades, a percentagem de atletas aptos e inaptos e uma distribuição de atletas por escalão etário.
Para realizar o primeiro passo recorri a adicionar cada linha do CSV a um dicinário do python. Assim a chave para cada entry será o id. Para este passo recorro à função **dicionaryCSV**.
A função **despOrd** cria uma lista de modalidades únicas a partir do dicionário fornecido. Ordena esta lista e imprime cada modalidade.
A função **aptidaoPercent** recebe um dicionário que contém informações sobre atletas. A partir deste, incrementa a variável definida para cada o aptos e inaptos e posteriormente calcula a sua percentagem.
A função **escalaoAtletas** calcula a distribuição de atletas por intervalo etário, onde cada escalão é definido por um intervalo de 5 anos. Depois retorna um dicionario onde as chaves são os intervalos e os values são os atletas neles contidos. Depois as chaves do dicionário são ordenadas em ordem crescente de idade e à medida que estas são iteradas, é imprimindo o intervalo de idade e o número de atletas correspondentes em cada escalão. 
