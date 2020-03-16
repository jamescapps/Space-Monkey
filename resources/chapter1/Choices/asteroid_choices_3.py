import pygame
from resuable_functions import update_and_flip, dialogue, good_luck
from asteroid_choices_4 import convinced, trash_response, war_profiteer, liar, responsible, one_time_thing


def explain_logically():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        update_and_flip()
        dialogue(' Look sir, I understand you are my superior...         ', 246, 600, 15)
        dialogue(' But the longer it takes me to get through this        ', 246, 625, 15)
        dialogue(' asteroid field, the longer it takes me to complete    ', 246, 650, 15)
        dialogue(' my mission....                                        ', 246, 675, 15)
        dialogue('                    (enter)                            ', 246, 700, 12)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            convinced()
            if event.key == pygame.K_1:
                convinced()

                
def insult():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) You are a piece of trash!                          ', 246, 600, 15)
        dialogue(' (2) You are a war profiteer!                           ', 246, 625, 15)
        dialogue(' (3) Forget it...                                       ', 246, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) You are a piece of trash!                          ', 246, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    trash_response()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) You are a war profiteer!                           ', 246, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    war_profiteer()

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) Forget it...                                       ', 246, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    good_luck()


def press_him():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) You are a liar!                                    ', 246, 600, 15)
        dialogue(' (2) I want to know who is responsible and what we are  ', 246, 625, 15)
        dialogue('     going to do about this!                            ', 246, 650, 15)
        dialogue('                                                        ', 246, 700, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) You are a liar!                                    ', 246, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    liar()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) I want to know who is responsible and what we are  ',  246, 625, 15, underline=True)
                    dialogue('     going to do about this!                            ', 246, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    responsible()


def talk_about_it():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) Tell him it was a one time thing.                  ', 246, 600, 15)
        dialogue(' (2) Tell him he better not try it again.               ', 246, 625, 15)
        dialogue(' (3) Forget it...                                       ', 246, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) Tell him it was a one time thing.                  ', 246, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    one_time_thing()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Tell him he better not try it again.               ', 246, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    # Run don't_try_again()

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) Forget it...                                       ', 246, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    good_luck()
                    # Run function to enter asteroid field without weapons.
