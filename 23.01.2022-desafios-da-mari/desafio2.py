meses_trabalhados = int(input("Quantas meses Tiago trabalhou? "))
disp = input('Tem disponibilidade entre dezembro e janeiro? ')

if (meses_trabalhados >= 12) and (disp == "Sim"):
    print('Tiago pode sair de férias')
else:
    print('Tiago não pode sair de férias')