from random import randint

# User input
min_num = int(input('Enter a min number: '))
max_num = int(input('Enter a max number: '))

if (max_num < min_num):
    print('Invalid input - shutting down ...')
else:
    rnd_num = randint(min_num, max_num)
    print(rnd_num)
