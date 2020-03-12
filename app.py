import intro
from Chapter1 import pre_asteroid, interaction1


def main():
    # Title Screen and Intro
    intro.title_screen()
    intro.shooting_star()
    intro.rocket_launch()
    intro.flying_through_space_1()
    intro.flying_through_space_2()

    # Chapter 1
    pre_asteroid.commander_convo()
    pre_asteroid.monkey_convo()
    interaction1.monkey_and_commander_convo()


main()
