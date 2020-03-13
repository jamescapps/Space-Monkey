import pygame
from resuable_functions import update_and_flip, dialogue, good_luck
from asteroid_choices_3 import explain_logically, insult, press_him, talk_about_it


def whats_the_problem():
    dialogue('  Well......                                              '
             , 510, 100, 15)
    dialogue('  What is it.....?                                        '
             , 510, 150, 15)
    dialogue('                                                          '
             , 520, 200, 15)
    dialogue('                                                          '
             , 520, 250, 15)


def nonsense():
    # Commander
    update_and_flip()
    dialogue(' How dare you address a superior in that manner?!       '
             , 510, 100, 15)
    dialogue(' You are here to follow orders, not to give opinions!   '
             , 510, 150, 15)
    dialogue('                                                        '
             , 510, 200, 15)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) Explain logically                                  ', 246, 600, 15)
        dialogue(' (2) Insult                                             ', 246, 625, 15)
        dialogue(' (3) Forget it...                                       ', 246, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) Explain logically                                  ', 246, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    explain_logically()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Insult                                             ', 246, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    insult()

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) Forget it...                                       ', 246, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    good_luck()


def bananas():
    # Commander
    update_and_flip()
    dialogue(' I.. eh... er..  Sorry about that.  There must have been '
             , 510, 100, 15)
    dialogue(' an accounting error somewhere.....                     '
             , 510, 150, 15)
    dialogue('                                                        '
             , 510, 200, 15)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) Press him                                          ', 246, 600, 15)
        dialogue(' (2) Forget it...                                       ', 246, 625, 15)
        dialogue('                                                        ', 246, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) Press him                                          ', 246, 600, 15,
                             underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    press_him()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Forget it...                                       ', 246, 625, 15,
                             underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    good_luck()


def the_party():
    # Commander
    update_and_flip()
    dialogue('                                                            '
             , 510, 100, 15)
    dialogue('   I.. eh... er..  I had a lot to drink that night...       '
             , 510, 150, 15)
    dialogue('                                                            '
             , 525, 200, 15)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) Keep talking about it.                             ', 246, 600, 15)
        dialogue(' (2) Forget it...                                       ', 246, 625, 15)
        dialogue('                                                        ', 246, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) Keep talking about it.                             ', 246, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    talk_about_it()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Forget it...                                       ', 246, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    good_luck()
