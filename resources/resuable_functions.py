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


def good_luck():
    dialogue('  Great! Get to it!                                       '
             , 510, 100, 15)
    dialogue('  Good luck out there Space Monkey!                       '
             , 510, 150, 15)
    dialogue('                                                          '
             , 520, 200, 15)
    dialogue('                                                          '
             , 520, 250, 15)
    pygame.time.delay(2000)


def convinced():
    dialogue('  Great! Get to it!                                       '
             , 510, 100, 15)
    dialogue('  Good luck out there Space Monkey!                       '
             , 510, 150, 15)
    dialogue('                                                          '
             , 520, 200, 15)
    dialogue('                                                          '
             , 520, 250, 15)
    pygame.time.delay(2000)