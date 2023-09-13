import pygame
import time
import sys
import random

#게임 목표 = 급격하게 생계가 안좋아지자 대대로 내려오는 가보를 팔아 어떻게든 살다가 20살이되고 열심히 일하고 돈을벌어서
#가보를 되찾자

#변수
item_use = 999
background = 0  
fatigue = 100
hp = 100
money = 0

price0 = random.randrange(1000, 50000)
price1 = random.randrange(1000, 50000)
price2 = random.randrange(1000, 50000)
price3 = random.randrange(1000, 50000)
price4 = random.randrange(1000, 50000) #처음 시작할떄 주식 가격 정하기

#아이템 리스트
item_list = [
    '물', '라면', '피로회복제', '안경', '샤프'
]

#불러오기용 텍스트 파일 만들기 & 불러오기에 필요한 변수들 만들기
status = open("status", "w")
status.write("fatigue : \n")
status.write("hp : \n")
status.write("money : \n")

#편의성을 위한 함수 정의
    
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

    #print(price0, price1, price2, price3, price4)
    

    
    


#fps
fps = pygame.time.Clock()

            
pygame.init()
screen = pygame.display.set_mode((420, 690))
pygame.display.set_caption("tears.Beta")

#마우스포인터 커스텀으로 변경
diamond = pygame.cursors.diamond
pygame.mouse.set_cursor(diamond)


#이미지 미리 불러오기   
start_background = pygame.image.load("사진\시작화면.png")
start_on = pygame.image.load("사진\START1.png")
start_off = pygame.image.load("사진\START.png")

font0 = pygame.font.SysFont("malgungothic", 40)
def item():
    global font0
    global item_use
    global item_list
    
    if item_use == 0:
        text_item0 = font0.render("물을 마셨습니다\
                                  체력과 피로가 각각 10씩 회복됩니다.", True, 'White')
        screen.blit(text_item0, (70,280))
        print('000000')
        pygame.display.update()
        item_use = 999

#시작화면 이미지 설정
#screen_set(start_background, 0, 0)
start_tt = 0
font = pygame.font.SysFont("malgungothic", 40)
text0 = font.render("제", True, 'white')
text1 = font.render("작", True, 'white')
text2 = font.render(" ", True, 'white')
text3 = font.render(":", True, 'white')
text4 = font.render(" ", True, 'white')
text5 = font.render("오", True, 'white')
text6 = font.render("현", True, 'white')
text7 = font.render("동", True, 'white')

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



def startgame():

    start_ticks = pygame.time.get_ticks()
    
    global start_tt
    global item_use
    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN: #키입력 받고 타입 전환하고 각 키의 대응하는 숫자
                if int(event.key) == 49:
                    item_use = 0
                    
        
        elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
        
        if int(elapsed_time) % 303 == 0 and int(elapsed_time) != 0: #5분마다 주식갱신
            stock()
            time.sleep(1)
        
        if start_tt == 0:   #실행시 제작표시
            start_text()
            start_tt =+ 1
            
        else:
            screen_set(start_background, 0, 0)
        
        item()                                      #아이템 사용 판단
         
        
        #if background == 0:
        #    screen_set(start_background, 0, 0)
        #    Button(start_off,235,235,158,61,start_on,235,235)
        
        # elif background == 1:
        #    screen_set(start_background, 10, 10)
            
        pygame.display.update()
        fps.tick(120)

startgame()

status.close()
pygame.quit()