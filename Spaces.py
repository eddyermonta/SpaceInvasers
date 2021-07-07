
import pygame,sys
from pygame.locals import *

ancho=900
alto=480

class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave=pygame.image.load("E:/USER/Documents/python/compu grafica/Space invaders/imagenes_pygame/nave.jpg")

        self.rect=self.ImagenNave.get_rect()
        self.rect.centerx=ancho/2
        self.rect.centery=alto-30

        self.listaDisparo=[]
        self.vida=True
        self.velocidad=20

    def movimientoDerecha(self):
        self.rect.right+=self.velocidad
        self._movimiento()

    def movimientoIzquierda(self):
        self.rect.left-=self.velocidad
        self._movimiento()

    def _movimiento(self):
        if self.vida==True:
            if self.rect.left<=0:
                self.rect.left=0
            elif self.rect.right>ancho:
                self.rect.right=ancho
    
    def disparar(self,x,y):
        miProyectil=proyectil(x,y)
        self.listaDisparo.append(miProyectil)

    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave,self.rect)

class proyectil(pygame.sprite.Sprite):
    
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagenProyectil=pygame.image.load("E:/USER/Documents/python/compu grafica/Space invaders/imagenes_pygame/disparoa.jpg")

        self.rect=self.imagenProyectil.get_rect()

        self.velocidadDisparo=5

        self.rect.top=posy
        self.rect.left=posx   

    def trayectoria(self):
            self.rect.top-=self.velocidadDisparo 
        
    def dibujar(self, superficie):
        superficie.blit(self.imagenProyectil,self.rect)


class Invasor(pygame.sprite.Sprite):

    
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.imagenA=pygame.image.load("E:/USER/Documents/python/compu grafica/Space invaders/imagenes_pygame/marcianoA.jpg")
        self.imagenB=pygame.image.load("E:/USER/Documents/python/compu grafica/Space invaders/imagenes_pygame/marcianoB.jpg")
        
        self.listaImagenes=[self.imagenA,self.imagenB]
        self.posImagen=0

        self.imagenInvasor=self.listaImagenes[self.posImagen]
        self.rect=self.imagenInvasor.get_rect()

        self.listaDisparo=[]
        self.velocidadDisparo=20
        self.rect.top=posy
        self.rect.left=posx   

        self.timeCambio=1


    def trayectoria(self):
            self.rect.top-=self.velocidadDisparo 
        
    def dibujar(self, superficie):
        self.imagenInvasor=self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor,self.rect)

    def comportamiento(self, tiempo):
        if self.timeCambio==tiempo:
            self.posImagen+=1
            self.timeCambio+=1

            if self.posImagen>len(self.listaImagenes)-1:
                self.posImagen=0
                
def spaceInvader():
    pygame.init()
    ventana=pygame.display.set_mode((ancho,alto))
    pygame.display.set_caption("Space Invader")
    ImagenFondo=pygame.image.load("E:/USER/Documents/python/compu grafica/Space invaders/imagenes_pygame/Fondo.jpg")
    
    jugador = NaveEspacial()
    enemigo=Invasor(100,100)
    #demoProyectil=proyectil(ancho/2,alto-30)
    enJuego=True
    reloj=pygame.time.Clock()
    while True:
        reloj.tick(60)
        #demoProyectil.trayectoria()
        tiempo=round(pygame.time.get_ticks()/1000,0)
        for evento in pygame.event.get():
            if evento.type==QUIT:
                pygame.quit()
                sys.exit()
            if enJuego==True:
                if evento.type==pygame.KEYDOWN:
                    if evento.key==K_LEFT:
                        jugador.movimientoIzquierda()
                    elif evento.key==K_RIGHT:
                        jugador.movimientoDerecha()
                    elif evento.key==K_s:
                        x,y=jugador.rect.center
                        jugador.disparar(x,y)
        ventana.blit(ImagenFondo,((0,0)))

        enemigo.comportamiento(tiempo)
        #demoProyectil.dibujar(ventana)

        jugador.dibujar(ventana)
        enemigo.dibujar(ventana)
        if len(jugador.listaDisparo)>0:
            for x in jugador.listaDisparo:
                x.dibujar(ventana)
                x.trayectoria()

                if x.rect.top<-10:
                    jugador.listaDisparo.remove(x)

        pygame.display.update()

spaceInvader()