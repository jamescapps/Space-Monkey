import pygame
import turtle
import time
from resources.resuable_functions import update_and_flip, dialogue
from resources.chapter1 import pre_asteroid


stop = False

# Setup
size = (800, 800)
screen = pygame.display.set_mode(size)
black = (0, 0, 0)

# Register images
brown_monkey = pygame.image.load('img/dream/brown_monkey.jpeg')
moon = pygame.image.load('img/dream/moon.jpeg')


def main():
    x = -200
    y = 0
    while x > -400:
        update_and_flip()
        screen.fill(black)
        screen.blit(brown_monkey, (-300, 0))
        pygame.time.delay(1500)
        update_and_flip()
        screen.fill(black)
        screen.blit(moon, (x, y))
        x -= 25
        y -= 25

    questions()


def questions():
    # Set up the screen
    new_win = turtle.Screen()
    new_win.reset()
    new_win.bgcolor('black')
    new_win.title('T h e  D r e a m')
    new_win.bgpic('img/dream/zeb.gif')

    # Register the image
    new_win.register_shape('img/dream/level_one_monkey.gif')
    new_win.register_shape('img/dream/surfboard.gif')

    # Create the player
    player = turtle.Turtle()
    player.shape('img/dream/level_one_monkey.gif')
    player.penup()
    player.speed(0)
    player.setposition(-400, -250)
    player.setheading(90)
    player_speed = 2.5

    # Create the surf board
    board = turtle.Turtle()
    board.shape('img/dream/surfboard.gif')
    board.penup()
    board.speed(0)
    board.setposition(-400, -320)
    board.setheading(90)
    board_speed = 2.5

    # Floating words
    floating_words_pen = turtle.Turtle()
    floating_words_pen.speed(0)
    floating_words_pen.color('white')
    floating_words_pen.penup()
    floating_words_pen.setposition(-50, 300)

    floating_words_string = ''
    floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))
    floating_words_pen.hideturtle()

    # Functions
    def move_left():
        x = player.xcor()
        x -= player_speed
        player.setx(x)

        x = board.xcor()
        x -= board_speed
        board.setx(x)

    def move_right():
        global stop
        if not stop:
            x = player.xcor()
            x += player_speed
            player.setx(x)

            x = board.xcor()
            x += board_speed
            board.setx(x)

        if player.xcor() == 2.5:
            stop = True

    # Key binding
    new_win.listen()
    new_win.onkeypress(move_left, 'Left')
    new_win.onkeypress(move_right, 'Right')

    # Main loop
    while True:
        player.showturtle()

        if player.xcor() == 2.5:
            while True:
                floating_words_pen.clear()
                floating_words_string = 'S t o p'
                floating_words_pen.write(floating_words_string, False, align='left',
                                         font=('Monospace', 20, 'normal'))

                time.sleep(5)
                floating_words_pen.clear()
                floating_words_pen.setposition(10, 300)
                floating_words_string = 'W h a t  i s  a b o v e  u p ?'
                floating_words_pen.write(floating_words_string, False, align='center',
                                         font=('Monospace', 20, 'normal'))

                answer = new_win.textinput('So tell me', 'What is above up?: ')

                if answer.lower() in ('above', 'below', 'around', 'between', 'among', 'up', 'donew_win', 'center', 'beyond'):
                    global stop
                    stop = False
                    new_win.clear()
                    question_two()

                else:
                    # Return to beginning
                    stop = False
                    questions()


def question_two():
    # Set up the screen
    new_win = turtle.Screen()
    new_win.reset()
    new_win.bgcolor('black')
    new_win.title('T h e  D r e a m')
    new_win.bgpic('img/dream/zeb.gif')

    # Register the image
    new_win.register_shape('img/dream/level_one_monkey.gif')
    new_win.register_shape('img/dream/surfboard.gif')

    # Create the player
    player = turtle.Turtle()
    player.shape('img/dream/level_one_monkey.gif')
    player.penup()
    player.speed(0)
    player.setposition(-400, -250)
    player.setheading(90)
    player_speed = 2.5

    # Create the surf board
    board = turtle.Turtle()
    board.shape('img/dream/surfboard.gif')
    board.penup()
    board.speed(0)
    board.setposition(-400, -320)
    board.setheading(90)
    board_speed = 2.5

    # Floating words
    floating_words_pen = turtle.Turtle()
    floating_words_pen.speed(0)
    floating_words_pen.color('white')
    floating_words_pen.penup()
    floating_words_pen.setposition(-50, 300)

    floating_words_string = ''
    floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))
    floating_words_pen.hideturtle()

    # Functions
    def move_left():
        x = player.xcor()
        x -= player_speed
        player.setx(x)

        x = board.xcor()
        x -= board_speed
        board.setx(x)

    def move_right():
        global stop
        if not stop:
            x = player.xcor()
            x += player_speed
            player.setx(x)

            x = board.xcor()
            x += board_speed
            board.setx(x)

        if player.xcor() == 2.5:
            stop = True

    # Key binding
    new_win.listen()
    new_win.onkeypress(move_left, 'Left')
    new_win.onkeypress(move_right, 'Right')

    # Main loop
    while True:
        player.showturtle()

        if player.xcor() == 2.5:
            while True:
                floating_words_pen.clear()
                floating_words_string = 'S t o p'
                floating_words_pen.write(floating_words_string, False, align='left',
                                         font=('Monospace', 20, 'normal'))

                time.sleep(5)
                floating_words_pen.clear()
                floating_words_pen.setposition(20, 300)
                floating_words_string = 'I f  y o u  s e e  t h e\nB u d d h a  o n  t h e  r o a d\nW h a t  m u s t ' \
                                        ' y o u  d o ? '
                floating_words_pen.write(floating_words_string, False, align='center',
                                         font=('Monospace', 20, 'normal'))

                time.sleep(5)
                answer = new_win.textinput('If you see the buddha on the road', 'What must you do?: ')

                if answer.lower() in ('kill', 'kill the buddha.', 'kill the buddha', 'kill him', 'kill him.'):
                    ending()
                    new_win.clear()

                else:
                    # Restart game
                    pre_asteroid.commander_convo()


def ending():
    print('The end')
    while True:
        update_and_flip()
        dialogue('    T h e  E n d            ', 475, 100, 30)
        dialogue('Unfortunately, life support ', 415, 150, 15)        
        dialogue('failed during hibernation...', 413, 200, 15)
        dialogue('Thank you for playing!      ', 445, 250, 20)
        dialogue('By James Capps              ', 460, 350, 15)
        dialogue('(enter to exit)             ', 475, 500, 20)
        event = pygame.event.wait()
        if event.type == pygame.KEYDOnew_win:
            if event.key == pygame.K_RETURN:
                pygame.display.quit()
                pygame.quit()
