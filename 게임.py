import pygame
import time
import sys

#편의성을 위한 함수 정
def screen_set(a, b, c):
    screen.blit(a, (b, c))
    
class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act,(x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            screen.blit(img_in,(x,y))
            
pygame.init()
width , height = 420, 690
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tears_identity.Beta")

#이미지 미리 불러오기
start_background = pygame.image.load("사진\시작화면1.png")
start_click = pygame.image.load("사진\startclick.png")
end_click = pygame.image.load("사진\endclick.png")

#시작화면 이미지 설정
screen_set(start_background, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False 
    startButton = Button(start_click,280,260, 220,90,end_click,280,260,None)
    pygame.display.update()

pygame.quit()

