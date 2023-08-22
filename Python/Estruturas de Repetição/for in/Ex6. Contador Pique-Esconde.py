#Sua tarefa é muito simples aqui: escreva um programa que use um loop for para "contar de forma incorreta" para cinco. Depois de contar até cinco, o programa deve imprimir na tela a mensagem final "Pronto ou não, aqui vou eu!"

import time 
for i in range(0,5):
   i += 1 
   print(i, "Mississippi")
   time.sleep(1)
print("Pronto ou não, aqui vou eu!")