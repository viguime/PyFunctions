alunos = [['EVA', 'Informática',2015], ['EDU', 'Direito',2018], ['TEO','Letras',2018], ['DIDI', 'Direito',2016], ['KAKA', 'Letras',2015],['VAVA', 'Informática',2018], ['LEO', 'Informática',2010],['AVA', 'Direito',2018],['LELE', 'Letras',2017], ['LEA', 'Informática',2015]]

def contaAlunosCurso(alunos):

    contai=0
    contal=0 
    contad=0
    i=0
    while i < len(alunos):
        contai = alunos[i].count('Informática') + contai
        contad = alunos[i].count('Direito') + contad
        contal = alunos[i].count('Letras') + contal
        i += 1

    return [['Informática', contai], ['Direito', contad], ['Letras', contal]]

print(contaAlunosCurso(alunos))