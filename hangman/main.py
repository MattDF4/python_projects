#Exercíco que checa se a letra escolhida pelo usuário está presente na palavra escolhida
#aleatóriamente dentro das opções da lista.
from random import choice
import os
import hangman_words
import hangman_art



empthy = []
choosen_world = choice(hangman_words.word_list)
choosen_world = choosen_world.lower()
empthy += len(choosen_world) * '-'

life_stage = 6
print(hangman_art.logo)
while True:
    guess = str(input('Guess a letter: ')).strip()

    os.system('cls')

    if guess in empthy:
             print(f'Você ja selecionou a letra \033[34m{guess}\033[m.')

    if guess not in choosen_world:
         print(f'A letra escolhida, \033[34m{guess}\033[m, não está na palavra. Você perdeu 1 vida.')
         life_stage -= 1
         if life_stage == 0:
              print(hangman_art.stages[life_stage])
              print('Você \033[31mPERDEU\033[m o jogo.')
              
              break
         else:
              print(hangman_art.stages[life_stage])
    else:
         print(hangman_art.stages[life_stage])

    position = 0
    
    for l in choosen_world:
        if l == guess:
            empthy[position] = l
        else:
             print()
        position += 1
                   
    print(empthy)
    if '-' not in empthy:
            print(f'\033[32mParabéns! Você completou a palavra \033[34m{choosen_world}\033[m')
            break
