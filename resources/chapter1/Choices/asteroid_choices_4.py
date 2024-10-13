import pygame
from resources.resuable_functions import update_and_flip, dialogue, good_luck
from resources.chapter1.asteroid_field import instructions

# Import your specific functions
from resources.chapter1.Choices.asteroid_choices_3 import explain_logically, insult, press_him, talk_about_it
from resources.chapter1.Choices.asteroid_responses import (
    trash_response, war_profiteer, liar, responsible, one_time_thing, dont_try_again, convinced
)

def display_dialogue_and_wait(options):
    """
    Displays dialogue options and waits for user input.
    :param options: A list of tuples in the format (text, function_to_call, *args)
    """
    if not options:
        raise ValueError("Options list cannot be empty")

    while True:
        update_and_flip()

        # Display options
        for idx, (text, _) in enumerate(options):
            dialogue(text, 246, 600 + (25 * idx), 15)

        # Wait for input and call the corresponding function
        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            for idx, (_, func, *args) in enumerate(options):
                if event.key == pygame.K_1 + idx:
                    # Underline selected option
                    dialogue(options[idx][0], 246, 600 + (25 * idx), 15, underline=True)
                    pygame.display.flip()
                    pygame.time.delay(1500)
                    func(*args)
                    return  # Exit after a choice is made

def explain_logically():
    options = [
        ("Look sir, I understand you are my superior...         ", convinced)
    ]
    display_dialogue_and_wait(options)

def insult():
    options = [
        ("(1) You are a piece of trash!                          ", trash_response),
        ("(2) You are a war profiteer!                           ", war_profiteer),
        ("(3) Forget it...                                       ", good_luck, instructions, False)
    ]
    display_dialogue_and_wait(options)

def press_him():
    options = [
        ("(1) You are a liar!                                    ", liar),
        ("(2) I want to know who is responsible and what we are  ", responsible)
    ]
    display_dialogue_and_wait(options)

def talk_about_it():
    options = [
        ("(1) Tell him it was a one-time thing.                  ", one_time_thing),
        ("(2) Tell him he better not try it again.               ", dont_try_again),
        ("(3) Forget it...                                       ", good_luck, instructions, False)
    ]
    display_dialogue_and_wait(options)
