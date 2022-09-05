# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 13:14:09 2022

@author: Toqa Alaa
"""
import sys
import pygame
import time
import random

def quit():
    sys.exit()

pygame.init()

white= (255,255,255)
black =(0,0,0)
red= (255,0,0)
green= (0,155,0)
blue= (0,255,0)
light_blue = (188, 221, 254)
dark_blue= (2,45,87)
near_black= (0,0 ,66)
dark_yellow= (190, 177, 16)
default_color =(91,191,26)
light_yellow= (239,243,152)


display_width= 800
display_height= 600

gameDisplay= pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("SNACK GAME")


head_img= pygame.image.load('Head3.png')
apple_img= pygame.image.load('apple3.png')



clock= pygame.time.Clock()
block_size =20

FPS=30


direction ="right"


small_font= pygame.font.SysFont("comicsansms", 25)
medium_font=  pygame.font.SysFont("comicsansms", 40)
large_font= pygame.font.SysFont("comicsansms", 70)
End_font= pygame.font.Font('Nosifer-Regular.ttf', 70)

def pause():
    paused= True
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_c:
                    paused= False
                elif event.key==pygame.K_q:
                    pygame.quit()
                    quit()
            gameDisplay.fill(white)
            message_to_screen("Paused"
                              ,black
                              , -100
                              , size= "large")
            
            message_to_screen("Press C to continue or Q to quit"
                              , black
                              , 25)
            
            pygame.display.update()
            clock.tick(15)
                              
def score(score):
    text= small_font.render("Score: "+ str(score), True, black)
    gameDisplay.blit(text, [0,0])
    

def randApple():
    randApplex= round(random.randrange(0, display_width- block_size))#/10.0)*10.0
    randAppley= round(random.randrange(display_height- block_size))#/10.0)*10.0
    
    return randApplex, randAppley


def intro():
    intro = True
    
    while intro:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_c:
                    intro= False
                if event.key== pygame.K_q:
                    pygame.quit()
                    quit()
                    
                    
        gameDisplay.fill(light_blue)
        message_to_screen("Welcome to snake game",
                          dark_blue
                          , -100
                          , size= "large")
        message_to_screen("Eat apples as much as you can"
                          ,dark_yellow, -20)
        message_to_screen("If you cross your self or the edges you will die"
                          , near_black, 20)
        
        message_to_screen("Press C to continue,  Q to quit, P to pause"
                          , near_black, 120)
        
        
        
        pygame.display.update()
        clock.tick(15)
        


def snake(block_size, snakelist):
    
    if direction=="right":
        head= pygame.transform.rotate(head_img, 270)
    if direction=="left":
        head= pygame.transform.rotate(head_img, 90)
    if direction=="up":
        head= head_img
        
    if direction=="down":
        head= pygame.transform.rotate(head_img, 180)
        
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist [:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1],block_size ,block_size])

def text(text, color, size):
    if size == "small":
        text_surface= small_font.render(text, True, color)
    if size == "medium":
        text_surface= medium_font.render(text, True, color)
    
    if size == "large":
        text_surface= large_font.render(text, True, color)
    if size == "End":
        text_surface= End_font.render(text, True, color)
    
    return text_surface, text_surface.get_rect()

def message_to_screen(msg,color, y_value=0, size= "small"):
    text_surface, text_rect=  text(msg, color, size)
    text_rect.center= (display_width/2), display_height/2+ y_value
    gameDisplay.blit(text_surface, text_rect)
    
"""
def welcome_message(msg,color):
    l =len(msg)
    screen_text= font.render(msg, True, color)
    gameDisplay.blit(screen_text, [(display_width/2)- l*10/2, 100])
"""

def gameLoop():
    global direction
    
    gameExit =False
    gameOver= False
    
    move_x= display_width/2
    move_y= display_height/2

    move_x_change= 0
    move_y_change= 0
    snakelist= []
    snakelen= 1
    
    randApplex, randAppley= randApple()
    
    
    while not gameExit:
        
        
        while gameOver== True:
            gameDisplay.fill(black)
            message_to_screen("Game Over"
                              , red
                              , -50
                              , size= "End")
            message_to_screen("Press C to play again or Q to quit!",red, 50, size= "medium")
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type ==pygame.QUIT:
                    gameOver= False
                    gameExit= True
                
                if event.type==pygame.KEYDOWN:
                    if event.key== pygame.K_q:
                        gameExit= True
                        gameOver = False
                    if event.key== pygame.K_c:
                        gameLoop()
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                gameExit= True
                
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_LEFT:
                    direction= "left"
                    move_x_change= -block_size
                    move_y_change= 0
                elif event.key== pygame.K_RIGHT:
                    direction= "right"
                    move_x_change= block_size
                    move_y_change= 0
                elif event.key== pygame.K_UP:
                    direction ="up"
                    move_y_change= -block_size
                    move_x_change= 0
                elif event.key== pygame.K_DOWN:
                    direction= "down"
                    move_y_change= block_size
                    move_x_change= 0
                elif event.key ==pygame.K_p:
                    pause()
                    
            
            """
            if event.type== pygame.KEYUP:
                if event.key== pygame.K_LEFT or event.key== pygame.K_RIGHT:
                    move_x_change= 0
                
                if event.key== pygame.K_UP or event.key== pygame.K_DOWN:
                    move_y_change= 0
            
            
            """
        if move_x>=display_width or move_x<=0 or move_y>=display_height or move_y<=0:
            gameOver= True 
        
                    
        move_x += move_x_change  
        move_y += move_y_change    
        
        #welcome_message("Welcome to the snack game", green)
        gameDisplay.fill(light_yellow)
        
        
        
        Apple_thick= 30;
        #pygame.draw.rect(gameDisplay, red, [randApplex, randAppley, Apple_thick, Apple_thick])
        gameDisplay.blit(apple_img, (randApplex, randAppley))
        
        snakeHead= []
        snakeHead.append(move_x)
        snakeHead.append(move_y)
        snakelist.append(snakeHead)
        
        if len(snakelist)>snakelen:
            del(snakelist[0])
            
            
        for each in snakelist[:-1]:
            if each== snakeHead:
                gameOver= True
        
        snake(block_size, snakelist)
        
        score(snakelen-1)
        
        pygame.display.update()
        
        
        
        if move_x > randApplex and move_x <randApplex+ Apple_thick or move_x+block_size >randApplex and move_x +block_size < randApplex+Apple_thick:
            if move_y> randAppley and move_y< randAppley+ Apple_thick:
                randApplex, randAppley= randApple()
                snakelen+=1
                
            elif move_y +block_size >randAppley and move_y+block_size <randAppley +Apple_thick:
                randApplex, randAppley= randApple()
                snakelen+=1  
                
        
        
        clock.tick(FPS)
            
    gameDisplay.fill(black)      
    message_to_screen("Good Bye", red, size= "large")
    pygame.display.update()
    time.sleep(1)
    pygame.quit()
    quit()
    
intro()  
gameLoop()
    
    
