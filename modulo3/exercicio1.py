import random

def intersecao_listas():
  
    lista1 = random.sample(range(1, 21), 10)  # 10 números únicos
    lista2 = random.sample(range(1, 21), 10)

    print("Lista 1:", lista1)
    print("Lista 2:", lista2)

   
    intersecao = list(set(lista1) & set(lista2))


    intersecao.sort()

    print("Elementos em comum (sem repeticao):", intersecao)
    return intersecao

intersecao_listas()