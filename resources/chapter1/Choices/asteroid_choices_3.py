import pygame
from resuable_functions import update_and_flip, dialogue, good_luck


def explain_logically():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        update_and_flip()
        dialogue(' Look sir, I understand you are my superior... but....    ', 246, 600, 15)
        dialogue(' The longer it takes me to get through this asteroid field', 246, 625, 15)
        dialogue(' The longer it takes me to complete my mission....        ', 246, 650, 15)
        pygame.time.delay(5000)
        # Run convinced function


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
                    pygame.time.delay(2000)
                    # Run trash_response function

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) You are a war profiteer!                           ', 246, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    # Run war_profiteer function

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) Forget it...                                       ', 246, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    good_luck()


def press_him():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) You are a liar!                                    ', 246, 600, 15)
        dialogue(' (2) I want to know who is responsible and what we are  ', 246, 625, 15)
        dialogue('     going to do about this!                            ', 246, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) You are a liar!                                    ', 246, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    # Run liar()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) I want to know who is responsible and what we are  ',  246, 625, 15, underline=True)
                    dialogue('     going to do about this!                            ', 246, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    # Run responsible()


def talk_about_it():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) Tell him it was a one time thing.                  ', 246, 600, 15)
        dialogue(' (2) Tell him not to be afraid what people will think.  ', 246, 625, 15)
        dialogue(' (3) Forget it...                                       ', 246, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) Tell him it was a one time thing.                  ', 246, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    # Run one_time_thing()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Tell him not to be afraid what people will think.  ', 246, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    # Run don't_be_afraid()

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) Forget it...                                       ', 246, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(2000)
                    good_luck()
