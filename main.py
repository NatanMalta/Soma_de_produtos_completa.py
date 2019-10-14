def receber_expressao(expressao):
    expressao = expressao.split("+")
    return expressao

def contar_variaveis(expressao_split):

    variaveis = []

    for porta_and in expressao_split:

        porta_and = porta_and.replace("~","").replace(".", "")

        for variavel in porta_and:
            if not( variavel in variaveis ):
                variaveis.append(variavel)
    
    return variaveis


def verif_expressao_completa_incompleta(expressao_split, variaveis):
    numero_variaveis = len(variaveis)
    contar_variaveis = 0
    contar_variaveis_expressao = numero_variaveis * len(expressao_split)

    for porta_and in expressao_split:
        for variavel in variaveis:
            if variavel in porta_and:
                contar_variaveis += 1
    if contar_variaveis_expressao == contar_variaveis:
        return True
    else:
        return False

def comletar_expressao(expressao_split, variaveis):
    variavel_completar = []
    porta_antiga = []
    porta_nova = []
    expressao_completa = []

    for porta_and in expressao_split:
        porta_antiga = []
        porta_antiga.append(porta_and)   

        #Descobrir variaveis que estão faltando
        for variavel in variaveis:
            if not( variavel in porta_and ):
                variavel_completar.append(variavel)

        #Percorrer variaveis que estão faltando
        for variavel in variavel_completar:
            for porta in porta_antiga:
                porta_nova.append("{}.{}".format(porta,variavel))
                porta_nova.append("{}.~{}".format(porta,variavel))
            porta_antiga = porta_nova
            porta_nova = []
        variavel_completar = []
        expressao_completa.extend(porta_antiga)
    return expressao_completa

def ordenar_expressao(expressao_completa):
    expressao_ordenada = []
    variavel_not = []
    for porta_and in expressao_completa:
        port = porta_and.replace("~","")
        porta_and = porta_and.split(".")
        port = port.split(".")
        port.sort()
        for variavel in porta_and:
            if "~" in variavel:
                variavel_not.append(variavel.replace("~",""))
        for not_variavel in variavel_not:
            port[port.index(not_variavel)] = "~"+not_variavel 
        expressao_ordenada.append(port)
        #print(port, variavel_not)


        variavel_not = []
    return expressao_ordenada

def tabela_verdade(expressao_completa_ordenada):
    tabela= []
    for porta_and in expressao_completa_ordenada:
        bits = []
        for bit in porta_and:
            if '~' in bit:
                bits.append(0)
            else:
                bits.append(1)
        tabela.append(bits)
        
    return tabela

def main(args):
    expressao = "~A.D+B.~C"
    expressao_split = receber_expressao(expressao)

    variaveis = contar_variaveis(expressao_split) 

    expressao_completa = comletar_expressao(expressao_split, variaveis)
    expressao_completa_ordenada = ordenar_expressao(expressao_completa)
    tabela = tabela_verdade(expressao_completa_ordenada)
    print("Expressão incompleta:",expressao)
    print("Variaveis:", variaveis)
    print("Expressão completa", expressao_completa)
    print("Expressão completa e ordenada", expressao_completa_ordenada)
    print("Tabela verdade", tabela)



    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
