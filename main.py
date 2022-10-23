import random
import math
import pygame
from pygame.locals import(KEYDOWN,K_ESCAPE,QUIT)
from helpers import *
from fuzzy import Fuzzy
from ObjectGui import ModelObject


def main():
    
    # randomn seed
    random.seed(random_seed)
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_DIMENSION, SCREEN_DIMENSION])
    background = pygame.image.load("utils/cancha.png").convert()
    ball = ModelObject(sprite_path="utils/ball.png")
    ball.rotation = 0.0

    player = ModelObject(sprite_path="utils/messi.png")

    goal = pygame.Surface((GOAL_WIDTH, GOAL_HEIGHT))
    goal.fill(BLACK)

    message_font = pygame.font.Font('ItalianFootball.ttf', 30)
    over_text = message_font.render('GOOOOOL' + '\n '+ 'PRESS R TO RESET', False, WHITE)

    textRect = over_text.get_rect()
    textRect.center = (SCREEN_DIMENSION / 2, SCREEN_DIMENSION / 2 - 150)

    # game state
    game_running = True
    ball_shot = False
    robot_won = False

    force_goal =0
    while game_running:
        # quit event, click or key
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_running = False

        screen.blit(background, (0, 0))
        
        # fuzzy loop
        if not ball_shot:
            dist, angle = Fuzzy.loop(ball, player)
            
        # the player reaches the ball
        if not ball_shot and dist <= MIN_DIST_2_BALL:
            dist_font = pygame.font.SysFont(None, 30)
            dist_surf = dist_font.render('Robot reached the ball!', True, (BLACK))
            screen.blit(dist_surf, (5, 30))
            
            # direction to goal
            rnd_rot_dev = math.pi / 6.0 * random.random()
            if random.random() <= 0.5:
                rnd_rot_dev *= -1.0
            force_goal = (math.pi / 2.0 + rnd_rot_dev)
            ball.set_direction(rad=force_goal)
            ball.speed = SPEED
            ball_shot = True
        
        # ball bounces on wall
        if ball.position.x < 70 or ball.position.x > SCREEN_DIMENSION-70:
            ball.rotate(math.pi)
        if ball.position.y < 70 or ball.position.y > SCREEN_DIMENSION-70:
            ball.rotate(math.pi)
            
        # reduce ball speed and stop ball if necessary
        if ball_shot:
            ball.speed -= FRICTION
            ball.move(ball.speed)
            if ball.speed < 0.1:
                ball.speed = 0.0
                ball_shot = False
                
        # ball reaches goal
        # simple detection if its on the range
        if ball.position.y > GOAL_POSITION:
            if ball.position.x > (SCREEN_DIMENSION / 2 - GOAL_WIDTH / 2) and ball.position.x < ((SCREEN_DIMENSION / 2 - GOAL_WIDTH / 2) + GOAL_WIDTH):
                screen.blit(over_text, textRect)
                robot_won = True

        # draw game objects
        screen.blit(ball.surf, (ball.position.x, ball.position.y))
        screen.blit(player.surf, (player.position.x, player.position.y))
        screen.blit(goal, (SCREEN_DIMENSION / 2 - GOAL_WIDTH / 2, SCREEN_DIMENSION - GOAL_HEIGHT))
        
        # debug messages
        message_surf = message_font.render(f'Distance to ball: {dist:.{2}f}', True, (BLACK))
        screen.blit(message_surf, (25, 25))
        message_surf3 = message_font.render(f'Kicking force: {force_goal:.{2}f}', True, (BLACK))
        screen.blit(message_surf3, (25, 75))


        pygame.display.flip()

        while robot_won:
            # quit event, click or key
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_r:
                        main()
if __name__ == '__main__':
    main()