import pygame
import time
import random

pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0,0,255)
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game')

dis_width = 800
dis_height = 600

game_over = False
game_close = False
 
x1 = 400
y1 = 300

snake_block = 10

snake_speed = 30
 
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None,50)

def message(msg,color):
    mesg = font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width//16,dis_height//2])

def draw_my_snake(snake_block,snake_list):
    for x in  snake_list:
        pygame.draw.rect(dis,blue,[x[0],x[1],snake_block,snake_block])


def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width//2
    y1 = dis_height//2

    x1_change = 0
    y1_change = 0

    length_of_snake = 1

    snake_list = []

    food_x = round(random.randrange(0,dis_width-snake_block)//10)*10
    food_y = round(random.randrange(0,dis_height-snake_block)//10)*10


    while not game_over:

        while game_close == True:
            message("You lost!,press 'Q' to quit or 'C' to play again",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_over = False
                        game_loop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0
        if (x1 >= dis_width or x1 <0) or (y1 >= dis_height or y1 < 0):
            game_close = True
        
        x1 += x1_change
        y1 += y1_change
        
        dis.fill(black)
        pygame.draw.rect(dis,red,[food_x,food_y,10,10])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
                break

        draw_my_snake(snake_block,snake_list)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0,dis_width-snake_block)//10)*10
            food_y = round(random.randrange(0,dis_height-snake_block)//10)*10
            length_of_snake += 1

     
        pygame.display.update()
     
     
        clock.tick(20)


    pygame.quit()
    quit()
game_loop()