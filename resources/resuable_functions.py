import pygame


size = (800, 800)
screen = pygame.display.set_mode(size)
white = (255, 255, 255)
black = (0, 0, 0)


def update_and_flip():
    pygame.display.update()
    pygame.display.flip()


def dialogue(words, x, y, font_size, underline=False):
    font = pygame.font.SysFont('monospace', font_size)
    font.set_underline(underline)
    text = font.render(words, True, white, black)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    screen.blit(text, text_rect)
    pygame.display.update()
