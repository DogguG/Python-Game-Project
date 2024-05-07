import pygame, sys
from settings import *
from level import Level
from button import Button
from player import Player
class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# sound 
		main_sound = pygame.mixer.Sound('audio/main.ogg')
		main_sound.set_volume(0.1)
		main_sound.play(loops = -1)
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
while False:
        game_over()
    
            
if __name__ == 'play':
	game = Game()
	game.run()

if __name__ == 'restart':
    game = Game()
    game.run()
class MainMenu:
	pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Zelda")

BG = pygame.image.load("graphics/mainmenu/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("graphics/mainmenu/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("Coming Soon!", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Zelda", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("graphics/mainmenu/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("graphics/mainmenu/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("graphics/mainmenu/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game = Game()  # Create an instance of the Game class
                    game.run()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()

class GameOver:
    pygame.init()
    SCREEN = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Game Over")

    GO = pygame.image.load("graphics/mainmenu/Background.png")
    
def restart():
        while True:
            RESTART_MOUSE_POS = pygame.mouse.get_pos()
            RESTART_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")
            RESTART_BACK.changeColor(RESTART_MOUSE_POS)
            RESTART_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RESTART_BACK.checkForInput(RESTART_MOUSE_POS):
                        Game.run()

            pygame.display.update()
        
def game_over():
    while True:
        SCREEN.blit(GO, (0, 0))

        GAMEOVERMENU_MOUSE_POS = pygame.mouse.get_pos()
        GAMEOVERMENU_TEXT = get_font(100).render("Game Over", True, "#b68f40")
        GAMEOVERMENU_RECT = GAMEOVERMENU_TEXT.get_rect(center=(640, 100))
        RESTART_BUTTON = Button(image=pygame.image.load("graphics/mainmenu/Play Rect.png"), pos=(640, 250), 
                            text_input="Play Again", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("graphics/mainmenu/Quit Rect.png"), pos=(640, 550), 
                            text_input="Give Up", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(GAMEOVERMENU_TEXT, GAMEOVERMENU_RECT)

        for button in [RESTART_BUTTON, QUIT_BUTTON]:
            button.changeColor(GAMEOVERMENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RESTART_BUTTON.checkForInput(GAMEOVERMENU_MOUSE_POS):
                    game = Game()  # Create an instance of the Game class
                    game.run()

                if QUIT_BUTTON.checkForInput(GAMEOVERMENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
game_over() 
            

