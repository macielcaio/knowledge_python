def get_notas(a1, a2, a3):
    notas = {"nota1": a1, "nota2": a2, "nota3": a3}
    return notas

def get_dados(mail, phone):
    dados = {"email": mail, "telefone": phone}
    return dados

def aluno(nome="Guest"):
    estudante = {"nome": nome, "notas": get_notas(10, 8, 9)}
    return estudante

# Cria o aluno e adiciona os dados de contato
aluno_jose = aluno("José")
aluno_jose.update(get_dados("teste@test.com", 123456))

# Mostra o dicionário final
print(aluno_jose)
