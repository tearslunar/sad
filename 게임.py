import pygame
import time
import sys
import random

#게임 목표 = 

#기본세팅
pygame.init()
screen = pygame.display.set_mode((420, 690))
pygame.display.set_caption("tears.Beta")

price0 = random.randrange(1000, 50000)
price1 = random.randrange(1000, 50000)
price2 = random.randrange(1000, 50000)
price3 = random.randrange(1000, 50000)
price4 = random.randrange(1000, 50000) #처음 시작할떄 주식 가격 정하기

#변수
item_use = 999
background = 0  
fatigue = 100
hp = 100
money = 0

#실행시 제작자 표현
start_tt = 0
font = pygame.font.SysFont("malgungothic", 40)
text0 = font.render("제", True, 'white')
text1 = font.render("작", True, 'white')
text2 = font.render(" ", True, 'white')
text3 = font.render(":", True, 'white')
text4 = font.render(" ", True, 'white')
text5 = font.render("", True, 'white')
text6 = font.render("", True, 'white')
text7 = font.render("", True, 'white')

#아이템 사용 폰트
font0 = pygame.font.SysFont("malgungothic", 40)

#fps
fps = pygame.time.Clock()

#아이템 리스트
item_list = [
    '물', '라면', '피로회복제', '안경', '샤프'
]

#함수
def screen_set(a, b, c):
    screen.blit(a, (b, c))
    
class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            screen.blit(img_act,(x_act, y_act))
            if click[0]:
                global background
                background =+ 1
                screen.fill('Black')
        else:
            screen.blit(img_in,(x,y))
            
def stock():
    price0 = random.randrange(1000, 50000)
    price1 = random.randrange(1000, 50000)
    price2 = random.randrange(1000, 50000)
    price3 = random.randrange(1000, 50000)
    price4 = random.randrange(1000, 50000)

    #print(price0, price1, price2, price3, price4) #확인용
    
text_list = [text0, text1, text2, text3, text4, text5, text6, text7]
text_x =[]
for i in range(8):
    text_x.append(i*32)

def start_text():
    
    for i in range(8):
        screen.blit(text_list[i], (70+text_x[i],280))
        pygame.display.update()
        time.sleep(0.2)
    time.sleep(1)
    

def item():  #아이템 사용 판단
    global font0
    global item_use
    global item_list
    
    if item_use == 0:
        text_item0 = font0.render("물을 마셨습니다.", True, 'White')
        screen.blit(text_item0, (70,280))
        item_use = 99
        
#마우스포인터 커스텀으로 변경
diamond = pygame.cursors.diamond
pygame.mouse.set_cursor(diamond)


#이미지 미리 불러오기   
start_background = pygame.image.load("사진\시작화면.png")
start_on = pygame.image.load("사진\START1.png")
start_off = pygame.image.load("사진\START.png")

#게임시작
def startgame():

    start_ticks = pygame.time.get_ticks() #5분 타이머용 
     
    global start_tt #전역변수 선언
    global item_use
    global money
    
    while True:
        
        fps.tick(120) #틱 120
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #키입력 받고 타입 전환하고 각 키의 대응하는 아이템
                if int(event.key) == 49:
                    item_use = 0
                    
        
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #5분 타이머
        
        if int(elapsed_time) % 303 == 0 and int(elapsed_time) != 0: #5분마다 주식갱신
            stock()
            time.sleep(1)
            
        if int(elapsed_time) % 10 == 0 and int(elapsed_time) != 0:
            money = money + 1000
        
        if start_tt == 0:   #실행시 제작자 표시
            start_text()
            start_tt =+ 1
            
        else:
            screen_set(start_background, 0, 0) #임시방편
        
        item()    #아이템 사용 판단
         
        #if background == 0:
        #    screen_set(start_background, 0, 0)
        #    Button(start_off,235,235,158,61,start_on,235,235)
        
        # elif background == 1:
        #    screen_set(start_background, 10, 10)
            
        pygame.display.update() #플레이 화면 업데이트

startgame() #게임시작 
pygame.quit()