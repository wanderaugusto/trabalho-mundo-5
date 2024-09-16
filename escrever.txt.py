# Abrindo (ou criando) o arquivo texto.txt no modo de escrita
arquivo = open("texto.txt", "w")

# Criando uma lista de frases
texto = list()

# Adicionando frases à lista usando o método append
texto.append("Esta é a primeira frase.\n")
texto.append("Aqui está a segunda frase.\n")
texto.append("Esta é a terceira frase do arquivo.\n")

# Escrevendo o conteúdo da lista no arquivo
for linha in texto:
    arquivo.write(linha)

# Fechando o arquivo após a escrita
arquivo.close()

# Informando que o arquivo foi criado e escrito com sucesso
print("O arquivo 'texto.txt' foi criado e o conteúdo foi escrito com sucesso.")
