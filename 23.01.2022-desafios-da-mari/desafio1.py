nota =  int(input('Qual a nota do aluno do PdA? '))
participacao = (input('Você é participativo? '))

if nota >= 7: 
    print('Parabéns! Você está aprovado!!')

elif (nota == 6) and (participacao == "Sim"):  
    print('Você está de recuperação!')
    
else:
    print('Você está reprovado!')
