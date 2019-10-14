print("""
   _____                             _                            _       _            
  / ____|                           | |                          | |     | |           
 | (___   ___  _ __ ___   __ _    __| | ___   _ __  _ __ ___   __| |_   _| |_ ___  ___ 
  \___ \ / _ \| '_ ` _ \ / _` |  / _` |/ _ \ | '_ \| '__/ _ \ / _` | | | | __/ _ \/ __|
  ____) | (_) | | | | | | (_| | | (_| |  __/ | |_) | | | (_) | (_| | |_| | || (_) \__ \\
 |_____/ \___/|_| |_| |_|\__,_|  \__,_|\___| | .__/|_|  \___/ \__,_|\__,_|\__\___/|___/
                                             | |                                       
                                             |_|                                       
""")





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

        port = ".".join(port)
        
        expressao_ordenada.append(port)
        variavel_not = []

    return expressao_ordenada

def tabela_verdade(expressao_completa_ordenada):   

    tabela= []

    for porta_and in expressao_completa_ordenada:

        bits = []

        for bit in porta_and.split("."):

            if '~' in bit:
                bits.append('0')
            else:
                bits.append('1')
        tabela.append(bits)
        
    return tabela

def mostrar_expressao_incompleta(expressao_incompleta):
    expressao_incompleta = expressao_incompleta.split("+")
    return " + ".join(expressao_incompleta)


def mostrar_variaveis(variaveis):
    return ",".join(variaveis)

def mostrar_expressao_completa(expressao_completa):
    return " + ".join(expressao_completa)

def mostra_tabela(tabela,variaveis):
    print("Tabela verdade:")
    tabela.sort()
    tabela_verdade = []

    for variavel in variaveis:
        
        print("|{}".format(variavel),end="")


    #qubrar linha
    print("|S|")

    for tab in tabela:
        
        for ta in tab:
            print("|{}".format(ta),end="")
        print("|1|")

    return "-".join(tabela_verdade)

def main(args):

    expressao = "A+B.~C"
    expressao_split = receber_expressao(expressao)

    


    variaveis = contar_variaveis(expressao_split) 

    expressao_completa = comletar_expressao(expressao_split, variaveis)
    expressao_completa_ordenada = ordenar_expressao(expressao_completa)
    tabela = tabela_verdade(expressao_completa_ordenada)

    print("Expressão incompleta:",mostrar_expressao_incompleta(expressao))
    print("Variaveis:", mostrar_variaveis(variaveis))
    print("Expressão completa:", mostrar_expressao_completa(expressao_completa))
    print("Expressão completa e ordenada:", mostrar_expressao_completa(expressao_completa_ordenada))
    
    mostra_tabela(tabela,variaveis)



    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
