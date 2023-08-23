import random

# Base de datos de usuarios
usuarios = {'usuario1': 'contrasena1', 'usuario2': 'contrasena2'}

# Función para inicio de sesión
def login():
    while True:
        usuario = input("Ingresa tu nombre de usuario: ")
        contrasena = input("Ingresa tu contraseña: ")
        if usuario in usuarios and usuarios[usuario] == contrasena:
            print("Inicio de sesión exitoso.\n")
            break
        else:
            print("Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo.\n")

# Función para jugar el juego
def jugar():
    print("¡Bienvenido al juego de esquivar obstáculos!\n")
    puntos = 0
    while True:
        obstaculo = random.randint(0, 1)
        respuesta = input("¿Esquivarás el obstáculo? (s/n): ")
        if respuesta == 's' and obstaculo == 0:
            puntos += 1
            print("¡Muy bien! Has esquivado el obstáculo. Puntos: ", puntos)
        elif respuesta == 's' and obstaculo == 1:
            print("¡Oh no! Has chocado contra el obstáculo. Fin del juego. Puntos: ", puntos)
            break
        elif respuesta == 'n' and obstaculo == 0:
            print("¡Oh no! Has chocado contra el obstáculo. Fin del juego. Puntos: ", puntos)
            break
        elif respuesta == 'n' and obstaculo == 1:
            puntos += 1
            print("¡Muy bien! Has evitado el obstáculo. Puntos: ", puntos)

# Flujo principal del programa
login()
jugar()
