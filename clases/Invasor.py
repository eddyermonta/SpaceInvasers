from clases.Proyectil import proyectil
import pygame
from random import randint

class invasor(pygame.sprite.Sprite):
  
    def __init__(self,posx,posy,distancia,imagenUno,imagenDos,tipo):
        pygame.sprite.Sprite.__init__(self)
        
        #definimos las imagenes a y b para realizar la animacion de los personajes
        self.imagenA=pygame.image.load(imagenUno)
        self.imagenB=pygame.image.load(imagenDos)
        
        #tipo se refiere a cuanto vale la bonificacion de cada enemigo
        self.tipo=tipo

        # se crea las imagenes correspondientes y una posicion inicial
        self.listaImagenes=[self.imagenA,self.imagenB]
        self.posImagen=0

        #en donde se coloca la imagen del invasor
        self.imagenInvasor=self.listaImagenes[self.posImagen]
        self.rect=self.imagenInvasor.get_rect()

        self.listaDisparo=[]
        #velocidad del disparo y la referencias a la posicion x y y del invasor
        self.velocidadDisparo=1
        self.rect.top=posy
        self.rect.left=posx   
        
        #que tantos proyectiles lanza los enemigos
        self.rangoDisparo=0.5
        self.timeCambio=1

        self.conquista=False

        #por defecto los enemigos se mueven a la derecha
        self.derecha=True

        #este contador para determinar cuantas vueltas hacen los enemigos antes de descender
        self.contador=0

        #podemos limitar aca el descenso
        self.maxDescenso=self.rect.top

        #colocamos un limite de cuanto se puede mover tanto a la derecha como a la izquierda
        self.limiteDerecha=posx+distancia
        self.limiteIzquierda=posx-distancia
    
    #funcione que me determina la trayectoria 
    def trayectoria(self):
            self.rect.top-=self.velocidadDisparo 
    #dibuja los invasores  
    def dibujar(self, superficie):
        self.imagenInvasor=self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor,self.rect)
    #determina el comportamiento de los invasores tanto su movimiento y sus disparos
    def comportamiento(self, tiempo,alto):
        if self.conquista == False:
            self._movimientos(alto)
        
            self._ataque()       
            if self.timeCambio==tiempo:
                self.posImagen+=1
                self.timeCambio+=1

                if self.posImagen>len(self.listaImagenes)-1:
                    self.posImagen=0

    def _ataque(self):
        if(randint(0,100)<self.rangoDisparo):
            self._disparo()

    def _disparo(self):
        x,y=self.rect.center
        miproyectil=proyectil(x,y,"imagenes_pygame/disparob.jpg",False)    
        self.listaDisparo.append(miproyectil)

    def _movimientos(self,alto):
        if self.contador<1:
            self._movimientoLateral()
        else:
            self._descenso(alto)

    def _descenso(self,alto):
        if self.maxDescenso==self.rect.top:
            self.contador=0
            self.maxDescenso=self.rect.top+50
        elif self.maxDescenso==alto/2:
            self._movimientoLateral()
        else:
            self.rect.top+=1
    
    def _movimientoLateral(self):
        if self.derecha==True:
            self.rect.left+=self.velocidadDisparo
            if self.rect.left>self.limiteDerecha:
                self.derecha=False
                self.contador+=1
        else:
            self.rect.left-=self.velocidadDisparo
            if self.rect.left<self.limiteIzquierda:
                self.derecha=True
                self.contador+=1
