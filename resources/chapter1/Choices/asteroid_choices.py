import pygame
from resuable_functions import update_and_flip, dialogue
from asteroid_choices_2 import good_luck, whats_the_problem


def say_no_1():
    # Commander
    update_and_flip()
    dialogue(' The Prime Directive states that you are not allowed'
             , 510, 100, 15)
    dialogue('to shoot an asteroid. The resulting debris may have'
             , 510, 150, 15)
    dialogue('negative consequences for other civilizations.     '
             , 510, 200, 15)
    dialogue(' Are you ready to enter the asteroid field?          '
             , 510, 250, 15)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) No  ', 243, 600, 15)
        dialogue(' (2) Yes ', 243, 625, 15)
        dialogue('                          ', 243, 650, 15)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) No ', 248, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    whats_the_problem()
                    say_more_choices_1()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Yes ', 242, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)

                    # Commander
                    update_and_flip()
                    good_luck()
                    # Run function to start to enter asteroid field.


def say_yes_1():
    # Commander
    update_and_flip()
    dialogue(' You are one sharp monkey. That is why we selected '
             , 510, 100, 15)
    dialogue(' you for this mission. Are you ready to enter the   '
             , 510, 150, 15)
    dialogue(' asteroid field?                                    '
             , 510, 200, 15)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) No ', 243, 600, 15)
        dialogue(' (2) Yes ', 246, 625, 15)
        dialogue('                   ', 286, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) No ', 248, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    whats_the_problem()
                    say_more_choices_1()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Yes ', 242, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    good_luck()
                    # Run function to start asteroid field.


def say_more_choices_1():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) The Prime Directive is nonsense.                   ', 246, 600, 15)
        dialogue(' (2) You lied about there being bananas in the capsule! ', 246, 625, 15)
        dialogue(' (3) We should talk about what happened at the party... ', 246, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) The Prime Directive is nonsense.                   ', 246, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) You lied about there being bananas in the capsule! ', 246, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) We should talk about what happened at the party... ', 246, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)