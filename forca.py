import random
palavra = ['python', 'programaçao', 'desenvolvimento', 'computador', 'inteligencia', 'aplicativo', 'algoritmo', 'web', 'dados',
           'interface', 'sistema', 'linguagem', 'estrutura', 'codigo', 'variavel', 'funçao', 'condicional', 'loop', 'repositorio', 'framework']
palavra_aleatoria = random.choice(palavra)
letras_usuario = []
chances = 6
ganhou = False


while True:

    # criar a logica
    for letra in palavra_aleatoria:
        if letra.upper() in letras_usuario:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"Você tem {chances} chances")
    tentativa = input("Escolha uma letra para advinhar:")
    letras_usuario.append(tentativa.upper())
    if tentativa.upper() not in palavra_aleatoria.upper():
        chances = chances - 1
        ganhou = True
        for letra in palavra_aleatoria:
            if letra.upper() not in letras_usuario:
                ganhou = False

        if chances == 0 or ganhou == True:
            break


if ganhou:
    print(f"Parabéns, você ganhou, sua palavra era {palavra_aleatoria}")
else:
    print(f"Você perdeu!, A palavra era {palavra_aleatoria} ")
