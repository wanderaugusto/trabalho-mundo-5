# Função bubbleSort para ordenar o array
def bubbleSort(array):
    # Iterar pelos elementos do array
    for i in range(len(array)):
        # Iterar sobre os elementos de dois a dois
        for j in range(0, len(array) - i - 1):
            # Verificar se o elemento j é maior que o elemento j+1
            if array[j] > array[j + 1]:
                # Troca dos elementos
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

# Declarar um array de números com 15 posições com valores aleatórios
import random
array_numeros = [random.randint(1, 100) for _ in range(15)]

# Exibir o array original
print("Array original:", array_numeros)

# Aplicar o método bubbleSort no array
bubbleSort(array_numeros)

# Exibir o array ordenado
print("Array ordenado:", array_numeros)
