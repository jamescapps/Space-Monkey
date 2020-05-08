import turtle
import time
from chapter2.levels import level_one, level_three


stop = False


def scene_1():

    # Set up the screen
    wn = turtle.Screen()
    wn.reset()
    wn.bgcolor('black')
    wn.title('T h e  D r e a m')
    wn.bgpic('img/dream/zeb.gif')

    # Register the image
    wn.register_shape('img/dream/level_one_monkey.gif')
    wn.register_shape('img/dream/surfboard.gif')

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
    wn.listen()
    wn.onkeypress(move_left, 'Left')
    wn.onkeypress(move_right, 'Right')

    # Main loop
    while True:
        player.showturtle()

        if player.xcor() == 2.5:
            while True:
                floating_words_pen.clear()
                floating_words_string = 'S t o p'
                floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))

                time.sleep(5)
                floating_words_pen.clear()
                floating_words_pen.setposition(10, 300)
                floating_words_string = 'W h o  a r e  y o u ?'
                floating_words_pen.write(floating_words_string, False, align='center', font=('Monospace', 20, 'normal'))

                time.sleep(5)
                floating_words_pen.clear()
                floating_words_string = 'S o m e t i m e s  y o u  k n o w'
                floating_words_pen.write(floating_words_string, False, align='center', font=('Monospace', 20, 'normal'))

                time.sleep(5)
                floating_words_pen.clear()
                floating_words_string = 'b u t  y o u  a l w a y s  d o.'
                floating_words_pen.write(floating_words_string, False, align='center', font=('Monospace', 20, 'normal'))

                time.sleep(5)
                floating_words_pen.clear()
                floating_words_pen.setposition(10, 300)
                floating_words_string = 'S o  t e l l  m e .'
                floating_words_pen.write(floating_words_string, False, align='center', font=('Monospace', 20, 'normal'))

                answer = wn.textinput('So tell me', 'Who are you?: ')

                if answer.lower() in ('mr. jones', 'the wolf', 'the girl', 'the deer', 'the moon'):
                    # Proceed to next section
                    level_three.main()
                else:
                    # Return to beginning
                    global stop
                    stop = False
                    level_one.game()
