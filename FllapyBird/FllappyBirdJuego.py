##librerias necesarias para juego pygame
import pygame
from pygame.locals import *
import sys
import random
clock = pygame.time.Clock()
##cargar sonido
pygame.init()
pygame.mixer.music.load('imagenes/flappyBird.mp3')
pygame.mixer.music.play()

FPS = 30

pygame.joystick.init()  # variable para cargar el joystick
try:
	j = pygame.joystick.Joystick(0) # igualamos una variable para cargar la palanca
	j.init() # ubicamos una instancia
	print ("Enabled joystick: {0}".format(j.get_name()))#imprimimos si lee el joytick
except pygame.error:
	print ("no joystick found.")#no lee el joystick

##fondo y medidad de la ventana
pantalla= pygame.display.set_mode((400, 700))
fondo = pygame.image.load("imagenes/fondo.png").convert()
myFont = pygame.font.SysFont("comicsansms", 30)
bird = pygame.Rect(65, 50, 50, 50)
birdSprites = [pygame.image.load("imagenes/1.png").convert_alpha(),
                pygame.image.load("imagenes/2.png").convert_alpha(),
                pygame.image.load("imagenes/muerto.png")]
arriba = pygame.image.load("imagenes/cilindroArriba.png").convert_alpha()
abajo = pygame.image.load("imagenes/cilindroAbajo.png").convert_alpha()

pygame.font.init()
font = pygame.font.SysFont("Arial", 50)

# variables para posiciones y eventos 
pared= 400##posicio de inicializacion
espacioCilindros = 130 ##espacio entre cilindros
aparicion = random.randint(-110, 110)##compensar espacios y movimientos para que aparezacan los cilindros
sprite = 0 ##variable para sprites
birdY = 350##variable para la posicion en y del bird
dead = False
saltar = 0
contador = 0 ##contador
velocidadSalto = 10 ##velocidad del pajaro
gravedad = 5 ##velocidad con la que va cayendo el ave
timer=0
while True:
     ##codigo para insertas los cilindros y visualizacion de mover pantalla

    clock.tick(50)##velocidad que se cambiara la pantalla
    pantalla.fill((255, 255, 255))##.fill me ayudara a llenar el espacio con las medidas
    pantalla.blit(fondo, (0, 0))##.blit me ayudara a cargar las imagenes y coordenadas
    
    pantalla.blit(arriba ,##cilindro hacia arriba
                 (pared, 360 + espacioCilindros - aparicion))##aparezcan los cilindros en un determinado 
    pantalla.blit(abajo,##llamamos a la variable abajo para la carga del cilindro 
                 (pared, 0 - espacioCilindros  - aparicion))
    pantalla.blit(font.render(str(contador),##llamamos solo al modulo que necesitamos
                              -1,
                             (255, 255, 255)),
            (200, 50))##posicion del conteo
    
    ##codigo para la aparicion de cada evento eimpresion en pantalla con sprites
    if dead:
      sprite = 2
    elif saltar:
      sprite = 1
    pantalla.blit(birdSprites[sprite], (70,birdY))
    if not dead:
      sprite = 0

    #aparicion en pantalla de cilindros aleatorios
    ##insertar mas de dos imagenes para la visualizacion de que se mueve la pantalla
    pared -= 2 ##conrol de velocidad que se produce el juego
    if pared < -80:##condicion para cruzar y aumentar el contador
      pared = 400
      contador += 1 ##contador aumenta
      aparicion = random.randint(-110, 110)  ##aparicion de los cilindros con numeros al azar

      
   ##codigo para control de gravedad y salto
    if saltar:
        ##casting para el cambio de controles y saltos
       velocidadSalto-= 1 ##cantidad de espacios al saltar mayor a 3 muy alto el espacio
       birdY -= velocidadSalto
       saltar-= 1##velocidad de la caida
    else:
      ##casting para la gravedad
          birdY +=gravedad ##posicion del pajaro igual a la gravedad con la que cae
          gravedad+= 0.2##velocidad que cae el objeto
    bird[1] = birdY ##casting que iguala al bird en posicion x e y
    levantarCilindro = pygame.Rect(pared,##espacios que existira entre los cilindros arriba
                             360 + espacioCilindros - aparicion + 10,
                             arriba.get_width() - 10, ##ANCHURA
                             arriba.get_height())##ALTURA
    bajarCilindro = pygame.Rect(pared,##espacios que existira entre los cilindros abajo
                               0 - espacioCilindros- aparicion - 10,##espacios que existira entre los cilindros
                               abajo.get_width() - 10,
                               abajo.get_height())
    if levantarCilindro.colliderect(bird):##condicion si llega a tocar un cilindro aparece el sprite muerto
            dead = True
    if bajarCilindro.colliderect(bird):##condicion si llega a tocar un cilindro aparece el sprite muerto
            dead = True
            
    if not 0 < bird[1] < 720:##espacio d ela pantalla hasta donde puede moverse el bird
            bird[1] = 50 ##posicion inicial cada que el juego repite en x
            birdY = 50##posicion ultima del pajaro en Y
            dead = False
            contador = 0 ##aumenta el contador
            pared = 400 ##espacio inicial entre la pared y el primer grupo de cilindros
            aparicion = random.randint(-110, 110) ##apariion de otro cilindro
            gravedad = 5 ##continua la gravedad

             ##controles del juego
    for event in pygame.event.get():##bucle para controles y muerte del juego que se repita
            if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not dead:##con dicion para controles con teclado mouse y aparicion del sprite muerte
                   saltar = 17 ##velocidad que toca aplatar el boton
                   gravedad = 5 ##gravedad que cae 
                   velocidadSalto = 10 ##velocidad o altura que cae el salto
            if (event.type == pygame.JOYAXISMOTION)and not dead:
                 if j.get_axis(1) >= 0.5:
                    saltar = 17 ##velocidad que toca aplatar el boton
                    gravedad = 5 ##gravedad que cae 
                    velocidadSalto = 10 ##velocidad o altura que cae el salto
                    #print ("Down has been pressed")  # Down
                 if j.get_axis(1) <= -1:
                    saltar = 17 ##velocidad que toca aplatar el boton
                    gravedad = 5 ##gravedad que cae 
                    velocidadSalto = 10 ##velocidad o altura que cae el salto
            if event.type == pygame.QUIT:##condicion para reiniciar el juego y datos almacenados
                    print('goodbye')
                    sys.exit()

    pygame.display.update()






   
