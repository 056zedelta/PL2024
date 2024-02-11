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
    modalidades_unicas = sorted(set(modalidades))
    for i, modalidade in enumerate(modalidades_unicas, start=1):
        print(f"{i}. {modalidade}")

modalidades_ordenadas = despOrd(meu_dicionario)

def aptidaoPercent(dicionario):
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

percentagem_aptos, percentagem_inaptos = aptidaoPercent(meu_dicionario)

print(f"Percentagem de atletas aptos: {percentagem_aptos:.2f}%")
print(f"Percentagem de atletas inaptos: {percentagem_inaptos:.2f}%")


def escalaoAtletas(dicionario):
    distribuicao = {}
    for valor in dicionario.values():
        idade = int(valor['idade'])
        escalao = idade // 5 * 5 
        chave_escalao = f"[{escalao}-{escalao + 4}]"
        if chave_escalao in distribuicao:
            distribuicao[chave_escalao] += 1
        else:
            distribuicao[chave_escalao] = 1
    return distribuicao

distribuicao_escalao_etario = escalaoAtletas(meu_dicionario)

chaves_ordenadas = sorted(distribuicao_escalao_etario.keys(), key=lambda x: int(x[1:3]))

for escalao in chaves_ordenadas:
    quantidade = distribuicao_escalao_etario[escalao]
    print(f"{escalao}: {quantidade} atletas")