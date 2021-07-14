
import pygame,sys
from pygame.locals import *
from random import randint
from clases.Nave import NaveEspacial
from clases.Invasor import invasor
import time

ancho=900
alto=480
listaEnemigo=[]

def inicio(ventana):
    ini=pygame.image.load("D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/imagenes_pygame/Inicio.png")
    ventana.blit(ini,((0,0)))
    pygame.display.update()
    time.sleep(2)

def detenerTodo():
    for enemigo in listaEnemigo:
        for disparo in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparo)
            enemigo.conquista=True

def cargarEnemigos():
    x=100
    for i in range(3):
        x+=100
        enemigoA=invasor(x,0,200,"D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/imagenes_pygame/marciano3A.jpg","D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/imagenes_pygame/marciano3B.jpg")
        listaEnemigo.append(enemigoA)
    x=100
    for i in range(3):
        x+=100
        enemigoB=invasor(x,80,200,"D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/imagenes_pygame/marciano2A.jpg","D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/imagenes_pygame/marciano2B.jpg")
        listaEnemigo.append(enemigoB)
    x=115
    for i in range(3):
        x+=100
        enemigoC=invasor(x,160,200,"D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/imagenes_pygame/marcianoA.jpg","D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/imagenes_pygame/marcianoB.jpg")
        listaEnemigo.append(enemigoC)
        
def fin_juego(ventana):
    finJuego=pygame.image.load("D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/imagenes_pygame/Mori.png")
    ventana.blit(finJuego,((ancho/2)-100,(alto/2)-100)) #fub del juego
    pygame.display.update()
    while(True):
        for eventos in pygame.event.get():
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                x,y= eventos.pos
                if(x>=398 and y>=251 and x<=503 and y<=265):
                    spaceInvader()
                elif(x>=398 and y>=275 and x<=497 and y<=296):
                    print("about")
                elif(x>=435 and y>=309 and x<=459 and y<=330):
                    exit()
        ventana.blit(finJuego,((ancho/2)-100,(alto/2)-100))
        pygame.display.update()

def spaceInvader():
    pygame.init()
    ventana=pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space Invader")
    ImagenFondo=pygame.image.load("D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/imagenes_pygame/Fondo.jpg")
    inicio(ventana)
    pygame.mixer.music.load('D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/sonidos_pygame/Intro.mp3')
    #pygame.mixer.music.play(100)

    miFuenteSistema=pygame.font.SysFont("Arial",30)
    Texto=miFuenteSistema.render("covid",0,(120,100,40))
    
    jugador = NaveEspacial(ancho,alto)
    cargarEnemigos()

    enJuego=True
    reloj=pygame.time.Clock()

    while True:
        reloj.tick(60)
        tiempo=round(pygame.time.get_ticks()/1,000)

        for evento in pygame.event.get():
            if evento.type==QUIT:
                pygame.quit()
                sys.exit()

            if enJuego==True:
                if evento.type==pygame.KEYDOWN:
                    if evento.key==K_LEFT:
                        jugador.movimientoIzquierda(ancho)
                    elif evento.key==K_RIGHT:
                        jugador.movimientoDerecha(ancho)
                    elif evento.key==K_s:
                        x,y=jugador.rect.center
                        jugador.disparar(x,y)

        ventana.blit(ImagenFondo,((0,0)))

        jugador.dibujar(ventana)

        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                if x.rect.top<-10:
                    jugador.listaDisparo.remove(x)
                else: 
                    for enemigo in listaEnemigo:
                        if x.rect.colliderect(enemigo.rect):
                            listaEnemigo.remove(enemigo)
                            jugador.listaDisparo.remove(x)
                            if(len(listaEnemigo)==0):
                                inicio(ventana)
                                detenerTodo()
                             #->bonificaciones

       
        if len(listaEnemigo)>0:
            for enemigo in listaEnemigo:
                enemigo.comportamiento(tiempo,alto)
                enemigo.dibujar(ventana)

                if enemigo.rect.colliderect(jugador.rect):
                    jugador.destruccion()
                    enJuego=False
                    detenerTodo()

                if len(enemigo.listaDisparo)>0:
                    for x in enemigo.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()

                        if x.rect.colliderect(jugador.rect):
                            jugador.destruccion()
                            enJuego=False
                            detenerTodo()

                        if x.rect.top>alto:
                            enemigo.listaDisparo.remove(x)
                            

                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    enemigo.listaDisparo.remove(x)
                                    
        if enJuego== False:
            #pygame.mixer.music.fadeout(3000)
            fin_juego(ventana)
            
        
        pygame.display.update()

spaceInvader()

