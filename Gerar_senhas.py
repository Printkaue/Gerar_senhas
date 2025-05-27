import random

#Lista de caracteres possiveis
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "S", "T", "U", "V", "W", "X", "Y", "Z"]

caracteres = ["@", "#", "$", "%", "&", "/", "!"]

numeros = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

carac = letras + caracteres + numeros

#pede o numero de caracteres
N = int(input("Digite o numrros de digitos da sua senha: "))

#sistema de criação
def gerar_senha(N, lista):
    senha = ""
    for chart in range(N):
        caractere = random.choice(lista)
        senha += caractere
    return senha
             
resultado = gerar_senha(N, carac)
print(resultado)
