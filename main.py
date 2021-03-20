from random import randint
print('Welcome to Ugadayka\nEnter number from 1 to 100')
x = randint(1, 100)

def is_valid(num):
  if num.isdigit():
    if 0 < int(num) <= 100:
      return True
  return False

while True:
  temp = input()
  if is_valid(temp):
    if int(temp) == x:
      print('Victory\nYou: {}\tWe: {}'.format(temp, x))
      break
    elif int(temp) > x:
      print('less')
    elif int(temp) < x:
      print('more')


# Улучшения проекта
# Добавьте подсчет попыток, сделанных пользователем. Когда число отгадано, программа должна показать количество попыток;
# Добавьте возможность генерации нового числа (повторная игра), после того, как пользователь угадал число;
# Добавить возможность указания правой границы для случайного выбора числа (от 1 до n).