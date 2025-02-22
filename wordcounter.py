textoIngresado = input("dame textoo xuxetumareee: ")

print("esto fue lo que ingresaste: ", textoIngresado)

cantLetras = len(textoIngresado)

print("esta es la cantidad de letras incluyendo espacios: ", cantLetras)

cantLetrasSinEspacios = len(textoIngresado.replace(" ", ""))

print("esta es la cantidad de letras sin espacios: ", cantLetrasSinEspacios)

cantPalabras = len(textoIngresado.split())

print("esta es la cantidad de palabras: ", cantPalabras)
