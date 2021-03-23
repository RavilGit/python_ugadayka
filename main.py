from random import randint
from os import system, name 
from time import sleep 

x = 0
counter = 0
games = list()
r_end = 100
print('Welcome to Ugadayka')

# define our clear function 
def clear(): 
  if name == 'nt': 
    # for cmd system('cls')
    _ = system('clear') 

def generate_new_num(end):
  return randint(1, end)

def is_valid(num, end):
  if num.isdigit():
    if 0 < int(num) <= end:
      return True
  return False

want_add = input('Do You want to enter end of range? y - yes | n - no\n')
if want_add == 'y':
  r_end = int(input('Enter end of range: '))
print('Enter num from 1 to {}'.format(r_end))
x = generate_new_num(r_end)
while True:
  temp = input()
  counter += 1
  if is_valid(temp, r_end):
    if int(temp) == x:
      print('Victory\nYou: {}\tWe: {}\nShot: {}'.format(temp, x, counter))
      games.append(counter)
      counter = 0
      print('-' * 70)
      print('Do You want to play again?\nPress Y - yes')
      game = input()
      if game == 'y':
      	r_end = int(input('Enter end of range: '))
      	x = generate_new_num(r_end)
      	sleep(1)
      	clear()
      	print('New num generated, Guess it!\nEnter num from 1 to {}'.format(r_end))
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

# clear function code from https://www.geeksforgeeks.org/clear-screen-python/