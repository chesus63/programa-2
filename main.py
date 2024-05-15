02 from microbit import *                                                            # Importa todas las funciones y clases del módulo microbit.
03 import random                                                                     # Importa el módulo random para generar números aleatorios.
04 numero = 0                                                                        # Inicializa la variable 'numero' con el valor 0.
05 display.show(Image.YES, delay=1000, clear=True)                                   # Muestra una imagen de "YES" en la pantalla durante 1 segundo y luego limpia la pantalla.
06 while True:                                                                       # Inicia un bucle infinito.
07     numero = random.randint(0, 9)                                                 # Genera un número aleatorio entre 0 y 9 y lo asigna a la variable 'numero'.
08     if button_a.get_presses():                                                    # Verifica si el botón A ha sido presionado.
09         display.show(numero, delay=500, clear=True)                               # Muestra el número aleatorio en la pantalla durante 0.5 segundos y luego limpia la pantalla.
10     else:                                                                         # Si el botón A no ha sido presionado:
11         display.show(Image.NO)                                                    # Muestra una imagen de "NO" en la pantalla.
