

texto1="Hola"
texto2="Mundo[]"
textofinal= texto1+""+texto2
print(textofinal)

print("El saludo es: %s %s " % (texto1,texto2))

cadena="Saludar dos: {1} {0} ".format(texto1,texto2)
print(cadena)

cadena="Saludar dos: {x} {y} ".format(texto1,texto2)
print(cadena)