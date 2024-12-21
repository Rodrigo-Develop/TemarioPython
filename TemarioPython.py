# Variables y sus tipos
cadena = "cadena de texto"
numero = 23
verdadFalso = True
numeroPuntoFlotante = 4.3  # Corregido para ser un número flotante
print(f"{type(cadena)}\n{type(numero)}\n{type(verdadFalso)}\n{type(numeroPuntoFlotante)}")

#Not operador
print(f"\n{not True}\n{not verdadFalso}")

#Equality operador ==
print(f"\n{numero==cadena}")

#Inequality operador !=
print(f"\n{numero!=cadena}")

#Formatted Strings
print(f"Hola {numero}")

#< > >= <=
print(f"\n{8>2}")
print(8<2)
print(8>=2)
print(8<=2)

#if else elif
a = 3
print()
if a<4:
    print(f"{a} es menor a 4")
elif a>7:
    print(f"{a} es menor a 7")
else:
    print(a)