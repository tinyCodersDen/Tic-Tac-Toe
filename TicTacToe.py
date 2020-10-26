import pygame
from pygame.locals import *
import time
pygame.init()
pygame.mixer.pre_init(44100,16,2,4096)
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic Tac Toe")
turn='x'
check1=False
class Box():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.ocuppant=False
        self.type=''
        pygame.draw.rect(screen,(0,0,255),(self.x-100,self.y-100,200,200),1)
    def isclicked(self,pos):
        global turn
        global check1
        if pos[0]>=self.x-100 and pos[0]<=self.x+100 and pos[1]>=self.y-100 and pos[1]<=self.y+100 and self.ocuppant==False:
            self.ocuppant=True
            check1=True
            if turn=='o':
                pygame.draw.circle(screen,(0,255,255),(self.x,self.y),100)
                self.type='o'
            else:
                self.type='x'
                pygame.draw.line(screen,(0,255,255),(self.x-100,self.y-100),(self.x+100,self.y+100))
                pygame.draw.line(screen,(0,255,255),(self.x+100,self.y-100),(self.x-100,self.y+100))
boxlist=[]
for w in range(100,600,200):
        for wc in range(100,600,200):
            b1=Box(w,wc)
            boxlist.append(b1)
font=pygame.font.Font('freesansbold.ttf',50)
pygame.mixer.music.load('Low_Life_High_Life (3).mp3')
pygame.mixer.music.play(-1)
while True:
    check=False
    for u in boxlist:
        if u.ocuppant==True:
            pass
        else:
            check=True
    if check==False:
        text=font.render('DRAW!',False,(255,255,255))
        screen.blit(text,(215,300))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        exit()
    for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type==MOUSEBUTTONDOWN:
                check1=False
                for a in boxlist:
                    a.isclicked(event.pos)
                if check1==True:
                    if turn=='o':
                        turn='x'
                    else:
                        turn='o'
    pygame.display.update()
    if (boxlist[0].type=='x' and boxlist[1].type=='x' and boxlist[2].type=='x') or (boxlist[3].type=='x' and boxlist[4].type=='x' and boxlist[5].type=='x') or (boxlist[6].type=='x' and boxlist[7].type=='x' and boxlist[8].type=='x') or (boxlist[0].type=='x' and boxlist[4].type=='x' and boxlist[8].type=='x') or (boxlist[6].type=='x' and boxlist[4].type=='x' and boxlist[2].type=='x') or (boxlist[0].type=='x' and boxlist[3].type=='x' and boxlist[6].type=='x') or (boxlist[1].type=='x' and boxlist[4].type=='x' and boxlist[7].type=='x') or (boxlist[2].type=='x' and boxlist[5].type=='x' and boxlist[8].type=='x'):
        text=font.render("X Wins",False,(255,255,255))
        screen.blit(text,(215,300))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        exit()
    if (boxlist[0].type=='o' and boxlist[1].type=='o' and boxlist[2].type=='o') or (boxlist[3].type=='o' and boxlist[4].type=='o' and boxlist[5].type=='o') or (boxlist[6].type=='o' and boxlist[7].type=='o' and boxlist[8].type=='o') or (boxlist[0].type=='o' and boxlist[4].type=='o' and boxlist[8].type=='o') or (boxlist[6].type=='o' and boxlist[4].type=='o' and boxlist[2].type=='o') or (boxlist[0].type=='o' and boxlist[3].type=='o' and boxlist[6].type=='o') or (boxlist[1].type=='o' and boxlist[4].type=='o' and boxlist[7].type=='o') or (boxlist[2].type=='o' and boxlist[5].type=='o' and boxlist[8].type=='o'):
        text=font.render("O Wins",False,(255,255,255))
        screen.blit(text,(215,300))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
        exit()