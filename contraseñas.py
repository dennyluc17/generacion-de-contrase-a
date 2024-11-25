import random
import string
import secrets

def generar_contraseña():
    # Solicitar longitud de la contraseña
    longitud = int(input("Ingrese la longitud deseada de la contraseña (mínimo 8): "))
    while longitud < 8:
        print("La longitud mínima es 8. Intente nuevamente.")
        longitud = int(input("Ingrese la longitud deseada de la contraseña (mínimo 8): "))
    
    