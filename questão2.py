total_recursos = int(input())
pop_piltover = int(input())
pop_zaun = int(input())
situacao_zaun = input()

def situacao(): # Função para analisar a situação de Zaun:
    if(situacao_zaun == 'desastre'):
        taxa_zaun = 0.9
    elif(situacao_zaun == 'crise'):
        taxa_zaun = 0.8
    elif(situacao_zaun == 'critica'):
        taxa_zaun = 0.7
    elif(situacao_zaun == 'normal'):
        taxa_zaun = 0.6
    elif(situacao_zaun == 'tranquilo'):
        taxa_zaun = 0.5
    else:
        pop_total = (pop_zaun + pop_piltover)
        taxa_zaun = (pop_zaun / pop_total)
    return (taxa_zaun)

def distribuir_recursos(): # Função para Distribuir os Recursos entre as cidades Zaun e Piltover
    recursos_zaun = total_recursos * situacao()
    recursos_piltover = total_recursos - recursos_zaun
    razao_entre_recursos = recursos_zaun / recursos_piltover
    def mensagem(): # Função de Imprimir o resultado
        
        print(f'Foi decidido que será {recursos_piltover:.1f} para Piltover e {recursos_zaun:.1f} para Zaun!')

        if(razao_entre_recursos >= 0.9):
            print('Zaun receberá uma bolada!!!')
        elif(razao_entre_recursos >= 0.8) and (razao_entre_recursos < 0.9):
            print('Quase que Piltover ficava sem nada, pobrezinhos...')
        elif(razao_entre_recursos >= 0.7) and (razao_entre_recursos < 0.8):
            print('O negócio vai ficar bom para Zaun hein.')
        elif(razao_entre_recursos >= 0.6) and (razao_entre_recursos < 0.7):
            print('Parece que Zaun ainda precisa de ajuda.')
        elif(razao_entre_recursos >= 0.5) and (razao_entre_recursos < 0.6):
            print('As coisas estão meio apertadas para Zaun.')
        elif(razao_entre_recursos < 0.5):
            print('A situação não está muito favorável para Zaun...')
    mensagem() # Chamando a função da mensagem.
distribuir_recursos() # Chamando a função de Distribuir os recursos.