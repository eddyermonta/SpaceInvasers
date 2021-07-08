from clases.Proyectil import proyectil
import pygame
from random import randint

class invasor(pygame.sprite.Sprite):
  
    def __init__(self,posx,posy,distancia,imagenUno,imagenDos):
        pygame.sprite.Sprite.__init__(self)
        self.imagenA=pygame.image.load(imagenUno)
        self.imagenB=pygame.image.load(imagenDos)
        
        self.listaImagenes=[self.imagenA,self.imagenB]
        self.posImagen=0

        self.imagenInvasor=self.listaImagenes[self.posImagen]
        self.rect=self.imagenInvasor.get_rect()

        self.listaDisparo=[]
        self.velocidadDisparo=1
        self.rect.top=posy
        self.rect.left=posx   

        self.rangoDisparo=0.5
        self.timeCambio=1

        self.conquista=False

        self.derecha=True
        self.contador=0
        self.maxDescenso=self.rect.top+20

        self.limiteDerecha=posx+distancia
        self.limiteIzquierda=posx-distancia
    def trayectoria(self):
            self.rect.top-=self.velocidadDisparo 
        
    def dibujar(self, superficie):
        self.imagenInvasor=self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenInvasor,self.rect)

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
        miproyectil=proyectil(x,y,"D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/imagenes_pygame/disparob.jpg",False)    
        self.listaDisparo.append(miproyectil)

    def _movimientos(self,alto):
        if self.contador<3:
            self._movimientoLateral()
        else:
            self._descenso(alto)

    def _descenso(self,alto):
        if self.maxDescenso==self.rect.top:
            self.contador=0
            self.maxDescenso=self.rect.top+20
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
