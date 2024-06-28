from random import randint
from time import perf_counter

tempo_inicial = perf_counter()
def busca_binaria_recursao(vetor, valor, esquerda, direita):
  if esquerda > direita:
    return -1

  meio = (esquerda + direita) // 2
  elemento_meio = vetor[meio]

  if elemento_meio == valor:
    return meio
  elif elemento_meio < valor:
    return busca_binaria_recursao(vetor, valor, meio + 1, direita)
  else:
    return busca_binaria_recursao(vetor, valor, esquerda, meio - 1)

def busca_binaria(vetor, valor):
  if len(vetor) == 0:
    return -1
  return busca_binaria_recursao(vetor, valor, 0, len(vetor) - 1)

def main():
  tamanho_vetor = int(input("Digite o tamanho do vetor: "))
  vetor = [randint(0, tamanho_vetor * 10) for _ in range(tamanho_vetor)] #números aleatórios
  vetor.sort()   # Ordenar o vetor
  valor_busca = int(input("Digite o valor a ser buscado: "))
  indice = busca_binaria(vetor, valor_busca)   
  if indice != -1:
    print(f"O valor {valor_busca} foi encontrado no índice {indice}.")
  else:
    print(f"O valor {valor_busca} não foi encontrado no vetor.")

main()

tempo_final = perf_counter()
print (f'{tempo_final - tempo_inicial}s')