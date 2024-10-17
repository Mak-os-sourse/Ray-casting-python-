import pygame

class Map():
    def __init__(self):
        self.rect_list = []
        
    def render_map(self, win):
        #80x80
        self.rect_list = []
        self.map = ["###############",
                    "#             #",
                    "#  ####       #",
                    "#             #",
                    "#      ###### #",
                    "#             #",
                    "#           # #",
                    "#   ##        #",
                    "#         #####",
                    "#             #",
                    "###############",]
        self.x_cell = 80
        self.y_cell = 80
        for y, i in enumerate(self.map):
            for x, j in enumerate(list(str(i))): 
                if j == '#':
                    self.rect = (self.x_cell * x, self.y_cell * y)
                    self.rect_list.append(self.rect)
                    # pygame.draw.rect(win, (65, 65, 65), (self.x_cell * x, self.y_cell * y, self.x_cell, self.y_cell))