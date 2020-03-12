import pygame
from resuable_functions import dialogue


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


def whats_the_problem():
    dialogue('  Well......                                              '
             , 510, 100, 15)
    dialogue('  What is it.....?                                        '
             , 510, 150, 15)
    dialogue('                                                          '
             , 520, 200, 15)
    dialogue('                                                          '
             , 520, 250, 15)
