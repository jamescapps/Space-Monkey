import pygame
from resuable_functions import update_and_flip, dialogue, good_luck
from chapter2 import dream
from chapter2.Choices import pre_dream_choices_2


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
        dialogue(' (1) I was just hoping we could chat. ', 243, 600, 15)
        dialogue(' (2) Nothing.. I am ready...          ', 243, 625, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) I was just hoping we could chat. ', 243, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function
                    pre_dream_choices_2.have_a_chat()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Nothing.. I am ready...          ', 243, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    good_luck()
                    # Run function to start the dream.
                    dream.dream()


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
        dialogue(' (1) Say something nice. ', 243, 600, 15)
        dialogue(' (2) Say something mean. ', 243, 625, 15)

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
                    # something_nice()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Say something mean. ', 243, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run next function
                    # something_mean()
