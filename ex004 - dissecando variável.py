# Método de Strings
# https://docs.python.org/pt-br/3/library/stdtypes.html

v = input('Digite um valor: ')
print ('O tipo primitivo desse valor é ', type(v))
print ('Só tem espaços? ', v.isspace())
print ('É um número? ', v.isnumeric())
print ('É alfabético? ', v.isalpha())
print ('É alfanumérico? ', v.isalnum())
print ('Está em maiúscula? ', v.istitle())
print ('Está em minúscula? ', v.islower())
print ('Está capitalizada? ', v.isupper())