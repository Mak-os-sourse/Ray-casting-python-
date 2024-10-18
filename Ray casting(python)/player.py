import pygame
from math import *

class Plaer():
    def __init__(self, settings):
        self.plaer_x = 120
        self.plaer_y = 120
        self.x_cos_speed = 0
        self.y_sin_speed = 0
        self.x_sin_speed = 0
        self.y_cos_speed = 0
        self.angle = 0
        self.angle_speed_right = 0
        self.angle_speed_left = 0
        self.FOV = pi/6
        self.distance_cur = (pi/3)/settings.num_ray
    
    def move(self):
        self.plaer_x += (self.x_cos_speed) * cos(self.angle)
        self.plaer_y += (self.y_sin_speed) * sin(self.angle)
        self.plaer_x += (self.x_sin_speed) * sin(self.angle)
        self.plaer_y += (self.y_cos_speed) * cos(self.angle)
        self.angle += self.angle_speed_right
        self.angle -= self.angle_speed_left
        
    def intersection(self, x, y):
        # 80 == cellsize
        return ((x//80) * 80, (y//80) * 80)
 
    def blit(self, win, map_game, settings):
        # pygame.draw.circle(win, (100, 100, 100), (int(self.plaer_x), int(self.plaer_y)), 20)
        # line = pygame.draw.line(win, (85, 100, 89), (self.plaer_x, self.plaer_y), (self.plaer_x + 900 * cos(self.angle), self.plaer_y + 900 * sin(self.angle)))
        
        self.dist = settings.num_ray / (3 * tan(pi/6))
        self.coeff = 2 * self.dist * settings.cellsize
        self.scale = settings.win_height / settings.num_ray
        
        self.cur_angel = self.FOV + self.angle
        
        self.xs, self.ys = self.intersection(self.plaer_x, self.plaer_y)
        
        for ray in range(settings.num_ray):
            self.cos_a = cos(self.cur_angel)
            self.sin_a = sin(self.cur_angel) 
            if self.cos_a > 0:
                self.dx = 1
                self.px = self.xs + 80
            if self.cos_a < 0:
                self.dx = -1
                self.px = self.xs
            
            for i in range(0, settings.widht_ray, settings.cellsize):
                self.depth_v = (self.px - self.plaer_x) / self.cos_a
                self.y = self.plaer_y + self.depth_v * self.sin_a
                if self.intersection(self.px + self.dx, self.y) in map_game.rect_list:
                    break
                self.px += self.dx * settings.cellsize
            
            if self.sin_a > 0:
                self.dy = 1
                self.py = self.ys + 80
            if self.sin_a < 0:
                self.dy = -1
                self.py = self.ys
            
            for i in range(0, settings.widht_ray, settings.cellsize):
                self.depth_h = (self.py - self.plaer_y) / self.sin_a
                self.x = self.plaer_x + self.depth_h * self.cos_a
                if self.intersection(self.x, self.py + self.dy) in map_game.rect_list:
                    break
                self.py += self.dy * settings.cellsize 
            
            if self.depth_h > self.depth_v:
                self.depth = (self.depth_v) * cos(self.angle - self.cur_angel)
            if self.depth_h < self.depth_v:
                self.depth = (self.depth_h)  * cos(self.angle - self.cur_angel)

            self.proj = self.coeff / (self.depth + 1)
                
            self.color = 240 / (1 + self.depth * self.depth * 0.000002)
            # line = pygame.draw.line(win, (105, 100, 170), (self.plaer_x, self.plaer_y), (self.plaer_x + self.depth * self.cos_a, self.plaer_y + self.depth * self.sin_a))
            pygame.draw.rect(win, (self.color,self.color,self.color), (ray * self.scale, (settings.win_width // 2) - self.proj // 2, self.scale, self.proj))
            self.cur_angel -= self.distance_cur 