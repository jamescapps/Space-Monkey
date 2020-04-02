import turtle


def game():
    def scene_1():
        # Set up the screen
        wn = turtle.Screen()
        wn.reset()
        wn.bgcolor('black')
        wn.title('T h e  D r e a m')
        wn.bgpic('img/dream/dream11.gif')

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
        floating_words_pen.setposition(-50, 325)

        floating_words_string = 'I  w i s h  I  h a d  m o r e'
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

            if player.xcor() > 515:
                scene_2()

    def scene_2():
        # Set up the screen
        wn = turtle.Screen()
        wn.reset()
        wn.bgcolor('black')
        wn.title('T h e  D r e a m')
        wn.bgpic('img/dream/dream9.gif')

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
        floating_words_pen.color('black')
        floating_words_pen.penup()
        floating_words_pen.setposition(-350, 325)

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
                floating_words_string = 'And again And again And again'
                floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))

            if player.xcor() >= 25:
                floating_words_pen.clear()
                floating_words_string = 'And never'
                floating_words_pen.write(floating_words_string, False, align='left', font=('Monospace', 20, 'normal'))

            if player.xcor() > 515:
                scene_2()

    scene_1()