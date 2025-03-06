import random
import string

length = int(input("Ingresa el largo de la contraseña: "))

caracteres = string.ascii_letters + string.digits + string.punctuation
contraseña = ''.join(random.choices(caracteres, k=length))

print(contraseña)