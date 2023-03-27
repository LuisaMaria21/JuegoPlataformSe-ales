import pygame, sys
import speech_recognition as sr

#Inicialización de pygame
pygame.init() 

#Definición de colores
BLACK = (0,    0,    0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)

#Definición de la ventana
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Juego de Plataformas con Speech Recognition")

# Definición del jugador
player_width = 50
player_height = 50
player_x = (window_width / 2) - (player_width / 2)
player_y = window_height - player_height
player_speed = 5

# Definición de la plataforma
platform_width = 100
platform_height = 20
platform_x = (window_width / 2) - (platform_width / 2)
platform_y = window_height - (player_height * 2)
platform_color = WHITE

# Definición del reconocedor de voz
r = sr.Recognizer()

# Función para obtener el comando de voz del jugador
def get_voice_command():
    with sr.Microphone() as source:
        print("Habla ahora...")
        audio = r.listen(source)
        try:
            command = r.recognize_google(audio, language="es-ES")
            print("Comando detectado: " + command)
            return command.lower()
        except:
            print("No se ha detectado ningún comando.")
            return None


# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Detección del comando de voz del jugador
    command = get_voice_command()
    if command == "izquierda":
        player_x -= player_speed
    elif command == "derecha":
        player_x += player_speed

    # Lógica del juego
    if player_x < 0:
        player_x = 0
    elif player_x > window_width - player_width:
        player_x = window_width - player_width

    # Dibujado de los elementos del juego
    window.fill(BLACK)
    pygame.draw.rect(window, platform_color, (platform_x, platform_y, platform_width, platform_height))
    pygame.draw.rect(window, WHITE, (player_x, player_y, player_width, player_height))
    pygame.display.update()   

# Finalización del juego
pygame.quit()

