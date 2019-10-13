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

def main(args):
    expressao_split = receber_expressao("A.~B+A.~C")

    variaveis = contar_variaveis(expressao_split) 

    print(verif_expressao_completa_incompleta(expressao_split, variaveis))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
