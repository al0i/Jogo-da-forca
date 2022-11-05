import random
import desenhos

#Abrindo arquivo e sorteando palavra;
arquivo = open("palavras.txt", 'r', encoding="utf-8")
palavra_sorteada = (random.choice(arquivo.readlines()[1:]).strip('\n').upper())

#Ocultando palavra;
palavra = list(palavra_sorteada)
palavra_oculta = []
for letras in palavra:
    palavra_oculta.append("_")    

#Verifica se letra chutada está na palavra. Parâmetros: Input, palavra sorteada em forma de lista e palavra ocultada em forma de lista, registro de erros, registro de letras digitadas;
def verificar(x,palavra,palavra_oculta,erros,letras_digitadas):
    if x in letras_digitadas:
        letras_digitadas.append(x)
        return '\033[43m''Você já digitou essa letra!''\033[m'
    elif x in palavra:
        for i in range(len(palavra)):
            if palavra[i] == x:
                palavra_oculta[i] = x
        letras_digitadas.append(x)
        return '\033[32m''Acerto!''\033[m'
    else:
        erros.append(x)
        letras_digitadas.append(x)
        return '\033[31m''Erro!''\033[m'

#Registro de erros e letras digitadas;
erros = []
letras_digitadas = []

print('\033[33m''BEM VINDO AO JOGO DA FORCA!''\033[m')
while True:
    #A cada rodada mostra os erros e as letras já digitadas;
    print("\nErros: ", len(erros))
    print("Letras digitadas: ",letras_digitadas)

    #Desenho da forca (pode ser modificado no arquivo 'desenho.py');
    print(desenhos.desenho(len(erros)))

    #Palavra para mostrar sem aparecer os elementos de lista;
    palavra_oculta_mostrar = ' '.join(palavra_oculta)
    print('\n',palavra_oculta_mostrar,'\n')

    #Pede e verifica a letra digitada;
    letra_chute = input("Digite uma letra: ").upper()
    print(verificar(letra_chute,palavra,palavra_oculta,erros,letras_digitadas))

    #Se completou toda a palavra;
    if palavra_oculta == palavra:
        print(desenhos.desenhoFeliz())
        print('\033[42m'"VOCÊ GANHOU!"'\033[m')
        break
    
    #Se não conseguiu completar a palavra;
    if len(erros) >= 6:
        print(desenhos.desenho(len(erros)))
        print('\033[41m'"VOCÊ PERDEU :("'\033[m')
        print("A palavra era:",f'\033[1;7m{"".join(palavra_sorteada)}\033[m')
        break
        
#Resultado final com total de erros e as letras digitadas;
print(f'''Resultados:
Erros: {len(erros)}
Jogadas: {len(letras_digitadas)}

''')