import pygame
from resuable_functions import update_and_flip, dialogue, good_luck
from chapter2 import dream


def have_a_chat():
    # Commander
    update_and_flip()
    dialogue(' What\'s on your mind?                  ', 490, 150, 15)
    dialogue('                                        ', 490, 200, 15)
    dialogue('                                        ', 490, 250, 15)
    dialogue('                                        ', 490, 300, 15)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) What should I expect during hibernation? ', 243, 600, 15)
        dialogue(' (2) Get personal                             ', 243, 625, 15)
        dialogue(' (3) Nothing.. I am ready... ', 246, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) What should I expect during hibernation? ', 243, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Get personal                             ', 243, 625, 15, underline=True)
                    pygame.display.flip()3
                    pygame.time.delay(1500)
                    # Run next function

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) Nothing.. I am ready...                  ', 243, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    good_luck()
                    # Run function to enter dream
                    # Need a better transition into dream...
                    dream.dream()


def something_nice():
    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) It has been a pleasure Commander.        ', 243, 600, 15)
        dialogue(' (2) I will miss you...                       ', 243, 625, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) It has been a pleasure Commander.        ', 243, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) I will miss you...                       ', 243, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function


def something_mean():
    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) I have never liked you.                  ', 243, 600, 15)
        dialogue(' (2) I will not miss you...                    ', 243, 625, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) I have never liked you.                  ', 243, 243, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) I will not miss you...                    ', 243, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function