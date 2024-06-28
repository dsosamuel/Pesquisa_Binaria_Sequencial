from random import randint
from time import perf_counter

tempo_inicial = perf_counter()
def busca_sequencial(vetor, valor):
  for i in range(len(vetor)):
    if vetor[i] == valor:
      return i
  return -1

def main():
  tamanho_vetor = int(input("Digite o tamanho do vetor: "))
  vetor = [randint(0, tamanho_vetor * 10) for _ in range(tamanho_vetor)] # Gerar e preencher o vetor com números aleatórios
  valor_busca = int(input("Digite o valor a ser buscado: "))
  indice = busca_sequencial(vetor, valor_busca)
  if indice != -1:
    print(f"O valor {valor_busca} foi encontrado no índice {indice}.")
  else:
    print(f"O valor {valor_busca} não foi encontrado no vetor.")

main()

tempo_final = perf_counter()
print (f'{tempo_final - tempo_inicial}s')