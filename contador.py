frase = input("Digite uma frase: ")
palavras = frase.split()
print(len(palavras))
print(palavras)

def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)