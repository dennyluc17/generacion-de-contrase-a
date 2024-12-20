## GENERADOR DE CONTRASEÑA

 ## DESCRIPCION DEL GENERADOR DE CONTRASEÑA

Este Generador de Contraseñas es una herramienta en Python diseñada para ayudar a los usuarios a crear contraseñas seguras y aleatorias. La contraseña generada puede incluir letras mayúsculas y minúsculas, números y, si lo deseas, caracteres especiales como símbolos y signos de puntuación. Este enfoque asegura que las contraseñas sean robustas y difíciles de predecir, lo cual es esencial para proteger cuentas en línea y mantener la seguridad de datos personales.


## OBJETIVO DE MI GENERADOR DE CONTRASEÑA

El objetivo del programa de tu generador de contraseñas es proporcionar una herramienta sencilla, interactiva y segura para crear contraseñas aleatorias y robustas, que ayuden a proteger las cuentas y datos personales de los usuarios.

## FUNCIONES PRINCIPALES DEL CODIGO
1. **Solicitar longitud de la contraseña**: El usuario puede especificar la longitud deseada de la contraseña (con un mínimo de 8 caracteres).
   
2. **Incluir caracteres especiales**: El programa pregunta si el usuario desea incluir caracteres especiales como símbolos y signos de puntuación en la contraseña. Si elige sí, se agregan al conjunto de caracteres posibles.

3. **Generación aleatoria de la contraseña**: Usando la función `secrets.choice()`, se genera una contraseña aleatoria que cumple con los requisitos establecidos por el usuario.

4. **Seguridad**: Al utilizar `secrets` en lugar de `random`, el programa asegura una generación de contraseñas más segura, evitando la predictibilidad que puede ser un riesgo en la creación de contraseñas con métodos más simples.

## Instrucciones de uso
ASEGURATE DE TENER  Python 3.x INSTALADO EN TU PC
1. Clona el repositorio o descarga el archivo Python en tu máquina local.
      https://github.com/dennyluc17/generacion-de-contrase-a
3. Ejecuta el archivo pincipal.
      CONTRASEÑAS
4. ejecuta en tu entorno python
5. El programa te pedirá que ingreses:
   - La longitud deseada para la contraseña (mínimo 8 caracteres).
   - Si deseas incluir caracteres especiales.
6. El programa generará una contraseña aleatoria con los parámetros que especificaste y la imprimirá en la pantalla.

##  EJEMPLO DE EJECUCION 
 - ingrese la longitud de la contraseña(mínimo 8) :15
   
   ¿Desea incluir caracteres especiales? (sí/no): si

   Contraseña generada: lBZ3oFre3tW8klm

   PS C:\Users\DELL\Desktop\DENNY\lucas py> 

## DATOS DEL USUARIO
 - INTEGRANTE 1 : Denny Johan Lucas 
   
 - INSTITUCION : Universidad Internacional del Ecuador
   
 - CARRERA : Ingenieria en software modalida en linea
   
 -  MATERIA : Logica de programacion 
    
 -  FECHA : 20 de dicienbre del  2024

 ## TECNOLOGIA UTULIZADA 
  -  LENGUAJE : Python
    
  -  LIBRERIA : String y Secrets

## ADICIONAL
Este proyecto es parte de nuestros aprendizajes asi como nuestras actividades a lo largo de la materia de logica de programacion para aprender fundamentos de programacion. Si tienes sugerencias, o mejoras dale no dudes contribuir a travez de pull resquests.
