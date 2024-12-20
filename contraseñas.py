
import string
import secrets

def generar_contrseña():
    #solicitar longitud de la contraseña
    longitud = int(input("ingrese la longitud de la contraseña(mínimo 8) :"))
    while longitud < 8:
        print("la longitud minima es 8. intente nuevamente.")
        longitud - int(input("ingrese la longitud deseada de la contraseña (mínimo 8)"))

    # Preguntar si se desean caracteres especiales
    usar_caracteres_especiales = input("¿Desea incluir caracteres especiales? (sí/no): ").lower
    
    # Definir los conjuntos de caracteres posibles
    caracteres_base = string.ascii_letters + string.digits  # Letras y números
    caracteres_especiales = string.punctuation  # Caracteres especiales

    if usar_caracteres_especiales == 'sí':
        caracteres_posibles = caracteres_base + caracteres_especiales
    else:
        caracteres_posibles = caracteres_base

     # Generar la contraseña aleatoria utilizando 'secrets.choice' para mayor seguridad
    contraseña = ''.join(secrets.choice(caracteres_posibles) for _ in range(longitud))
    
    return contraseña

# Llamada a la función para generar y mostrar la contraseña
contraseña_generada = generar_contrseña()
print("Contraseña generada:", contraseña_generada)
