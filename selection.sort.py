# Criando um array com 15 números inteiros sem ordenação
import random
array = [random.randint(1, 100) for _ in range(15)]

# Exibir o array original
print("Array original:", array)

# Primeira iteração no array
for i in range(len(array)):
    # Variável para armazenar o índice do menor valor
    menor_indice = i
    
    # Segunda iteração para comparar o elemento atual com os próximos
    for j in range(i + 1, len(array)):
        # Se o elemento no índice "menor_indice" for maior que o elemento no índice "j"
        if array[menor_indice] > array[j]:
            # Atualiza o menor_indice para o índice "j"
            menor_indice = j
    
    # Troca os valores entre array[i] e array[menor_indice]
    array[i], array[menor_indice] = array[menor_indice], array[i]

# Exibir o array ordenado
print("Array ordenado:", array)
