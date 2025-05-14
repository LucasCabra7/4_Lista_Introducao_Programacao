def maquinas(): # Função para as informações de cada máquina.
    qtd_maquinas = int(input())

    soma_gastos = 0
    maior_gasto = 0

    for i in range(qtd_maquinas): # Percorrer todos os elementos da quantidade de maquinas para gerar os inputs

        tempo = int(input())
        potencia = float(input())
        percentual_ineficiencia = int(input())
        preco_unid_energia = float(input())

        energia = energia_inicial(tempo, potencia) # Chamando a função Energia inicial
        acrescimo = acrescimo_energia(energia, percentual_ineficiencia) # Chamando a função Acrescimo
        consumo = consumo_total(acrescimo, energia) # Chamando a função Consumo Total
        gastos = gasto_total(consumo, preco_unid_energia) # Chamando a função Gasto Total

        soma_gastos += gastos # Incrementando a soma dos gastos

        if(gastos > maior_gasto): # Verificando qual é o maior gasto para qual maquina
            maior_gasto = gastos

        outputs(consumo) # Chamando a função dos outputs

    output_gastos(soma_gastos, maior_gasto) # Chamando a função dos outputs para a soma e maior gasto

def energia_inicial(tempo, potencia): # Função que retorna o resultado da Energia Inicial
    return (potencia * tempo)

def acrescimo_energia(energia, percentual_ineficiencia): # Função que retorna o resultado do Acrescimo
    return (energia * (percentual_ineficiencia / 100))

def consumo_total(acrescimo, energia): # Função que retorna o resultado do Consumo Total
    return (acrescimo + energia)

def gasto_total(consumo, preco_unid_energia): # Função que retorna o resultado do Gasto Total
    return (preco_unid_energia * consumo)

def outputs(consumo): # Função que verifica cada condição para o consumo e imprime o resultado:
    
    if(consumo == 0):
        print('Parece que essa coisa nem ao menos funciona')
    elif((consumo > 0) and (consumo <= 100)):
        print(f'Temos aqui uma máquina formidável, seu consumo de energia é {consumo:.2f}')
    elif((consumo > 100) and (consumo <= 300)):
        print(f'Você tem certeza que essa coisa não vai explodir? seu consumo de energia é {consumo:.2f}')
    elif(consumo > 300):
        print('Você se importaria de jogar seus explosivos em qualquer outro lugar?')

def output_gastos(soma_gastos, maior_gasto): # Função que imprime a soma dos gastos e o maior gasto:

    print(f'Os gastos totais com as maquinas foi de {soma_gastos:.2f}')
    print(f'A máquina mais cara gasta um total de {maior_gasto:.2f} para os cofres de Piltover')

maquinas() # Chamando a função principal maquinas.