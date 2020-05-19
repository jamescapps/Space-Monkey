import pygame
from resources.resuable_functions import update_and_flip, dialogue, good_luck
from resources.chapter2 import dream
from resources.chapter2.Choices import pre_dream_choices_4


def hybernation_explanation():
    # Commander
    update_and_flip()
    dialogue(' Your body will be in suspension.       ', 490, 100, 15)
    dialogue(' However, your mind will be active.     ', 490, 150, 15)
    dialogue(' Essentially you will be having a       ', 490, 200, 15)
    dialogue(' 750 year long dream...                 ', 490, 250, 15)

    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) Will I perceive time?                    ', 243, 600, 15)
        dialogue(' (2) Are there any long-term effects?         ', 243, 625, 15)
        dialogue('(3) Well let\'s get to it!                   ', 243, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) Will I perceive time?                    ', 248, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_4.perceive_time()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Are there any long-term effects?         ', 248, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_4.long_term_effects()

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) Well let\'s get to it!                   ', 248, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    good_luck()
                    # Run function to enter dream
                    # Need a better transition into dream...
                    dream.dream()


def get_personal():
    while True:
        # Monkey
        update_and_flip()
        dialogue(' (1) Are you afraid to die?                    ', 243, 600, 15)
        dialogue(' (2) Will you miss me?                         ', 243, 625, 15)
        dialogue(' (3) Nothing.. I am ready...                   ', 243, 650, 15)

        # Underline selection before running next function.
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue(' (1) Are you afraid to die?                    ', 248, 600, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_4.afraid_to_die()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue(' (2) Will you miss me?                         ', 248, 625, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    pre_dream_choices_4.miss_me()

            if event.key == pygame.K_3:
                while True:
                    update_and_flip()
                    dialogue(' (3) Nothing.. I am ready...                   ', 248, 650, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    good_luck()
                    # Run function to enter dream
                    # Need a better transition into dream...
                    dream.dream()


def pleasure():
    while True:
        # Monkey
        update_and_flip()
        dialogue(' Sir, it has been an absolute pleasure           ', 235, 600, 15)
        dialogue(' to serve under you. I wish you all              ', 235, 625, 15)
        dialogue(' the best.                                       ', 235, 650, 15)

        # Maybe add something meaningful from the Commander.
        pygame.time.delay(3000)
        good_luck()
        # Run function to enter dream
        # Need a better transition into dream...
        dream.dream()


def miss_you():
    while True:
        # Monkey
        update_and_flip()
        dialogue(' Sir...                                  ', 243, 600, 15)
        dialogue(' I am... going to ...                    ', 243, 625, 15)
        dialogue(' miss you..                              ', 243, 650, 15)

        while True:
            # Commander
            update_and_flip()
            dialogue(' I appreciate that Space Monkey.         ', 490, 150, 15)
            dialogue(' The feeling is mutual.                  ', 490, 200, 15)
            dialogue(' Now get out there and complete your     ', 490, 250, 15)
            dialogue(' mission!                                ', 490, 300, 15)

            pygame.time.delay(3000)
            # Run function to enter dream
            # Need a better transition into dream...
            dream.dream()


def never_liked_you():
    while True:
        # Monkey
        update_and_flip()
        dialogue(' Commander I would just like to say that   ', 243, 600, 15)
        dialogue(' I have never liked you. You are a war     ', 243, 625, 15)
        dialogue(' pig who profits on the carnage of regime  ', 243, 650, 15)
        dialogue(' changes throughout this galaxy. I wish you', 243, 700, 15)
        dialogue(' a slow, painful death...       (enter)    ', 243, 750, 15)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:

                while True:
                    # Commander
                    update_and_flip()
                    dialogue(' Well I am on Earth living out my days   ', 490, 150, 15)
                    dialogue(' while you are in a capusle, asleep for  ', 490, 200, 15)
                    dialogue(' the next 750 years...  So good luck on  ', 490, 250, 15)
                    dialogue(' your mission!                           ', 490, 300, 15)

                    pygame.time.delay(3000)
                    # Run function to enter dream
                    # Need a better transition into dream...
                    dream.dream()


def not_miss_you():
    while True:
        # Monkey
        update_and_flip()
        dialogue('Commander I will not miss you. I have         ', 243, 600, 15)
        dialogue('tolerated you as a manor of professionalism   ', 243, 625, 15)
        dialogue('and I feel no emotion at the thought of       ', 243, 650, 15)
        dialogue('never seeing your face again.    (enter)      ', 243, 675, 15)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:

                while True:
                    # Commander
                    update_and_flip()
                    dialogue(' Uh.. Great good luck out there.         ', 490, 100, 15)
                    dialogue('                                         ', 490, 150, 15)
                    dialogue('                                         ', 490, 200, 15)
                    dialogue('                                         ', 490, 250, 15)

                    pygame.time.delay(3000)
                    # Run function to enter dream
                    # Need a better transition into dream...
                    dream.dream()
