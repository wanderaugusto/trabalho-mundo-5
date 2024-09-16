# Abrindo o arquivo com o método open e lendo todo o conteúdo
arquivo = open("loremipsum.txt", "r")

# Imprimir o conteúdo completo do arquivo
conteudo_completo = arquivo.read()
print("Conteúdo completo do arquivo:")
print(conteudo_completo)

# Fechar o arquivo após a leitura
arquivo.close()

# Reabrindo o arquivo para outras operações
arquivo = open("loremipsum.txt", "r")

# Imprimir apenas a primeira linha do arquivo
primeira_linha = arquivo.readline()
print("\nPrimeira linha do arquivo:")
print(primeira_linha)

# Fechar o arquivo
arquivo.close()

# Reabrindo o arquivo novamente para outra operação
arquivo = open("loremipsum.txt", "r")

# Imprimir apenas os 3 primeiros caracteres do arquivo
primeiros_caracteres = arquivo.read(3)
print("\nPrimeiros 3 caracteres do arquivo:")
print(primeiros_caracteres)

# Fechar o arquivo
arquivo.close()

# Utilizando a instrução "with" para abrir o arquivo e armazenar o conteúdo
with open("loremipsum.txt", "r") as arquivo:
    conteudo_with = arquivo.read()
    print("\nConteúdo do arquivo utilizando 'with':")
    print(conteudo_with)
