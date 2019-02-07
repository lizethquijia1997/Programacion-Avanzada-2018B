import pygame ##libreria pygame importar paquetes
from pygame.locals import * ##colocar un grupo limitado de constantes dentro de un script
import sys ##acceso a variables
import random ##tener valores aleatorios
from random import randint
 

clock = pygame.time.Clock()##importo la libreria de tiempo

pygame.init()##variable para cargar sonido
pygame.mixer.music.load('imagenes/flappyBird.mp3')
pygame.mixer.music.play()


pygame.joystick.init()  # variable para cargar el joystick
try:
	j = pygame.joystick.Joystick(0) # igualamos una variable para cargar la palanca
	j.init() # ubicamos una instancia
	print ("Enabled joystick: {0}".format(j.get_name()))#imprimimos si lee el joytick
except pygame.error:
	print ("no joystick found.")#no lee el joystick


pantalla= pygame.display.set_mode((400, 700))##medidas de la ventana ancho y alto
fondo = pygame.image.load("imagenes/fondo.png").convert()##cargar la imagen de fondo
pygame.display.set_caption("Flappy Bird")##titulo
bird = pygame.Rect(65, 50, 50, 50)##configura al personaje de fondo almacenar para en espacio rectangulares


##cargar sprites aplicando la sinaxis pygamE
##convert.alpha() me servira para imprimir el evento cuando se lo llama
birdSprites = [pygame.image.load("imagenes/1.png").convert_alpha(),
                pygame.image.load("imagenes/2.png").convert_alpha(),
                pygame.image.load("imagenes/muerto.png")]
arriba = pygame.image.load("imagenes/cilindroArriba.png").convert_alpha()
abajo = pygame.image.load("imagenes/cilindroAbajo.png").convert_alpha()


##codigo para el conteo en el juego
pygame.font.init()##modulo inicializado a mano
font = pygame.font.SysFont("Arial", 50) ##tipo de letra para el contador

##bucle para la repeticion de juegos

 
# Defino algunos colores que voy a utilizar
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 250, 0)
RED = (250, 0, 0)
LIGHTRED =(200, 0, 0)
LIGHTGREEN =(0, 200, 0)
LIGHTBLUE = (0, 0, 250)
BLUE = (121, 151, 247)
PURPLE =(181, 34, 230)
LIGHTPURPLE =(218, 167, 235)
BLUEBACKGROUND = (94, 196, 230)
YELLOW = (250, 242, 22)
LIGHTYELLOW = (250, 246, 122)
GREENOBSTACLE = (103, 235, 59)
DARKGREENOBSTACLE = (101, 168, 79)
VERYDARKGREENOBSTACLE = (50, 94, 57)

pygame.init()
size = (400, 700)
screen = pygame.display.set_mode(size)


# Inital set of variables
done = False
scorePoints = 0
x = 350
y = 250
ySpeed = 2
xSpeed = 0
xPos =700
yPos = 0
xSize = 70
ySize = randint(0, 350)
space = 200
obSpeed = 2.5
ground = 460
gOver=False
scoreList=[]
pause=False


clock = pygame.time.Clock()

#FUNCIONES
# funcion para escribir el texto
def printText(msg, x, y, size):
    font = pygame.font.SysFont(None, size)
    text = font.render (msg, True, BLACK)
    screen.blit(text, [x, y])

# Displays Game Over and final score
def gameOver():
    printText("GAME OVER", 180, 100, 75)
    printText("tu puntuacion: "+str(scorePoints), 230, 150, 50)




# funcion standard para la presentacion
def textObjects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()
    pygame.display.update()
    time.sleep(2)
    gameLoop()

# Crear funvion para alguna accion
def button(msg, x, y, w, h, iColor, aColor, action =None, prev = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

# posicion del mouse para acceder a una ventana
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, iColor,(x,y,w,h))
        if click[0] == 1 and action != None:
             if not prev:
                 action()
             else:
                 action(prev)
    else:
        pygame.draw.rect(screen, aColor,(x,y,w,h))

    smallText = pygame.font.SysFont(None, 20)
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect = textObjects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

# Menu de inicializacion
def gameIntro():

    listScr=False
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(BLUEBACKGROUND)
        printText("Flappy Bird", 90, 100, 75)

#botones del menu
        button("EMPEZAR",90,200,300,40, GREEN, LIGHTGREEN, gameLoop)
        button("PUNTUACIONES", 90, 300, 300, 40, BLUE, LIGHTBLUE, listScreen)
        button("SALIR",90,400,300,40, RED, LIGHTRED, gameQuit)

        pygame.display.update()
        clock.tick(15)
# pantalla d emenu de pausa
def gamePause():
    global pause
    listScr=False
    pause=True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(BLUEBACKGROUND)
        printText("PAUSED", 260, 100, 75)

        button("EMPEZAR",210,200,300,40, GREEN, LIGHTGREEN, gameLoop)
        button("SALIR",210,350,300,40, RED, LIGHTRED, gameQuit)
        pygame.display.update()
        clock.tick(15)



   
# Para aquellas pantallas con botón de REGRESAR, la pantalla de fuente de parámetro muestra dónde volver
        if sourceScreen == "pause":
            button("REGRESAR",0,0,100,50, GREEN, LIGHTGREEN, gamePause)
        else:
            button("REGRESAR",0,0,100,50, GREEN, LIGHTGREEN, gameIntro)

        pygame.display.update()
        clock.tick(15)

# PUNTUACIONES
def listScreen():
    global scorePoints
    global listScr
    listScr=True
    while listScr:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(BLUEBACKGROUND)
        printText("PUNTUACIONES", 50, 50, 50)

# Mostrar la lista de los diez primeros en orden
        y=0
        if gOver == True:
            if len(scoreList) > 10:
                for i in range(10):
                    printText("%s.............................  %s"%(i+1,scoreList[i]), 250, 180+y, 30)
                    y+=25
            else:   
                for i in range(len(scoreList)):
                    printText("%s.............................  %s"%(i+1,scoreList[i]), 250, 180+y, 30)
                    y+=25

        button("REGRESAR",0,0,100,50, GREEN, LIGHTGREEN, gameIntro)
        scorePoints=0

        pygame.display.update()
        clock.tick(15)

# Crea y administra la lista de las diez mejores puntuaciones.
def scoreTopTen(scorePoints):
    if scorePoints != 0:
        scoreList.append(int(scorePoints))
        scoreList.sort()
        scoreList.reverse()
        return scoreList
    else:
        return scoreList
    


# salir
def gameQuit ():
    intro=False
    pygame.quit()
    quit()


def gameLoop():
        
## variables para posiciones y eventos 
      pared= 400##posicion de inicializacion
      espacioCilindros = 130 ##espacio entre cilindros
      aparicion = random.randint(-110, 110)##compensar espacios y movimientos para que aparezacan los cilindros
      sprite = 0 ##variable para sprites
      birdY = 350##variable para la posicion en y del bird
      dead = False
      saltar = 0
      contador = 0 ##contador
      velocidadSalto = 10 ##velocidad del pajaro
      gravedad = 5 ##velocidad con la que va cayendo el ave
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
        sprite = 2##sprite muerto
      elif saltar:
        sprite = 1##sprite volando
        pantalla.blit(birdSprites[sprite], (70,birdY))
      if not dead:
        sprite = 0##sprite posicion natural
      
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
      pygame.display.update()##imprimir imagenes

    

    ##controles del juego
      for event in pygame.event.get():##bucle para controles y muerte del juego que se repita
             if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not dead:##con dicion para controles con teclado mouse y aparicion del sprite muerte
                   saltar = 17 ##velocidad que toca aplatar el boton
                   gravedad = 5 ##gravedad que cae 
                   velocidadSalto = 10 ##velocidad o altura que cae el salto
            
             if (event.type == pygame.JOYAXISMOTION)and not dead:  # Joystick
                   saltar = 17 ##velocidad que toca aplatar el boton
                   gravedad = 5 ##gravedad que cae 
                   velocidadSalto = 10 ##velocidad o altura que cae el salto
        
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           done = True
           print('goodbye')
           sys.exit()
    gameIntro()
    

    











 
