from helpers import *
import math


actions = [
    # first position is movement and second rotation
    [1, 0], [1, math.pi / 6.0], [1, math.pi / 3.0], #slow
    [5, 0], [5, math.pi / 6.0], [5, math.pi / 3.0], # normal
    [10, 0], [10, math.pi / 6.0], [10, math.pi / 3.0] # fast
]
class Fuzzy():
    # Membership functions for distance
    def distance_close(x):
        if x <= 2:
            return 1.0
        elif x > SCREEN_DIMENSION/2.0:
            return 0.0
        return -0.099 * x + 1.23
    
    def distance_medium(x):
        if x <= SCREEN_DIMENSION/2.0:
            return 0.141421512474792 * x
        return -0.014 * x + 1.99999858578688
    
    def distance_far(x):
        if x <= SCREEN_DIMENSION/2.0:
            return 0.0
        elif x > SCREEN_DIMENSION:
            return 1.0
        return 0.8 * x - 2.4
    
    def angle_close(x):
        if x <= math.pi / 6.0:
            return 1.0
        elif x >= math.pi / 2.0:
            return 0.0
        return -0.96 * x + 1.56
    
    def angle_medium(x):
        if x <= math.pi / 2.0:
            return 0.636619772284456 * x
        return -0.12 * x + 2
    
    def angle_far(x):
        if x <= math.pi / 2.0:
            return 0.0
        elif x >= 3.0 * math.pi / 2.0:
            return 1.0
        return 0.4 * x - 0.2
    
    def loop(ball,player):
        # get the distance between  the player and the ball
        distance = player.position.distance(ball.position)
        direction_2_ball = player.position.direction_to(ball.position)
        angle = player.direction.angle(direction_2_ball)
        
        distance_f = [Fuzzy.distance_close(distance), Fuzzy.distance_medium(distance), Fuzzy.distance_far(distance)]
        rotation_f = [Fuzzy.angle_close(angle), Fuzzy.angle_medium(angle), Fuzzy.angle_far(angle)]
        
        # add min value to rules list
        rules = []
        for dist in distance_f:
            for rot in rotation_f:
                rules.append(min(dist, rot))
        
        max_value = -1
        index = 0     
        for i in range(len(rules)):
            if rules[i] > max_value:
                max_value = rules[i]
                index = i
        
        # get action      
        action = actions[index]
        player.rotate(rad=action[1], clockwise=(player.position.y >= ball.position.y))
        player.move(speed=action[0])
        return distance, angle
