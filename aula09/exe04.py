notas = [
    ("Ana", 9.5),
    ("João", 8.0),
    ("Maria", 10.0),
    ("Pedro", 7.5),
    ("Ana", 10.0),
    ("Carlos", 6.5)
]

maior_nota = max(nota for aluno, nota in notas)

alunos_maior = tuple(aluno for aluno, nota in notas if nota == maior_nota)

alunos_reprovados = {aluno for aluno, nota in notas if nota < 7}

print("A maior nota alcançada é:", maior_nota)
print("Alunos que tiraram a maior nota:", alunos_maior)
print("Alunos que tiveram nota menor que 7.0:", alunos_reprovados)


