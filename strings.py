# Modificando strings con funciones
# Mayusculas/minusculas => upper()- lower()- capitalize()- title()- swapcase()

from itertools import count


frase = "...   &&&   Este  & ejercicio $· de == repaso con ¿? Python viene muy bien"

ejeupper = frase.upper()
print(ejeupper)  # Devuelve ==>>  ESTE EJERCICIO DE REPASO CON PYTHON VIENE MUY BIEN
# Convierte cada caracter del string en MAYÚSCULAS

ejelower = ejeupper.lower()
print(ejelower) # Devuelve ==>> este ejercicio de repaso con python viene muy bien
# Convierte cada caracter del string en minúsculas

ejecapitalize = ejelower.capitalize()
print(ejelower) # Devuelve ==>> Este ejercicio de repaso con python viene muy bien
# Observa como la palabra Python ==> python, la deja como estaba
# Convierte el primer caracter del string en Mayúscula

ejetitle = frase.title()
print(ejetitle) # Devuelve ==>> Este Ejercicio De Repaso Con Python Viene Muy Bien
# Convierte el primer caracter de cada palabra del string en Mayúscula

ejeswapcase = frase.swapcase()
print(ejeswapcase) # Devuelve ==>> eSTE EJERCICIO DE REPASO CON pYTHON VIENE MUY BIEN
# Convierte los caracteres en mayuscula en minuscula y viceversa 
# en cada palabra del string
ejeswapcase2 = ejetitle.swapcase()
# Cambiamos esto => Este Ejercicio De Repaso Con Python Viene Muy Bien
# por esto =======> eSTE eJERCICIO dE rEPASO cON pYTHON vIENE mUY bIEN
print(ejeswapcase2)

# #####################################################################

# Reemplazo/ Remover con strip()- replace()

frase2 = "Este ejercicio de repaso con Python viene muy bien pero que muy bien con Python"

ejestrip = frase.strip('. &')
print(frase, len(frase)) # longitud con espacios en blanco 56
print(ejestrip, len(ejestrip)) # longitud despues de strip() 50
print()

ejerstrip = frase2.rstrip()
print(ejerstrip, len(ejerstrip)) # len de 53
ejelstrip = frase2.lstrip()
print(ejelstrip, len(ejelstrip)) # len de 53
# strip() y sus variantes rstrip() y lstrip() eliminan los espacios 
# en blanco de una cadena
# si le pasas por parametro strip('. &') elimina todos los
# caracteres que encuentre desde la izquierda hasta el primero que no pueda
# el resto los deja

ejereplace = frase2.replace('Python', 'Serpiente' ,1 ) # replace()
# tiene 3 parametros('oldstr', 'newstr' , Numero de ocurrencias a cambiar)
# por defecto cambia todas si no se le pasa el tercer parametro
print(ejereplace)
print()

ejesplit = frase.split(' ', 4)
print(ejesplit)
print()
# split() convierte a lista el string
indice = 0
for x in ejesplit:
    print('Indice: ',indice, x)
    indice +=1
frase3 = ejesplit[4]
print(frase3.strip())
