## IMPORTAR MODULOS ##
import secrets
import string
import pyperclip as clipboard

# Definir los tipos de caracteres con string
letras = string.ascii_letters
digitos = string.digits
caracteres_especiales = string.punctuation

# Definir la longitud de la contraseña
longitud_contraseña = int(input('Ingrese la longitud de la contraseña: '))
contraseña = ''

# Crear el alfabeto de los caracteres a usar
alfabeto = letras + digitos + caracteres_especiales

# Crear la contraseña segun la longitud
for i in range(longitud_contraseña):
    contraseña += secrets.choice(alfabeto)

# Decision de copiar o no copiar la contraseña
print(contraseña)
portapapeles = input("Quieres copiar la contraseña en tu portapapeles? (Y/N) ")
if portapapeles == "Y":
    clipboard.copy(contraseña)
    print("Se ha copiado", contraseña, "en el portapapeles")
    exit
else:
    print("El programa se cerrará...")
    exit
