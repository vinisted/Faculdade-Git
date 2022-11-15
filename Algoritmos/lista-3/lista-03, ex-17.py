turmas = int(input('digite a quantidade de turmas: '))
aturmas = []
turma = 1

for i in range(turmas):
    print('turma ', turma)
    alunos = int(input('Alunos da turma: '))
    while alunos > 40:
        print('turma ', turma, '(uma turma só pode ter 40 alunos)')
        alunos = int(input('Alunos da turma : '))
    turma += 1
    aturmas.append(alunos)

media = sum(aturmas) / len(aturmas)
print('A media e igual a: ', media)