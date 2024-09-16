import random

# Criando um array de 15 posições com números inteiros e valores aleatórios
array_numeros = [random.randint(0, 100) for _ in range(15)]

# Ordenar o array em ordem crescente
array_numeros.sort()
print("Array em ordem crescente:", array_numeros)

# Ordenar o array em ordem decrescente
array_numeros.sort(reverse=True)
print("Array em ordem decrescente:", array_numeros)

# Criando um array de strings (nome, dataNascimento, cpf, rg)
array_strings = [
    "nome", "dataNascimento", "cpf", "rg", 
    "email", "telefone", "endereco", "cidade", 
    "estado", "cep", "pais", "profissao", 
    "empresa", "salario", "nacionalidade"
]

# Ordenar o array de strings em ordem crescente
array_strings.sort()
print("Array de strings em ordem crescente:", array_strings)

# Ordenar o array de strings em ordem decrescente
array_strings.sort(reverse=True)
print("Array de strings em ordem decrescente:", array_strings)
