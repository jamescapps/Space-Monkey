import pygame
from resources.resuable_functions import update_and_flip

pygame.init()

size = (800, 800)
white = (255, 255, 255)
blue = (0, 6, 40)
black = (0, 0, 0)

# Screen set up
screen = pygame.display.set_mode(size)
pygame.display.set_caption('S p a c e  M o n k e y')

# Register images
images = {
    'thumbs_up_monkey': pygame.image.load('img/thumbs_up_monkey.png').convert(),
    'background': pygame.image.load('img/about_background.png').convert(),
    'rocket': pygame.image.load('img/rocketship.png').convert(),
    'small_rocket': pygame.image.load('img/small_rocket.png').convert(),
    'exhaust': pygame.image.load('img/exhaust.png').convert(),
    'star': pygame.transform.rotate(pygame.image.load('img/working_star.png').convert(), 20),
    'stars': pygame.image.load('img/basic_star.png').convert(),
    'blue_star': pygame.image.load('img/blue_star.png').convert(),
    'planet': pygame.image.load('img/saturn.png').convert()
}

# Rotated images
images['side_small_rocket'] = pygame.transform.rotate(images['small_rocket'], -90)
images['side_rocket'] = pygame.transform.rotate(images['rocket'], -90)
images['side_exhaust'] = pygame.transform.rotate(images['exhaust'], -90)

# Utility Functions
def draw_stars():
    """Helper function to draw stars at predefined positions."""
    star_positions = [(100, 100), (220, 520), (347, 750), (400, 120), (500, 600)]
    for pos in star_positions:
        screen.blit(images['stars'], pos)


def rocket_movement(x, y, rocket_image, exhaust_image, exhaust_x, exhaust_y, increment):
    """Handles the movement of a rocket and its exhaust."""
    screen.fill(black)
    draw_stars()
    screen.blit(images['planet'], (500, -10))  # Include planet in space scenes
    x += increment
    exhaust_x += increment
    screen.blit(rocket_image, (x, y))
    screen.blit(exhaust_image, (exhaust_x, exhaust_y))
    update_and_flip()
    screen.fill(black)


# Functions for each section
def title_screen():
    x, y = 820, 150

    title_font = pygame.font.SysFont('monospace', 50)
    title_text = title_font.render('   S p a c e  M o n k e y   ', True, white, blue)
    command_font = pygame.font.SysFont('courier', 30)
    command_text = command_font.render('Press Enter To Start', True, white, blue)

    title_text_rect = title_text.get_rect(center=(x // 2, y // 2))
    command_text_rect = command_text.get_rect(center=(x // 2, y * 4))

    while True:
        screen.fill(blue)
        corners = [(1, 1), (1, 750), (750, 1), (750, 750)]
        for pos in corners:
            screen.blit(images['blue_star'], pos)

        screen.blit(title_text, title_text_rect)
        screen.blit(images['thumbs_up_monkey'], [100, 100])
        screen.blit(command_text, command_text_rect)
        screen.blit(images['side_small_rocket'], (150, 700))
        screen.blit(images['side_small_rocket'], (350, 700))
        screen.blit(images['side_small_rocket'], (550, 700))
        pygame.display.update()

        # Hit enter to continue to next screen.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            break


def shooting_star():
    x, y = 0, 500

    while x < 700 and y > 0:
        screen.blit(images['background'], [0, 0])
        screen.blit(images['star'], (x, y))
        pygame.display.flip()
        x += 0.75
        y -= 0.75
        update_and_flip()
        screen.fill(black)


def rocket_launch():
    x, y = 300, 500
    exhaust_x, exhaust_y = 355, 745

    while y > 0:
        screen.blit(images['background'], [0, 0])
        rocket_movement(x, y, images['rocket'], images['exhaust'], exhaust_x, exhaust_y, 0)
        y -= 0.5
        exhaust_y -= 0.5


def flying_through_space_1():
    x, y, exhaust_x, exhaust_y = 0, 300, -360, 350
    while x < 700:
        rocket_movement(x, y, images['side_rocket'], images['side_exhaust'], exhaust_x, exhaust_y, 0.25)


def flying_through_space_2():
    x, y, exhaust_x, exhaust_y = 0, 300, -360, 350
    while x < 700:
        rocket_movement(x, y, images['side_rocket'], images['side_exhaust'], exhaust_x, exhaust_y, 0.25)
