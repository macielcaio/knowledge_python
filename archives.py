###   ARCHIVES   ###

# Enviar "r" significa abrir no modo de leitura, que é o padrão.
# Enviar "w" significa modo de escrita, para reescrever o conteúdo de um arquivo.
# Enviar "a" significa modo de anexar, para adicionar novo conteúdo ao final do arquivo.

# Adicionar "b" a um modo o abre no binary mode, que é usado para arquivos que não são de texto (como arquivos de imagem e som).

# # write mode
# open("filename.txt", "w")

# # read mode
# open("filename.txt", "r")
# open("filename.txt")

# # binary write mode
# open("filename.txt", "wb")

# file = open("/usercode/files/books.txt")
# cont = file.read()
# print(cont)
# file.close()

# file = open("filename.txt", "r")
# i = 2
for i in range(21):
    print(i)
# file.close()