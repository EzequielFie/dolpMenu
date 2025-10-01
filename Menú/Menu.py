from time import sleep
import pygame, sys, os, random, math, time, threading
import pygame_menu
from pygame_menu import themes
 
pygame.init()
surface = pygame.display.set_mode((600, 500))

# Load background image
background_image = pygame.image.load('Menú/Imgs/bonk.png')
 
def set_difficulty(value, difficulty):
    print(value)
    print(difficulty)
 
def start_the_game():
    pass
 
def level_menu():
    mainmenu._open(level)

def show_image():
    image = pygame.image.load('Menú/Imgs/bonk.png')
    surface.blit(image, (0, 0))
    pygame.display.flip()
    sleep(2)
 
mainmenu = pygame_menu.Menu('Dolphinator 3000', 600, 500, theme=themes.THEME_ORANGE)
mainmenu.add.text_input('Name: ', default='username', maxchar=20)

click_sound = pygame.mixer.Sound('Menú/Sounds/click.wav') 
happy_sound = pygame.mixer.Sound('Menú/Sounds/bonk.mp3')
def play_click_sound():
    click_sound.play()
def play_happy_sound():
    happy_sound.play()

mainmenu.add.button('Play', lambda: [play_click_sound(), start_the_game()])
mainmenu.add.button('Levels', lambda: [play_click_sound(), level_menu()])
mainmenu.add.button("Music", lambda: [play_click_sound(), pygame.mixer.music.set_volume(0)])
mainmenu.add.button("FELICIDAD", lambda: [play_happy_sound(), show_image()])
mainmenu.add.button('Quit', lambda: [play_click_sound(), pygame.quit(), sys.exit()])

level = pygame_menu.Menu('Select a Difficulty', 600, 500, theme=themes.THEME_DARK)
level.add.selector('Difficulty :', [('Easy', 1), ('Hard', 2)], onchange=set_difficulty)
 
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()

    # Draw background image
    surface.blit(background_image, (0, 0))

    if mainmenu.is_enabled():
        mainmenu.update(events)
        mainmenu.draw(surface)

    pygame.display.update()