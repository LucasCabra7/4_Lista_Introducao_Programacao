personagens_da_serie = ["Jinx", "Vi", "Heimerdinger", "Ekko", "Caitlyn", "Jayce", "Viktor", "Silco", "Claggor", "Vander", "Mylo"]

qtd_personagens = int(input())

lista_personagens = []

def adicionar_personagem(lista_personagens, personagem): # Função para adicionar o personagem.
    adicionou = lista_personagens + [personagem]
    return adicionou 

def remover_personagem(lista_personagens, personagem): # Função para remover o personagem.
    n = len(lista_personagens) - 1
    nova_lista = [""] * n
    j = 0

    for i in lista_personagens: # Percorrer todos os elementos da lista de personagens
        if i != personagem: # Condicional para verificar se o elemento da lista é diferente do personagem (input)
            nova_lista[j] = i
            j += 1 # Adiciona o personagem na nova lista
    return nova_lista

def quantidade_inputs(lista_personagens, qtd_personagens): # Função para quantidade de inputs
    while (len(lista_personagens) != qtd_personagens): # Loop para verificar se o tamanho da lista é diferente da quantidade de personagens. 
        comando = input()
        personagem = input()

        if (comando == 'Adiciona'): # Condicional para verificar o comando de Adicionar ou Remover o personagem:
            lista_personagens = adicionar_personagem(lista_personagens, personagem)
            print(f'Personagem {personagem} adicionado')
        elif(comando == 'Remove'):
            lista_personagens = remover_personagem(lista_personagens, personagem)
            print(f'Personagem {personagem} removido')
    return lista_personagens

def verificar_resultado(lista_personagens, personagens_da_serie): # Função para verificar o Resultado.
    venceu_ou_perdeu = 'venceu'
    for nome in lista_personagens:
        if(nome not in personagens_da_serie):
            venceu_ou_perdeu = 'perdeu'
    return venceu_ou_perdeu

def resultado(lista_personagens, personagens_da_serie): # Função para imprimir o resultado.
    print('Lista final de personagens:')
    for elemento in lista_personagens:
        print(elemento)

    if(verificar_resultado(lista_personagens, personagens_da_serie) == 'venceu'):
        print('Parabéns!! Você conseguiu acertar todos os nomes.')
        print('UAUUU! Acho que estamos preparados para ver a segunda temporada.')
    else:
        print('Infelizmente você perdeu...')
        print('Eita... Vamos precisar assistir novamente.')     

lista_personagens = quantidade_inputs(lista_personagens, qtd_personagens)
resultado(lista_personagens, personagens_da_serie)