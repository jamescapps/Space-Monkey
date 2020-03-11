import pygame


pygame.init()

size = (800, 800)
white = (255, 255, 255)
blue = (0, 6, 40)
black = (0, 0, 0)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Space Monkey')

background_image = pygame.image.load('img/about_background.png').convert()
thumbs_up_monkey = pygame.image.load('img/thumbs_up_monkey.png').convert()

star = pygame.transform.rotate(pygame.image.load('img/working_star.png').convert(), 20)
stars = pygame.image.load('img/basic_star.png').convert()
planet = pygame.image.load('img/saturn.png').convert()

rocket = pygame.image.load('img/rocketship.png').convert()
small_rocket = pygame.image.load('img/small_rocket.png').convert()
side_small_rocket = pygame.transform.rotate(small_rocket, -90)

exhaust = pygame.image.load('img/exhaust.png').convert()
side_rocket = pygame.transform.rotate(rocket, -90)
side_exhaust = pygame.transform.rotate(exhaust, -90)

comms_photo = pygame.image.load('img/comms_photo.png').convert()
commander = pygame.image.load('img/commander.png').convert()


def intro():
    x = 820
    y = 150

    title_font = pygame.font.SysFont('monospace', 60)
    title_text = title_font.render('* Space Monkey! *', True, white, blue)
    title_text_rect = title_text.get_rect()
    title_text_rect.center = (x // 2, y // 2)

    command_font = pygame.font.SysFont('courier', 30)
    command_text = command_font.render('Press Enter To Start', True, white, blue)
    command_text_rect = command_text.get_rect()
    command_text_rect.center = (x // 2, y * 4)

    replace_command_text = command_font.render('                       ', True, white, blue)
    replace_command_text_rect = replace_command_text.get_rect()
    replace_command_text_rect.center = (x // 2, y * 4)

    while True:
        screen.fill(blue)
        screen.blit(title_text, title_text_rect)
        screen.blit(thumbs_up_monkey, [100, 100])
        screen.blit(command_text, command_text_rect)
        # Would like to make blinking more consistent.
        screen.blit(side_small_rocket, (150, 700))
        screen.blit(side_small_rocket, (350, 700))
        screen.blit(side_small_rocket, (550, 700))
        pygame.display.update()
        screen.blit(replace_command_text, replace_command_text_rect)
        pygame.display.update()
        pygame.display.flip()

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                break


def shooting_star():
    x = 0
    y = 500

    while x < 700 and y < 700:
        screen.blit(background_image, [0, 0])
        pygame.display.flip()
        x += .75
        y -= .75
        screen.blit(star, (x, y))
        pygame.display.update()
        pygame.display.flip()
        screen.fill(black)


def rocket_launch():
    x = 300
    y = 500
    exhaust_x = 355
    exhaust_y = 745

    while y > 0:
        screen.blit(background_image, [0, 0])
        x += 0
        y -= .5
        exhaust_x += 0
        exhaust_y -= .5
        screen.blit(rocket, (x, y))
        pygame.display.flip()
        # screen.blit(exhaust, (exhaust_x, exhaust_y))
        # Need better exhaust or smoke.
        pygame.display.update()
        pygame.display.flip()
        screen.fill(black)


def flying_through_space_1():
    x = 0
    y = 300
    exhaust_x = -360
    exhaust_y = 350

    while x < 700:
        screen.fill(black)
        screen.blit(stars, (100, 100))
        screen.blit(stars, (220, 520))
        screen.blit(stars, (347, 750))
        screen.blit(stars, (400, 120))
        screen.blit(stars, (500, 600))
        x += .25
        y -= 0
        exhaust_x += .25
        exhaust_y -= 0
        screen.blit(side_rocket, (x, y))
        pygame.display.flip()
        screen.blit(side_exhaust, (exhaust_x, exhaust_y))
        pygame.display.update()
        pygame.display.flip()
        screen.fill(black)


def flying_through_space_2():
    x = 0
    y = 300
    exhaust_x = -360
    exhaust_y = 350

    while x < 700:
        screen.fill(black)
        screen.blit(stars, (130, 110))
        screen.blit(stars, (200, 540))
        screen.blit(stars, (247, 650))
        screen.blit(stars, (400, 120))
        screen.blit(stars, (300, 600))
        screen.blit(planet, (500, -10))
        x += .25
        y -= 0
        exhaust_x += .25
        exhaust_y -= 0
        screen.blit(side_rocket, (x, y))
        pygame.display.flip()
        screen.blit(side_exhaust, (exhaust_x, exhaust_y))
        pygame.display.update()
        pygame.display.flip()
        screen.fill(black)


def pre_asteroids_commander():
    while True:
        screen.blit(commander, [300, 200])
        pygame.display.update()
        pygame.display.flip()

        font = pygame.font.SysFont('monospace', 20)
        text = font.render(' Space Monkey! Are you there?  Do you read me?... ', True, white, black)
        text_rect = text.get_rect()
        text_rect.center = (400, 500)
        screen.blit(text, text_rect)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.fill(black)
                break


def pre_asteroids_monkey():
    while True:
        pygame.display.update()
        pygame.display.flip()
        screen.blit(comms_photo, [300, 200])
        pygame.display.update()
        pygame.display.flip()

        font = pygame.font.SysFont('monospace', 20)
        text = font.render(' Loud and clear Commander! ', True, white, black)
        text_rect = text.get_rect()
        text_rect.center = (420, 500)
        screen.blit(text, text_rect)

        event = pygame.event.wait()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                screen.fill(black)
                break


def pre_asteroids_monkey_and_commander():
    while True:
        screen.blit(comms_photo, [500, 500])
        pygame.display.update()
        pygame.display.flip()
        screen.blit(commander, [50, 40])

        font = pygame.font.SysFont('monospace', 15)
        text = font.render(' You are approaching the asteroid belt?', True, white, black)
        text_rect = text.get_rect()
        text_rect.center = (500, 150)
        screen.blit(text, text_rect)
        pygame.display.update()

        font = pygame.font.SysFont('monospace', 15)
        text1 = font.render(' Do you remember the prime directive?', True, white, black)
        text_rect1 = text.get_rect()
        text_rect1.center = (500, 200)
        screen.blit(text1, text_rect1)
        pygame.display.update()
        break

    #  Need to have user answer display where space monkey's text is and update Commanders based on input.
    user_answer = input('You can respond however you like to the Commander...')

    if user_answer.lower() == 'no':
        print('The prime directive means you are not allowed to use your weapons on any of these asteroids.'
              'The Fleet will not be responsible for rogue shards destroying other planets!  Can you agree to this?')
    elif user_answer.lower() == 'yes':
        print('Good.  I always knew you were sharp.  Once you get through this asteroid belt I will be in touch '
              'with new instructions.')
    else:
        print('Look we should focus on the task at hand...')


def main():
    intro()
    shooting_star()
    rocket_launch()
    flying_through_space_1()
    flying_through_space_2()
    pre_asteroids_commander()
    pre_asteroids_monkey()
    pre_asteroids_monkey_and_commander()


main()
