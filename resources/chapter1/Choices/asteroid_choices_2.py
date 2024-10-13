import pygame
from resources.resuable_functions import update_and_flip, dialogue, good_luck
from resources.chapter1.Choices.asteroid_choices_3 import explain_logically, insult, press_him, talk_about_it
from resources.chapter1.asteroid_field import instructions

def whats_the_problem():
    dialogue('  Well......                                              ', 510, 100, 15)
    dialogue('  What is it.....?                                        ', 510, 150, 15)

def nonsense():
    update_and_flip()
    dialogue(' How dare you address a superior in that manner?!       ', 510, 100, 15)
    dialogue(' You are here to follow orders, not to give opinions!   ', 510, 150, 15)
    
    choices = [
        ('(1) Explain logically', explain_logically),
        ('(2) Insult', insult),
        ('(3) Forget it...', good_luck, instructions, False)
    ]

    handle_choices(choices)

def bananas():
    update_and_flip()
    dialogue(' I.. eh... er..  Sorry about that.  There must have been ', 510, 100, 15)
    dialogue(' an accounting error somewhere.....                     ', 510, 150, 15)

    choices = [
        ('(1) Press him', press_him),
        ('(2) Forget it...', good_luck, instructions, False)
    ]

    handle_choices(choices)

def the_party():
    update_and_flip()
    dialogue('   I.. eh... er..  I had a lot to drink that night...       ', 510, 150, 15)

    choices = [
        ('(1) Keep talking about it.', talk_about_it),
        ('(2) Forget it...', good_luck, instructions, False)
    ]

    handle_choices(choices)

def handle_choices(choices):
    """
    Handles rendering of dialogue choices and user input to execute corresponding actions.
    :param choices: List of tuples in the format (display_text, function_to_call, *args)
    """
    while True:
        update_and_flip()
        for idx, (text, *_) in enumerate(choices):
            dialogue(text, 246, 600 + (25 * idx), 15)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            for idx, (_, func, *args) in enumerate(choices):
                if event.key == pygame.K_1 + idx:
                    update_and_flip()
                    dialogue(choices[idx][0], 246, 600 + (25 * idx), 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    func(*args)

                    if func == good_luck:
                        pygame.time.delay(3000)
                        
                    return  # Exit once a choice is made
