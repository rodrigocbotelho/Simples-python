resposta = str(input('DIGITE "D": ').strip().lower())
while resposta == 'd':
    nome = str(input('INFORME SEU NOME: ').strip().upper()).split()
    idade = int(input('INFORME SUA IDADE: ').strip())
    if (idade >=18):
        print('PRIMEIRO NOME: {}'.format(nome[0].upper()))
        print('SOBRENOME NOME: {}'.format(nome[-1].upper()))
        print('ACESSO A CARTEIRA: APROVADO')
    else:
        print('PRIMEIRO NOME: {}'.format(nome[0]))
        print('SOBRENOME NOME: {}'.format(nome[-1]))
        print('ACESSO A CARTEIRA: NEGADO')
        print('\033[1;31m* IDADE NECESSÁRIA "21" *\033[m')
    resposta = str(input('DIGITE "D" PARA REPETIR: ').strip().lower())
