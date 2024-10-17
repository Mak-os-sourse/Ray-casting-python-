import pygame 
from player import Plaer 
from map_game import *
from settings import *

def run_game():
    settings = Settings()
    pygame.init()
    pygame.font.init()
    win = pygame.display.set_mode((settings.win_height, settings.win_width), pygame.RESIZABLE)
    pygame.display.set_caption("Ray casting")
    
    FPS = pygame.time.Clock()
    plaer = Plaer(settings)
    map_game = Map()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.QUIT()
            if event.type == pygame.VIDEORESIZE:
                x, y = win.get_size()
                settings.win_height = x
                settings.win_width = y
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    plaer.y_sin_speed = 10
                    plaer.x_cos_speed = 10
                if event.key == pygame.K_s:
                    plaer.y_sin_speed = -10
                    plaer.x_cos_speed = -10
                if event.key == pygame.K_a:
                    plaer.y_cos_speed = 10
                    plaer.x_sin_speed = -10
                if event.key == pygame.K_d:
                    plaer.y_cos_speed = -10
                    plaer.x_sin_speed = 10
                if event.key == pygame.K_RIGHT:
                    plaer.angle_speed_left = 0.02
                if event.key == pygame.K_LEFT:
                    plaer.angle_speed_right = 0.02
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    plaer.y_sin_speed = 0
                    plaer.x_cos_speed = 0
                if event.key == pygame.K_s:
                    plaer.y_sin_speed = 0
                    plaer.x_cos_speed = 0
                if event.key == pygame.K_a:
                    plaer.x_sin_speed = 0
                    plaer.y_cos_speed = 0
                if event.key == pygame.K_d:
                    plaer.x_sin_speed = 0
                    plaer.y_cos_speed = 0
                if event.key == pygame.K_RIGHT:
                    plaer.angle_speed_left = 0
                if event.key == pygame.K_LEFT:
                    plaer.angle_speed_right = 0
        
        win.fill((230, 230, 230))
        pygame.draw.rect(win, (66, 170, 255), (0, 0, settings.win_height, settings.win_width//2))
        pygame.draw.rect(win, (180,165,165), (0, settings.win_width//2, settings.win_height, settings.win_width//2))
        map_game.render_map(win)
        plaer.blit(win, map_game, settings)
        font = pygame.font.SysFont('Robot', 30)
        text_fps = font.render(str(int(FPS.get_fps())) + " FPS", True, (200, 100, 70))
        text_move = font.render("W,S,A,D: передвижение", True, (200, 100, 70))
        text_camer = font.render("<-, ->: передвижение камеры", True, (200, 100, 70))
        win.blit(text_fps, (10,10))
        win.blit(text_move, (10,settings.win_width - 45))
        win.blit(text_camer, (10,settings.win_width - 25))
        plaer.move()
        
        pygame.display.flip()
        FPS.tick()
               
run_game()


