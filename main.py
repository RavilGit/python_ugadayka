from random import randint
from os import system, name 
from time import sleep 

print('Welcome to Ugadayka\nEnter number from 1 to 100')

x = randint(1, 100)
counter = 0
games = list()

# define our clear function 
def clear(): 
  if name == 'nt': 
    # for cmd system('cls')
    _ = system('cls') 

def generate_new_num():
  return randint(1, 100)

def is_valid(num):
  if num.isdigit():
    if 0 < int(num) <= 100:
      return True
  return False

while True:
  temp = input()
  counter += 1
  if is_valid(temp):
    if int(temp) == x:
      print('Victory\nYou: {}\tWe: {}\nShot: {}'.format(temp, x, counter))
      games.append(counter)
      counter = 0
      print('-' * 70)
      print('Do You want to play again?\nPress Y - yes')
      game = input()
      if game == 'y':
        x = generate_new_num()
        sleep(1) 
        clear()
        print('New num generated, Guess it!')
      else:
        print('-' * 70)
        print('_' * 29 + ' Your stat ' + '_' * 29)
        for i in range(len(games)):
          print('Game number: {}\tShots: {}'.format(i + 1, games[i]))
        print('-' * 70)
        break
    elif int(temp) > x:
      print('less')
    elif int(temp) < x:
      print('more')
  else:
    print('{} is not valid number\nEnter number in range 1 - 100:'.format(temp))

# Улучшения проекта
# Добавить возможность указания правой границы для случайного выбора числа (от 1 до n).


# clear function code from https://www.geeksforgeeks.org/clear-screen-python/