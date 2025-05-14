oponente_jinx = input().split(' - ')
nome = oponente_jinx[0]
vida = int(oponente_jinx[1])
distancia = int(oponente_jinx[2])
velocidade = int(oponente_jinx[3])
defesa = int(oponente_jinx[4])

qtd_lanca_missil = 0

print(f'Andando pelas ruas de Zaun, jinx dá de cara com um {nome} e agora vão lutar.')

def verifica_arma(velocidade, vida, defesa, distancia, qtd_lanca_missil): # Função para verificar qual arma a Jinx deve usar.
    if((distancia >= 50) and (defesa == 0) and (qtd_lanca_missil == 0)):
        vida = lanca_missel(vida)
        qtd_lanca_missil += 1
    elif((distancia >= 30)):
        vida, defesa = fish_bones(vida, defesa)
    elif((distancia >= 15) and (defesa == 0)):
        vida = arma_pow_pow(vida)
    else:
        velocidade, vida = arma_zap(velocidade, vida, defesa)

    distancia -= velocidade
    return velocidade, vida, defesa, distancia, qtd_lanca_missil

def arma_zap(velocidade, vida, defesa): # Função para Arma Zap.
    dano = 5
    if(velocidade > 1):
        velocidade -= 1
    if(defesa == 0):
        vida -= dano
        print('Você foi zapeado hahaha.')
    else:
        print('Ele está com defesa e está muito perto!')
    return velocidade, vida

def arma_pow_pow(vida): # Função para Arma PowPow.
    dano = 15
    vida -= dano
    print('Jinx vai encher esse cara de buracos agora.')
    return vida

def fish_bones(vida, defesa): # Função para Arma Fish Bones.
    dano = 30
    if(defesa == 1):
        defesa = 0
        print('A defesa dele foi destruída com o poder da Fishbones!')
    else:
        vida -= dano
        print('Vamos derretê-lo com a Fishbones!')
    return vida, defesa

def lanca_missel(vida): # Função para Arma Lança Missel.
    dano = 100
    vida -= dano
    print('Ele vai ser transformado em cinzas pelo SUPER MÍSSIL!')
    return vida

while ((vida > 0) and (distancia > 0)): # Loop para decrementar a vida ou distância do inimigo da jinx.
    velocidade, vida, defesa, distancia, qtd_lanca_missil = verifica_arma(velocidade, vida, defesa, distancia, qtd_lanca_missil)
    if(distancia <= 0):
        print('Ah não, A Jinx foi PEGA!')
    elif(vida <= 0):
        print('Ninguem é capaz de derrotar a Jinx!!!')