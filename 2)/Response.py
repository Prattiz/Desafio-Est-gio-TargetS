# Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

def contador(text):
    # Converte a string para minúsculas e conta cada 'a' no texto
    counter = text.lower().count('a')
    
    if counter > 0:
        print(f"A letra 'a' aparece {counter}X em {text}.")
    else:
        print("A letra 'a' não aparece na string fornecida.")


input = input("Digite uma string: ")

contador(input)