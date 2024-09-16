import time

# Função Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Função Selection Sort
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        menor_indice = i
        for j in range(i + 1, n):
            if lista[menor_indice] > lista[j]:
                menor_indice = j
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

# Abrindo e lendo o conteúdo do arquivo "texto.txt" e armazenando as palavras em uma lista
with open("loremipsum.txt", "r") as arquivo:
    texto = list()
    for linha in arquivo:
        palavras = linha.split()  # Divide a linha em palavras
        texto.extend(palavras)  # Adiciona as palavras à lista

# Copiando a lista de palavras para usar em diferentes métodos de ordenação
lista_bubble = texto.copy()
lista_selection = texto.copy()
lista_sort = texto.copy()

# Medindo o tempo de execução do Bubble Sort
inicio_bubble = time.time()
bubble_sort(lista_bubble)
fim_bubble = time.time()
tempo_bubble = fim_bubble - inicio_bubble

# Medindo o tempo de execução do Selection Sort
inicio_selection = time.time()
selection_sort(lista_selection)
fim_selection = time.time()
tempo_selection = fim_selection - inicio_selection

# Medindo o tempo de execução do método nativo sort()
inicio_sort = time.time()
lista_sort.sort()
fim_sort = time.time()
tempo_sort = fim_sort - inicio_sort

# Exibindo os tempos de execução e resultados
print("Resultado da ordenação por Bubble Sort:")
print(lista_bubble)
print(f"Tempo de execução (Bubble Sort): {tempo_bubble:.6f} segundos\n")

print("Resultado da ordenação por Selection Sort:")
print(lista_selection)
print(f"Tempo de execução (Selection Sort): {tempo_selection:.6f} segundos\n")

print("Resultado da ordenação pelo método nativo sort():")
print(lista_sort)
print(f"Tempo de execução (Método nativo sort): {tempo_sort:.6f} segundos\n")

# Escolher o método de melhor performance (no caso o método nativo sort()) e salvar no arquivo "ordenado.txt"
with open("ordenado.txt", "w") as arquivo_ordenado:
    for palavra in lista_sort:
        arquivo_ordenado.write(palavra + "\n")

print("As palavras ordenadas foram salvas no arquivo 'ordenado.txt'.")
