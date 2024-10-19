print("És um aluno da turma D, fizeste 3 minitestes, uma apresentação e um exame final. A média vai ser feita de 0 a 100.")
notMiniteste1 = int(input("mini teste 1: "))
notMiniteste2 = int(input("mini teste 2: "))
notMiniteste3 = int(input("mini teste 3: "))
notApresentacao = int(input("nota da apresentação: "))
notExamefinal = int(input("nota do exame final: "))
media_minitestes = (notMiniteste1+notMiniteste2+notMiniteste3)/3
media_final = (media_minitestes*0.6) + (notApresentacao*0.1) + (notExamefinal*0.3)
print(media_final)