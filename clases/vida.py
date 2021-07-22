import pygame
class vida(pygame.sprite.Sprite):
    def __init__(self,posx,posy,imagen):
        pygame.sprite.Sprite.__init__(self)
         #imagen de las vidas
        self.imagen=pygame.image.load(imagen)
         #lista de vidas
        self.listaImagenes=[self.imagen]
        self.posImagen=0
         #posiciones de las vidas x y
        self.imagenVIDA=self.listaImagenes[self.posImagen]
        self.rect=self.imagenVIDA.get_rect()

        self.rect.top=posy
        self.rect.left=posx
 #dibuje las vidas
    def dibujar(self, superficie):
        self.imagenVIDA=self.listaImagenes[self.posImagen]
        superficie.blit(self.imagenVIDA,self.rect)