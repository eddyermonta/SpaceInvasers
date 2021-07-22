
from clases.vida import vida
import pygame,sys
from pygame.locals import *
from random import randint
from clases.Nave import NaveEspacial
from clases.Invasor import invasor

import time

ancho=900
alto=480
#carga los enemigos
listaEnemigo=[]
listaVidas=[]


#carga el inicio de la ventana
def inicio(ventana):
    ini=pygame.image.load("imagenes_pygame/Inicio.png")
    ventana.blit(ini,((0,0)))
    pygame.display.update()
    time.sleep(2)
#para el juego
def detenerTodo():
    for enemigo in listaEnemigo:
        for disparo in enemigo.listaDisparo:
            enemigo.listaDisparo.remove(disparo)
            enemigo.conquista=True
#carga los tipos de invasores y su posicion inicial
def cargarEnemigos():
    x=100
    for i in range(3):
        x+=100
        enemigoA=invasor(x,0,200,"imagenes_pygame/marciano3B.jpg","imagenes_pygame/marciano3B.jpg",10)
        listaEnemigo.append(enemigoA)
    x=100
    for i in range(3):
        x+=100
        enemigoB=invasor(x,80,200,"imagenes_pygame/marciano2A.jpg","imagenes_pygame/marciano2B.jpg",20)
        listaEnemigo.append(enemigoB)
    x=115
    for i in range(3):
        x+=100
        enemigoC=invasor(x,160,200,"imagenes_pygame/marcianoA.jpg","imagenes_pygame/marcianoB.jpg",30)
        listaEnemigo.append(enemigoC)
#carga las vidas
def cargarVidas():
    x=50
    for i in range(3):
        x+=50
        vidas=vida(x,alto-50,"imagenes_pygame/vida.png")
        listaVidas.append(vidas)
#ventana del end game
def fin_juego(ventana):
    finJuego=pygame.image.load("imagenes_pygame/Mori.png")
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
    #set caption es el titulo de la ventana
    pygame.display.set_caption("Space Invader")
    ImagenFondo=pygame.image.load("imagenes_pygame/Fondo.jpg")
    inicio(ventana)
    #sonidos del juego
    pygame.mixer.music.load('sonidos_pygame/Intro.mp3')
    pygame.mixer.music.play(100)

    #fuente para el programa
    miFuenteSistema=pygame.font.SysFont("Arial",30)
    
    #donde se guarda los puntajes
    puntaje = 0

    #carga jugadores invasores y vidas
    jugador = NaveEspacial(ancho,alto)
    cargarEnemigos()
    cargarVidas()
    
    #en juego para saber si todavia esta en juego que se mueva la nave o si no no se mueve
    enJuego=True
    #los fps
    reloj=pygame.time.Clock()

    while True:
        #vamos a 60 fps
        reloj.tick(60)
        tiempo=round(pygame.time.get_ticks()/1,000)
        #formato de score
        tPuntaje='SCORE:{0000}'.format(puntaje)
        #color del score y se le mete el puntaje al score
        Texto=miFuenteSistema.render(tPuntaje,True,(0,255,0))
        
        #evento para salir
        for evento in pygame.event.get():
            if evento.type==QUIT:
                pygame.quit()
                sys.exit()
        #si estoy jugando me puedo mover y disparar
            if enJuego==True:
                if evento.type==pygame.KEYDOWN:
                    if evento.key==K_LEFT:
                        jugador.movimientoIzquierda(ancho)
                    elif evento.key==K_RIGHT:
                        jugador.movimientoDerecha(ancho)
                    elif evento.key==K_s:
                        x,y=jugador.rect.center
                        jugador.disparar(x,y)
        #dibuje el fonto y la nave
        ventana.blit(ImagenFondo,((0,0)))
        jugador.dibujar(ventana)
        #programacion del disparo del jugador
        if len(jugador.listaDisparo)>0:
            #dibuje el disparo
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()
                #si sale de la pantalla superior borrelo
                if x.rect.top<-10:
                    jugador.listaDisparo.remove(x)
                else: 
                    #si colisiona con el enemigo me va a dar un puntaje 
                    for enemigo in listaEnemigo:
                        if x.rect.colliderect(enemigo.rect):
                            listaEnemigo.remove(enemigo)
                            jugador.listaDisparo.remove(x)
                            
                            puntaje+=enemigo.tipo
                            #si hay 0 enemigos ya gane
                            if len(listaEnemigo)==0:
                                ventana.blit(Texto,((50,50)))
                                fin_juego(ventana)

       #comportamiento enemigo y dibuje
        if len(listaEnemigo)>0:
            for enemigo in listaEnemigo:
                enemigo.comportamiento(tiempo,alto)
                enemigo.dibujar(ventana)
                #si enemigo colisiona con el jugador se muere
                if enemigo.rect.colliderect(jugador.rect):
                    ventana.blit(Texto,((50,50)))
                    jugador.destruccion()
                    jugador.dibujar(ventana)
                    enJuego=False
                    detenerTodo()
                    fin_juego(ventana)
                #dibuje disparos de los enemigos    
                if len(enemigo.listaDisparo)>0:
                    for x in enemigo.listaDisparo:
                        x.dibujar(ventana)
                        x.trayectoria()

                       #si el disparo del enemigo colisiona con el jugador pierde salud se borra un dibujo de las vidas
                        if x.rect.colliderect(jugador.rect):
                            enemigo.listaDisparo.remove(x)
                            jugador.salud=jugador.salud-1
                            print(jugador.salud)
                            for corazones in listaVidas:
                                listaVidas.remove(corazones)
                            #si ya no le quedan vidas game over
                            if jugador.salud==0:
                                jugador.destruccion()
                                jugador.dibujar(ventana)
                                enJuego=False
                                ventana.blit(Texto,((50,50)))
                                detenerTodo()
                           #si el diparo se sale de la pantalla inferior se remueve
                        if x.rect.top>alto:
                            enemigo.listaDisparo.remove(x)
                            
                        #si los disparos colisionan entre ellos se remueven ambos
                        else:
                            for disparo in jugador.listaDisparo:
                                if x.rect.colliderect(disparo.rect):
                                    jugador.listaDisparo.remove(disparo)
                                    enemigo.listaDisparo.remove(x)
        #si hay vidas que dibujar dibujelas las 3 vidas                          
        if len(listaVidas)>0:
            for vidas in listaVidas:
                vidas.dibujar(ventana)
                len(listaVidas)
        #si murio musica de fin de juego
        if enJuego== False:
            pygame.mixer.music.fadeout(3000)
            #fin de juego
            fin_juego(ventana)
        #ventana de intente de nuevo
        ventana.blit(Texto,((50,50)))
        pygame.display.update()

spaceInvader()

