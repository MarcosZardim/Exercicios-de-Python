d1 = input('digite algo: ')
print('O tipo primitivo desse valor é? {}' .format(type(d1)))
print('Só tem espaços? {}'.format(d1.isspace()))
print('É um numero? {}'.format(d1.isnumeric()))
print('É alfabético? {}'.format(d1.isalpha()))
print('É alfanumérico? {}'.format(d1.isalnum()))
print('Está em maiúsculas? {}'.format(d1.isupper()))
print('Está em minúsculas? {}'.format(d1.islower()))
print('Está capitalizada? {}'.format(d1.istitle()))
