def descriptografar(): # Função para Descriptografar:
    resultado = ''
    for letra in formula_criptografada: # Percorre todos os elementos da palavra da formula criptografada.
        if(deslocamento_cifra > 0): # Verifica se o Deslocamento da cifra for maior que zero.
            indice = (letras.index(letra) - deslocamento_cifra) # Encontrar a posição da letra dentro da lista de letras e subtrair do deslocamento e assim obtendo o indíce do deslocamento.
            resultado += letras[indice % 26] # Garante que se o indíce for negativo, ele voltara para o inicio da lista de letras.
        else:
            resultado += letra # Se o deslocamento for zero, irá armazenar a própria letra sem deslocamento.

    def calcular_dano(): # Função para Calculcar o Dano:
        if(resultado == 'ALTO'):
            fator = 2
        elif(resultado == 'MEDIO'):
            fator = 1.5
        elif(resultado == 'BAIXO'):
            fator = 1
        dano = round(precisao * (poder_explosao / resistencia) * fator)

        ataques.append([nome, dano]) # Adiciona o nome e o dano como uma sublista da lista de ataques.

        def ordem_ataques(): # Função de Ordenar os Ataques:
            print(f'Decifrando: {resultado}')
            print(f'{nome}: {dano} de dano calculado.')

            if(dano >= 100): 
                print(f'{nome} será destruído!')
            else:
                print(f'{nome} resistirá ao ataque.')
            print('')
        
        ordem_ataques() # Chamando a função Ordenar os Ataques.
    calcular_dano() # Chamando a funçãp Calcular o Dano.

letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

n_ataques = int(input())

if(n_ataques == 0): # Condicional para verificar se o nª de ataques for igual a zero.
    print('Piltover em paz... por enquanto.')
else: # Caso contrário:
    ataques = [] # Lista para armazenar as sublistas com [`nome`, `dano`].

    for i in range(n_ataques): # Incrementar a quantidade de inputs através da quantidade de ataques.
        info_ataque = input().split(', ')
        nome = info_ataque[0]
        precisao = int(info_ataque[1])
        resistencia = int(info_ataque[2])
        poder_explosao = int(info_ataque[3])
        formula_criptografada = info_ataque[4].upper()
        deslocamento_cifra = int(info_ataque[5])
        descriptografar() # Chamando a função de Descriptografar toda vez que percorrer um ataque, e assim sucessivamente.

    for i in range(len(ataques)): # Percorre cada posição da lista de ataques.
        for j in range(i + 1, len(ataques)): # Percorre todos os elementos que vem seguinte do i, ou seja, i + 1 (j).
            if(ataques[i][1] < ataques[j][1]): # Verifica se primeiro dano é menor que o segundo dano (e assim sucessivamente, se houver mais).
                ataques[i], ataques[j] = ataques[j], ataques[i] # Troca as posições em ordem Decrescente

    print('Prioridade de ataques:')
    for ataque in ataques: # Percorre todos os elementos da lista de ataques em ordem Descrecente.
        print(f'{ataque[0]} - {ataque[1]} de dano')