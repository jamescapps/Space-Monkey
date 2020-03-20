import pygame
from resuable_functions import update_and_flip, dialogue
from asteroid_choices_5 import i_understand, strong_feelings


def convinced():
    # Commander
    dialogue('  You know... that\'s not a bad point....                 '
             , 510, 100, 15)
    dialogue('  Ok Space Monkey... You have permission to ignore the    '
             , 510, 150, 15)
    dialogue('  the Prime Directive.  Weapons free!                     '
             , 520, 200, 15)
    dialogue('  Now get in that asteroid field!                          '
             , 520, 250, 15)
    pygame.time.delay(1500)
    # Run function to start asteroid field with weapons.


def trash_response():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        dialogue('  You are a piece of trash Commander! It is no secret  '
                 , 250, 600, 15)
        dialogue('  I can not stand the site nor smell of your foul      '
                 , 250, 625, 15)
        dialogue('  existence. But I am here to do a mission.  Not       '
                 , 250, 650, 15)
        dialogue('  play nice with you! Now I am going to get through    '
                 , 250, 675, 15)
        dialogue('  that asteroid field while you sit in your cushy      '
                 , 250, 700, 15)
        dialogue('  leather chair smoking a cigar!       (enter)         '
                 , 250, 725, 15)
        pygame.time.delay(1500)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Commander
                dialogue('  Space Monkey you seem to forget that I am in command.   '
                         , 520, 100, 15)
                dialogue('  I have control of your weapons system and I will not    '
                         , 520, 125, 15)
                dialogue('  release them at this time.  If you die in the asteroid  '
                         , 520, 150, 15)
                dialogue('  field we will simply send another monkey out to do the  '
                         , 520, 175, 15)
                dialogue('  job. Never forget that I am in control and you are      '
                         , 520, 200, 15)
                dialogue(' expendable                 (enter)                       '
                         , 530, 225, 15)
                pygame.time.delay(1500)

                pygame.event.clear()
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Commander
                        dialogue('  Now get in that asteroid field and adhere to the prime  '
                                 , 520, 100, 15)
                        dialogue('  directive.           (enter)                            '
                                 , 520, 125, 15)
                        dialogue('                                                          '
                                 , 520, 150, 15)
                        dialogue('                                                          '
                                 , 520, 175, 15)
                        dialogue('                                                          '
                                 , 520, 200, 15)
                        dialogue('                                                          '
                                 , 530, 225, 15)
                        pygame.time.delay(1500)

                        """pygame.event.clear()
                        event = pygame.event.wait()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                # Run function to enter asteroid field without weapons."""


def war_profiteer():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        dialogue('  Commander I know your secret...                      '
                 , 250, 600, 15)
        dialogue('  You made a sizable fortune as a prominent share      '
                 , 250, 625, 15)
        dialogue('  holder in a company manufacturing arms during the    '
                 , 250, 650, 15)
        dialogue('  Terydian Revolution....                              '
                 , 250, 675, 15)
        dialogue('  So I am going into this asteroid field weapons free  '
                 , 250, 700, 15)
        dialogue('  or I am letting your secret be known.       (enter)  '
                 , 250, 725, 15)
        pygame.time.delay(1500)

        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Commander
                dialogue('  Space Monkey....                                        '
                         , 520, 100, 15)
                dialogue('  How did you find out...?                                '
                         , 520, 125, 15)
                dialogue('  Ok.  Weapons free.                                      '
                         , 520, 150, 15)
                dialogue('  We will talk more about this later...                   '
                         , 520, 175, 15)
                dialogue('                      (enter)                             '
                         , 520, 200, 15)
                dialogue('                                                          '
                         , 530, 225, 15)
                pygame.time.delay(1500)

                """pygame.event.clear()
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Run function to enter asteroid field with weapons."""


def liar():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        dialogue('  You are a liar!  You knew very well there were no    '
                 , 250, 600, 15)
        dialogue('  bananas in the capsule!!!!                           '
                 , 250, 625, 15)
        dialogue('                                                       '
                 , 250, 650, 15)
        dialogue('                                                       '
                 , 250, 675, 15)
        dialogue('                                                       '
                 , 250, 700, 15)
        dialogue('                                                       '
                 , 250, 725, 15)
        pygame.time.delay(3000)
        update_and_flip()

        dialogue('  Space Monkey....                                        '
                 , 520, 100, 15)
        dialogue('  Forget about the bananas for 5 seconds.                 '
                 , 520, 125, 15)
        dialogue('  You are obsessed with bananas!                          '
                 , 520, 150, 15)
        dialogue('  Complete this mission and you will have more bananas    '
                 , 520, 175, 15)
        dialogue('  than you can dream of!                                  '
                 , 520, 200, 15)
        dialogue('                                                          '
                 , 530, 225, 15)
        pygame.time.delay(3000)

        # Run function to enter asteroid field without weapons.


def responsible():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        dialogue('  We need to hold an inquiry and find out who is       '
                 , 250, 600, 15)
        dialogue('  responsible for this.  This injustice shall not      '
                 , 250, 625, 15)
        dialogue('  stand!!!!                                            '
                 , 250, 650, 15)
        dialogue('                                                       '
                 , 250, 675, 15)
        dialogue('                                                       '
                 , 250, 700, 15)
        dialogue('                                                       '
                 , 250, 725, 15)
        pygame.time.delay(3000)
        update_and_flip()

        # Commander
        dialogue('  Space Monkey....                                        '
                 , 520, 100, 15)
        dialogue('  Forget about the bananas for 5 seconds.                 '
                 , 520, 125, 15)
        dialogue('  Look if I let you use your weapons in the asteroid      '
                 , 520, 150, 15)
        dialogue('  field will you forget about the bananas?                '
                 , 520, 175, 15)
        dialogue('                                                          '
                 , 520, 200, 15)
        dialogue('                                                          '
                 , 530, 225, 15)
        pygame.time.delay(3000)

        while True:
            # Monkey
            update_and_flip()
            dialogue('  (1)  Yes                                             '
                     , 250, 600, 15)
            dialogue('  (2)  No                                              '
                     , 250, 625, 15)
            dialogue('                                                       '
                     , 250, 650, 15)
            dialogue('                                                       '
                     , 250, 675, 15)
            dialogue('                                                       '
                     , 250, 700, 15)
            dialogue('                                                       '
                     , 250, 725, 15)

            # Underline selection before running next function.
            event = pygame.event.wait()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    while True:
                        update_and_flip()
                        dialogue(' (1) Yes ', 50, 600, 15, underline=True)
                        pygame.display.flip()
                        pygame.time.delay(1500)
                        # Run function to enter asteroid field with weapons.

                if event.key == pygame.K_2:
                    while True:
                        update_and_flip()
                        dialogue(' (2) No ', 50, 625, 15, underline=True)
                        pygame.display.flip()
                        pygame.time.delay(1500)

                        # Commander
                        dialogue('  Space Monkey....                                        '
                                 , 520, 100, 15)
                        dialogue('  that is the best I can do right now.. .                 '
                                 , 520, 125, 15)
                        dialogue('                                                          '
                                 , 520, 150, 15)
                        dialogue('                                                          '
                                 , 520, 175, 15)
                        dialogue('                                                          '
                                 , 520, 200, 15)
                        dialogue('                                                          '
                                 , 530, 225, 15)
                        pygame.time.delay(3000)
                        # Run function to enter asteroid field with weapons.


def one_time_thing():
    # Have to start new loop to get rid of underline.
    while True:
        # Monkey
        dialogue('  Look... Commander....                                '
                 , 250, 600, 15)
        dialogue('  We both had a lot of fun, but you know we need to    '
                 , 250, 625, 15)
        dialogue('  keep this relationship professional right?           '
                 , 250, 650, 15)
        dialogue('                                                       '
                 , 250, 675, 15)
        dialogue('                                                       '
                 , 250, 700, 15)
        dialogue('                                                        '
                 , 250, 725, 15)
        pygame.time.delay(1500)

        # Commander
        update_and_flip()
        dialogue('  (1) Of course I understand.                             '
                 , 520, 100, 15)
        dialogue('  (2) But my feelings are strong...                       '
                 , 520, 125, 15)
        dialogue('                                                          '
                 , 520, 150, 15)
        dialogue('                                                          '
                 , 520, 175, 15)
        dialogue('                                                          '
                 , 520, 200, 15)
        dialogue('                                                          '
                 , 530, 225, 15)
        pygame.time.delay(1500)

        # Underline selection before running next function.
        pygame.event.clear()
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                while True:
                    update_and_flip()
                    dialogue('  (1) Of course I understand.                             '
                             , 520, 100, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    i_understand()

            if event.key == pygame.K_2:
                while True:
                    update_and_flip()
                    dialogue('  (2) But my feelings are strong...                       '
                             , 520, 125, 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    strong_feelings()


def dont_try_again():
    # Commander
    update_and_flip()
    dialogue('    Of course I understand.                               '
             , 520, 100, 15)
    dialogue('    My deepest apologies Space Monkey.                    '
             , 520, 125, 15)
    dialogue('    As a matter of fact, eh, forget about the Prime       '
             , 520, 150, 15)
    dialogue('    Directive. Go ahead and blast those asteroids!        '
             , 520, 175, 15)
    dialogue('                                                          '
             , 520, 200, 15)
    dialogue('                                                          '
             , 530, 225, 15)
    pygame.time.delay(3000)
    # Run function to start asteroid field with weapon.
