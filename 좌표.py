import pygame

a = 0
pygame.init()
width , height = 420, 690
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tears_Roguelike.Beta")

start_background = pygame.image.load("사진\시작화면.png")
def screen_set(a, b, c):
    screen.blit(a, (b, c))
screen_set(start_background, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False 
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print(pygame.mouse.get_pos())
    pygame.display.update()