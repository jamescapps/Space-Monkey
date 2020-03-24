import pygame
from resuable_functions import update_and_flip, dialogue


def say_no():
    # Commander
    update_and_flip()
    dialogue(' Well...                                ', 490, 150, 15)
    dialogue(' What is it....                         ', 490, 200, 15)
    dialogue('                                        ', 490, 250, 15)
    dialogue('                                        ', 490, 300, 15)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) You are kind of a dick. ', 243, 600, 15)
        dialogue(' (2) Nothing.. I am ready... ', 246, 625, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) You are kind of a dick. ', 248, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Nothing.. I am ready... ', 242, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function


def say_yes():
    # Commander
    update_and_flip()
    dialogue(' Great.  You will be asleep for 750 years.  This may '
             , 510, 100, 15)
    dialogue(' be the last time we speak.  I will most likely be   '
             , 510, 150, 15)
    dialogue(' long since dead when you awake.                     '
             , 510, 200, 15)
    dialogue('                                        ', 490, 250, 15)
    dialogue('                                        ', 490, 300, 15)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) Say something nice... ', 243, 600, 15)
        dialogue(' (2) Say something mean... ', 243, 625, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) Say something nice, ', 243, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Say something mean. ', 243, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function
