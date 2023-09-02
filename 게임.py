import pickle
import pygame
import time
import sys

#변수
fatigue = 0
hp = 100
money = 0

#불러오기용 텍스트 파일 만들기 & 불러오기에 필요한 변수들 만들기
status = open("status", "w")
status.write("fatigue : \n")
status.write("hp : \n")
status.write("money : \n")

#편의성을 위한 함수 정의
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

bitmap_2 = pygame.cursors.Cursor(
    (24, 24), (0, 0), *pygame.cursors.compile(pygame.cursors.thickarrow_strings)
)
pygame.mouse.set_cursor(bitmap_2)


#이미지 미리 불러오기
start_background = pygame.image.load("사진\시작화면.png")

#시작화면 이미지 설정
screen_set(start_background, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False 
    pygame.display.update()

status.close()
pygame.quit()