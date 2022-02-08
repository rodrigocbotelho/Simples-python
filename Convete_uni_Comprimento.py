resposta = str(input('DESEJA CONVERTE UNIDADES DE COMPRIMETROS S/N?').strip().lower())
while resposta == 's':
    print('''OPÇÕES:
    [ 1 ] METROS PRA CENTÍMETROS
    [ 2 ] CENTÍMETROS PARA METROS''')
    escolha = int(input('ESCOLHA: '.strip()))
    if escolha == 1:
        print('-=-=-METROS PRA CENTÍMETROS-=-=-')
        n1 = float(input('DIGITE O VALOR EM METROS: ').strip())
        print('VALORES:\nMETROS: {:.0f}m\nCENTÍMETROS: {:.0f}cm'.format(n1 ,n1 * 100 ).strip())
        resposta = str(input('Desejar repetir S/N?'))
    elif escolha == 2:
        print('-=-=-CENTÍMETROS PARA METROS-=-=-')
        n1 = float(input('DIGITE O VALOR EM CENTÍMETROS: ').strip())
        print('VALORES:\nCENTÍMETROS: {:.0f}cm\nMETROS: {:.0f}m'.format(n1 , n1 / 100 ).strip())
        resposta = str(input('Desejar repetir S/N?'))
    else:
        print('OPÇÃO INVALIDA! TENTE NOVAMENTE!')
        resposta = str(input('DESEJA CONVERTE UNIDADES DE COMPRIMETROS S/N?').strip().lower())
print('FIM!')
