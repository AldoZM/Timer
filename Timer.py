import pygame,sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("Hola")

fuente = pygame.font.SysFont("Arial",30)

aux=1

while True:
    ventana.fill((255,255,255))
    tiempo = pygame.time.get_ticks()/1000
    if aux==tiempo:
        aux+=1
        print (tiempo) 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    contador = fuente.render("Tiempo: "+str(tiempo),0,(120,70,0))
    ventana.blit(contador,(100,100))
    pygame.display.update()
