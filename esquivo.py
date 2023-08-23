import pygame
import random

# Inicializar pygame
pygame.init()

# Definir los colores
blanco = (255, 255, 255)
negro = (0, 0, 0)

# Definir el tamaño de la pantalla
ancho = 800
alto = 600
pantalla = pygame.display.set_mode((ancho, alto))

# Definir la posición y tamaño del jugador
jugador_ancho = 50
jugador_alto = 50
jugador_x = 375
jugador_y = 500

# Definir la velocidad del jugador
jugador_velocidad = 1

# Definir la posición y tamaño del obstáculo
obstaculo_ancho = 50
obstaculo_alto = 50
obstaculo_x = random.randint(0, ancho - obstaculo_ancho)
obstaculo_y = 0

# Definir la velocidad del obstáculo
obstaculo_velocidad = 1

# Definir la puntuación
puntuacion = 0
fuente = pygame.font.Font(None, 36)

# Bucle principal del juego
juego_terminado = False
while not juego_terminado:
    # Manejar eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_terminado = True

    # Mover al jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador_x > 0:
        jugador_x -= jugador_velocidad
    if teclas[pygame.K_RIGHT] and jugador_x < ancho - jugador_ancho:
        jugador_x += jugador_velocidad

    # Mover el obstáculo
    obstaculo_y += obstaculo_velocidad

    # Si el obstáculo se sale de la pantalla, reiniciar su posición y aumentar la puntuación
    if obstaculo_y > alto:
        obstaculo_x = random.randint(0, ancho - obstaculo_ancho)
        obstaculo_y = 0
        puntuacion += 1

    # Si el jugador choca con el obstáculo, terminar el juego
    if jugador_x + jugador_ancho > obstaculo_x and jugador_x < obstaculo_x + obstaculo_ancho and jugador_y < obstaculo_y + obstaculo_alto and jugador_y + jugador_alto > obstaculo_y:
        juego_terminado = True

    # Dibujar la pantalla
    pantalla.fill(blanco)
    pygame.draw.rect(pantalla, negro, [jugador_x, jugador_y, jugador_ancho, jugador_alto])
    pygame.draw.rect(pantalla, negro, [obstaculo_x, obstaculo_y, obstaculo_ancho, obstaculo_alto])
    texto = fuente.render("Puntuacion: " + str(puntuacion), True, negro)
    pantalla.blit(texto, [10, 10])
    pygame.display.update()

