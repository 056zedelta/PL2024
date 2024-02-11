def dicionaryCSV(nome_arquivo):
    dicionario = {}
    with open(nome_arquivo, 'r') as arquivo_csv:
        linhas = arquivo_csv.readlines()[1:]
        for linha in linhas:
            valores = linha.strip().split(',')
            chave = valores[0]
            valor = {
                "_id": valores[0],
                "index": valores[1],
                "dataEMD": valores[2],
                "nome": {"primeiro": valores[3], "último": valores[4]},
                "idade": valores[5],
                "género": valores[6],
                "morada": valores[7],
                "modalidade": valores[8],
                "clube": valores[9],
                "email": valores[10],
                "federado": valores[11],
                "resultado": valores[12].strip()
            }
            dicionario[chave] = valor
    return dicionario

meu_dicionario = dicionaryCSV('emd.csv')


def despOrd(dicionario):
    modalidades = []
    for valor in dicionario.values():
        modalidades.append(valor['modalidade'])
    modalidades_ordenadas = sorted(modalidades)
    return modalidades_ordenadas

modalidades_ordenadas = despOrd(meu_dicionario)

print(modalidades_ordenadas)


def calcular_percentagens_aptidao(dicionario):
    total_atletas = len(dicionario)
    aptos = 0
    inaptos = 0

    for valor in dicionario.values():
        if valor['resultado'] == 'true':
            aptos += 1
        else:
            inaptos += 1

    percentagem_aptos = (aptos / total_atletas) * 100
    percentagem_inaptos = (inaptos / total_atletas) * 100

    return percentagem_aptos, percentagem_inaptos

percentagem_aptos, percentagem_inaptos = calcular_percentagens_aptidao(meu_dicionario)

print(f"Percentagem de atletas aptos: {percentagem_aptos:.2f}%")
print(f"Percentagem de atletas inaptos: {percentagem_inaptos:.2f}%")


def distribuicao_atletas_por_escalao(dicionario):
    distribuicao = {}
    for valor in dicionario.values():
        idade = int(valor['idade'])
        escalao = idade // 5 * 5  # Arredonda para baixo para o múltiplo de 5 mais próximo
        chave_escalao = f"[{escalao}-{escalao + 4}]"
        if chave_escalao in distribuicao:
            distribuicao[chave_escalao] += 1
        else:
            distribuicao[chave_escalao] = 1
    return distribuicao

distribuicao_escalao_etario = distribuicao_atletas_por_escalao(meu_dicionario)

for escalao, quantidade in distribuicao_escalao_etario.items():
    print(f"{escalao}: {quantidade} atletas")