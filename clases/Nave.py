import pygame
from clases.Proyectil import proyectil

class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self,ancho,alto):
        pygame.sprite.Sprite.__init__(self)
        self.ImagenNave=pygame.image.load("D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/imagenes_pygame/nave.jpg")

        self.rect=self.ImagenNave.get_rect()
        self.rect.centerx=ancho/2
        self.rect.centery=alto-30

        self.listaDisparo=[]
        self.vida=True
        self.velocidad=20
        self.sonidoDisparo=pygame.mixer.Sound("D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/sonidos_pygame/DisparoLaser.wav")

    def movimientoDerecha(self,ancho):
        self.rect.right+=self.velocidad
        self._movimiento(ancho)

    def movimientoIzquierda(self,ancho):
        self.rect.left-=self.velocidad
        self._movimiento(ancho)

    def _movimiento(self,ancho):
        if self.vida==True:
            if self.rect.left<=0:
                self.rect.left=0
            elif self.rect.right>ancho:
                self.rect.right=ancho
    
    def disparar(self,x,y):
        miProyectil=proyectil(x,y,"D:/Usuario/Documentos/Eduardo/Utp/semestre 5/computacion grafica/parte3/Space invaders/imagenes_pygame/disparoa.jpg",True)
        self.listaDisparo.append(miProyectil)
        self.sonidoDisparo.play()

    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave,self.rect)
