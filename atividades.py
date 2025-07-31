def adicionar(dicionario, aluno, nota):
    nota = float(nota)
    if aluno in dicionario:
        dicionario[aluno].append(nota)
    else:
        dicionario[aluno] = [nota]
    print(f"Nota {nota} adicionada para o aluno {aluno}")


def remover(dicionario, aluno):
    if aluno in dicionario:
        del dicionario[aluno]
        print(f"Aluno {aluno} removido com sucesso")
    else:
        print("Aluno não encontrado")

