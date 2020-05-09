import turtle
from resources.chapter2.levels import level_two


def game():
    # Set up the screen
    wn = turtle.Screen()
    wn.reset()
    wn.bgcolor('black')
    wn.title('T h e  D r e a m')
    wn.bgpic('img/dream/level_dream_background_1.gif')

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

    # 'O' in howl
    o_string = 'o'

    o_1_pen = turtle.Turtle()
    o_1_pen.speed(0)
    o_1_pen.color('white')
    o_1_pen.penup()
    o_1_pen.setposition(50, -165)
    o_1_pen.write(o_string, False, align='left', font=('Monospace', 20, 'normal'))
    o_1_pen.hideturtle()

    o_2_pen = turtle.Turtle()
    o_2_pen.speed(0)
    o_2_pen.color('white')
    o_2_pen.penup()
    o_2_pen.setposition(70, -145)
    o_2_pen.write(o_string, False, align='left', font=('Monospace', 20, 'normal'))
    o_2_pen.hideturtle()

    o_3_pen = turtle.Turtle()
    o_3_pen.speed(0)
    o_3_pen.color('white')
    o_3_pen.penup()
    o_3_pen.setposition(90, -125)
    o_3_pen.write(o_string, False, align='left', font=('Monospace', 20, 'normal'))
    o_3_pen.hideturtle()

    # 'w' in howl
    w_string = 'w'

    w_1_pen = turtle.Turtle()
    w_1_pen.speed(0)
    w_1_pen.color('white')
    w_1_pen.penup()
    w_1_pen.setposition(110, -105)
    w_1_pen.write(w_string, False, align='left', font=('Monospace', 20, 'normal'))
    w_1_pen.hideturtle()

    w_2_pen = turtle.Turtle()
    w_2_pen.speed(0)
    w_2_pen.color('white')
    w_2_pen.penup()
    w_2_pen.setposition(130, -85)
    w_2_pen.write(w_string, False, align='left', font=('Monospace', 20, 'normal'))
    w_2_pen.hideturtle()

    o_4_pen = turtle.Turtle()
    o_4_pen.speed(0)
    o_4_pen.color('white')
    o_4_pen.penup()
    o_4_pen.setposition(150, -65)
    o_4_pen.write(o_string, False, align='left', font=('Monospace', 20, 'normal'))
    o_4_pen.hideturtle()

    o_5_pen = turtle.Turtle()
    o_5_pen.speed(0)
    o_5_pen.color('white')
    o_5_pen.penup()
    o_5_pen.setposition(170, -45)
    o_5_pen.write(o_string, False, align='left', font=('Monospace', 20, 'normal'))
    o_5_pen.hideturtle()

    o_6_pen = turtle.Turtle()
    o_6_pen.speed(0)
    o_6_pen.color('white')
    o_6_pen.penup()
    o_6_pen.setposition(190, -25)
    o_6_pen.write(o_string, False, align='left', font=('Monospace', 20, 'normal'))
    o_6_pen.hideturtle()

    # '!' in howl
    excl_string = '!'

    excl_pen = turtle.Turtle()
    excl_pen.speed(0)
    excl_pen.color('white')
    excl_pen.penup()
    excl_pen.setposition(210, -5)
    excl_pen.write(excl_string, False, align='left', font=('Monospace', 20, 'normal'))
    excl_pen.hideturtle()

    # Functions
    def move_left():
        x = player.xcor()
        x -= player_speed
        player.setx(x)

        x = board.xcor()
        x -= board_speed
        board.setx(x)

    def move_right():
        x = player.xcor()
        x += player_speed
        player.setx(x)

        x = board.xcor()
        x += board_speed
        board.setx(x)

    # Key binding
    wn.listen()
    wn.onkeypress(move_left, 'Left')
    wn.onkeypress(move_right, 'Right')

    # Main loop
    while True:
        player.showturtle()

        if player.xcor() > 515:
            scene_2()


def scene_2():
    # Set up the screen
    wn = turtle.Screen()
    wn.reset()
    wn.bgcolor('black')
    wn.title('T h e  D r e a m')
    wn.bgpic('img/dream/level_drem_background_2.gif')

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

    # Functions
    def move_left():
        x = player.xcor()
        x -= player_speed
        player.setx(x)

        x = board.xcor()
        x -= board_speed
        board.setx(x)

    def move_right():
        x = player.xcor()
        x += player_speed
        player.setx(x)

        x = board.xcor()
        x += board_speed
        board.setx(x)

    # Key binding
    wn.listen()
    wn.onkeypress(move_left, 'Left')
    wn.onkeypress(move_right, 'Right')

    # Main loop
    while True:
        player.showturtle()

        if player.xcor() > 515:
            scene_3()


def scene_3():
    # Set up the screen
    wn = turtle.Screen()
    wn.reset()
    wn.bgcolor('black')
    wn.title('T h e  D r e a m')
    wn.bgpic('img/dream/dream_level_background_3.gif')

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

    # Functions
    def move_left():
        x = player.xcor()
        x -= player_speed
        player.setx(x)

        x = board.xcor()
        x -= board_speed
        board.setx(x)

    def move_right():
        x = player.xcor()
        x += player_speed
        player.setx(x)

        x = board.xcor()
        x += board_speed
        board.setx(x)

    # Key binding
    wn.listen()
    wn.onkeypress(move_left, 'Left')
    wn.onkeypress(move_right, 'Right')

    # Main loop
    while True:
        player.showturtle()

        if player.xcor() > 515:
            scene_4()


def scene_4():
    # Set up the screen
    wn = turtle.Screen()
    wn.reset()
    wn.bgcolor('black')
    wn.title('T h e  D r e a m')
    wn.bgpic('img/dream/dream_scene_4.gif')

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
    floating_words_pen.setposition(-400, 200)

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
        x = player.xcor()
        x += player_speed
        player.setx(x)

        x = board.xcor()
        x += board_speed
        board.setx(x)

    # Key binding
    wn.listen()
    wn.onkeypress(move_left, 'Left')
    wn.onkeypress(move_right, 'Right')

    # Main loop
    while True:
        player.showturtle()

        if -300 <= player.xcor() < 25:
            floating_words_pen.clear()
            floating_words_string = 'W h o  a r e  y o u ?'
            floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))

        if player.xcor() >= 25:
            floating_words_pen.clear()
            floating_words_string = 'M r .  J o n e s  n e v e r\nl e t s  u s  p l a y  i n\nh i s  t r e e  h o u ' \
                                    's e . '
            floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))

        if player.xcor() > 515:
            scene_5()


def scene_5():
    # Set up the screen
    wn = turtle.Screen()
    wn.reset()
    wn.bgcolor('black')
    wn.title('T h e  D r e a m')
    wn.bgpic('img/dream/dream8.gif')

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
    floating_words_pen.setposition(-400, 200)

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
        x = player.xcor()
        x += player_speed
        player.setx(x)

        x = board.xcor()
        x += board_speed
        board.setx(x)

    # Key binding
    wn.listen()
    wn.onkeypress(move_left, 'Left')
    wn.onkeypress(move_right, 'Right')

    # Main loop
    while True:
        player.showturtle()

        if -300 <= player.xcor() < 25:
            floating_words_pen.clear()
            floating_words_string = 's o m e t h i n g'
            floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))

        if player.xcor() >= 25:
            floating_words_pen.clear()
            floating_words_string = 'a n y t h i n g '
            floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))

        if player.xcor() > 515:
            level_two.scene_1()
