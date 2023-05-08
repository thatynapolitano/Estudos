"""
Projete um programa que use um loop while e solicite continuamente que o usuário insira uma palavra, a menos que o usuário insira "chupacabra" como a palavra de saída secreta, caso em que a mensagem "Você saiu do loop com sucesso". Deve ser impresso na tela, e o loop deve terminar.

Não imprima nenhuma das palavras inseridas pelo usuário. Use o conceito de execução condicional e a declaração break.
"""

secret_word = "chupacabra"

palavra = input("Escreva uma palavra: ")

while palavra != secret_word:
    print("Tente novamente")
    palavra = input("Escreva uma palavra: ")
    if palavra == secret_word:
        break
print("Você saiu do loop com sucesso")