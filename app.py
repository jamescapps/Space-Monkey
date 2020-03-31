import intro
from chapter1 import pre_asteroid
from chapter2 import pre_dream, dream
from chapter2.levels import level_one, level_two


def main():
    # Title Screen and Intro
    intro.title_screen()
    intro.shooting_star()
    intro.rocket_launch()
    intro.flying_through_space_1()
    intro.flying_through_space_2()

    # Chapter 1- The Asteroid Field
    pre_asteroid.commander_convo()
    pre_asteroid.monkey_convo()
    pre_asteroid.monkey_and_commander_convo()
    # Asteroid field game is ran within these functions based on outcome of conversations.

    # Chapter 2- The Dream
    #pre_dream.main()
    #dream.dream()
    #level_one.game()
    #level_one.scene_4()
    #level_two.scene_1()

main()
