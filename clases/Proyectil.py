import pygame

class proyectil(pygame.sprite.Sprite):
    
    def __init__(self,posx,posy,ruta,personaje):
        pygame.sprite.Sprite.__init__(self)
        #imagen del proyectil
        self.imagenProyectil=pygame.image.load(ruta)
        #posicion del proyectil
        self.rect=self.imagenProyectil.get_rect()
        #velocidad del proyectil
        self.velocidadDisparo=5
         #posicion del proyectil x y
        self.rect.top=posy
        self.rect.left=posx   

        self.disparoPersonaje=personaje
     #trayectoria del disparo de los proyectiles
    def trayectoria(self):
            if self.disparoPersonaje:
                self.rect.top-=self.velocidadDisparo 
            else:
                self.rect.top+=self.velocidadDisparo 
    #dibuja los proyectiles    
    def dibujar(self, superficie):
        superficie.blit(self.imagenProyectil,self.rect)