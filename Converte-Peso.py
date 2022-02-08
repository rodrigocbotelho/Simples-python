resposta = str(input('Deseja converter seu peso para Lbs ou Kg S/N? ')).strip().upper()
while resposta == 'S':
    print('''Opções:
[ 1 ] Lbs para Kg
[ 2 ] Kg para lbs''')
    escolha = int(input('Resposta: ').strip())
    if escolha == 1: 
        peso = float(input('Digite seu peso: ').strip())
        print('Seu peso em:\nLbs: {}; \nKg: {:.2f};'.format(peso, peso /  2.205))
        resposta = str(input('Deseja repetir o processo S/N? ')).strip().upper()
    elif escolha == 2:
        peso = float(input('Digite seu peso: ').strip())
        print('Seu peso em:\nKg: {}; \nLbs: {:.2f};'.format(peso, peso *  2.205))
        resposta = str(input('Deseja repetir o processo S/N? ')).strip().upper()
    else:
        print('VALOR INCORRETO! TENTE NOVAMENTE!')
        resposta = str(input('Deseja converter seu peso para Lbs ou Kg S/N? ')).strip().upper()
print('EXIT')


