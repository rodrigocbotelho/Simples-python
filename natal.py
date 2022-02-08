from random import choice
from pygame import mixer
from time import sleep 
mixer.init()
mixer.music.load('natal.mp3')
mixer.music.play()
print('HO HO HO! PAPAI NOEL CHEGOU!')
resposta = str(input('DESEJAR GANHAR PRESENTES DE NATAL S/N?')).strip().lower()
while resposta == 's':
    nome = str(input('Qual é seu nome? '))
    presentes = ('Cachecol','Camisa Natalina', 'Chapéu do Papai Noel', )
    lista = choice(presentes)
    print('DEIXA EU VER O QUE TEM NA SACOLA DE PRESENTES!...')
    sleep(2)
    print('PARABÉNS! {} VOCÊ GANHOR UM {} DE NATAL!'.format(nome.upper(), lista))
    resposta = str(input('DESEJA REPETIR S/N?').strip().lower())
print('FELIZ NATAL!')