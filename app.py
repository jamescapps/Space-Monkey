from resources import intro
from resources.chapter1 import pre_asteroid
from resources.chapter2 import pre_dream, dream
from resources.chapter2.levels import level_one, level_two, level_three, level_four, level_five


def run_intro_sequence():
    """Handles the introduction sequence of the game."""
    intro.title_screen()
    intro.shooting_star()
    intro.rocket_launch()
    intro.flying_through_space_1()
    intro.flying_through_space_2()


def run_chapter1_asteroid_field():
    """Handles the events in Chapter 1: The Asteroid Field."""
    pre_asteroid.commander_convo()
    pre_asteroid.monkey_convo()
    pre_asteroid.monkey_and_commander_convo()


def run_chapter2_dream():
    """Handles the events in Chapter 2: The Dream."""
    pre_dream.main()
    dream.dream()
    level_one.game()
    level_one.scene_4()
    level_two.scene_1()
    level_three.main()
    level_four.game()
    level_five.ending()


def main():
    """Main function that controls the game flow."""
    run_intro_sequence()
    run_chapter1_asteroid_field()

    # Uncomment to run Chapter 2
    # run_chapter2_dream()


if __name__ == "__main__":
    main()
