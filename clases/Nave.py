import pygame
from clases.Proyectil import proyectil

class NaveEspacial(pygame.sprite.Sprite):
    def __init__(self,ancho,alto):
        pygame.sprite.Sprite.__init__(self)
        #imagen para la animacion de la nave y explocion
        self.ImagenNave=pygame.image.load("imagenes_pygame/nave.jpg")
        self.ImagenExplosion=pygame.image.load("imagenes_pygame/explosion.jpg")
        #vidas de la nave
        self.salud=3

        #posicion de la bave en x y y
        self.rect=self.ImagenNave.get_rect()
        self.rect.centerx=ancho/2
        self.rect.centery=alto-30
    
        #disparos esta vivo velocidad y los sonidos correspondientes
        self.listaDisparo=[]
        self.vida=True
        self.velocidad=20
        self.sonidoDisparo=pygame.mixer.Sound("sonidos_pygame/DisparoLaser.wav")
        self.sonidoExplosion=pygame.mixer.Sound("sonidos_pygame/destruccion.wav")
   
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
        miProyectil=proyectil(x,y,"imagenes_pygame/disparoa.jpg",True)
        self.listaDisparo.append(miProyectil)
        self.sonidoDisparo.play()

    def destruccion(self):
        self.sonidoExplosion.play()
        self.vida=False
        self.velocidad=0
        self.ImagenNave=self.ImagenExplosion
        

    def dibujar(self, superficie):
        superficie.blit(self.ImagenNave,self.rect)
