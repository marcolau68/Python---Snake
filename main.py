# Snake

import turtle
import random
import time
import tkinter.messagebox

mode = input('Easy, Normal, or Hard?')

if mode.lower() == 'easy':
    delay = 0.12
elif mode.lower() == 'normal':
    delay = 0.1
elif mode.lower() == 'hard':
    delay = 0.08

# Board
board = turtle.Screen()
board.title('Snake Game')
board.bgcolor('black')
board.setup(width=600, height=600)
board.tracer(0)

# Snake
snake = turtle.Turtle()
snake.color('white')
snake.shape('square')
snake.speed(0)
snake.penup()
snake.goto(0, 0)

# Food
food = turtle.Turtle()
food.color('red')
food.shape('circle')
food.penup()
food.speed(0)
food.goto(0, 100)


def up():
    snake.setheading(90)


def down():
    snake.setheading(270)


def left():
    snake.setheading(180)


def right():
    snake.setheading(0)


def move():
    snake.forward(20)


def snake_food_collide():
    distance1 = ((snake.xcor() - food.xcor()) ** 2 + (snake.ycor() - food.ycor()) ** 2) ** 0.5
    return distance1


def snake_body_collide():
    distance2 = ((snake.xcor() - body[1].xcor()) ** 2 + (snake.ycor() - body[1].ycor()) ** 2) ** 0.5
    return distance2


turtle.listen()

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

body = []
body.append(snake)

pen = turtle.Turtle()
pen.color('white')
pen.shape('square')
pen.speed(0)
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Score: 0  Higherscore: 0', align='center', font=('Courier', 24, 'normal'))

score = 0
highscore = 0

while True:
    board.update()

    # If the snake ate the food
    if snake_food_collide() < 20:
        foodx = random.randint(-290, 290)
        foody = random.randint(-290, 290)
        food.goto(foodx, foody)

        new_body = turtle.Turtle()
        new_body.color('grey')
        new_body.shape('square')
        new_body.speed(0)
        new_body.penup()
        new_body.goto(0, 0)
        body.append(new_body)

        score += 1
        delay -= 0.001

        if score > highscore:
            highscore = score

        pen.clear()
        pen.write('Score: %s  Higherscore: %s' % (score, highscore), align='center', font=('Courier', 24, 'normal'))

    # Additional segments of the snake
    for i in range(len(body) - 1, 0, -1):
        x = body[i - 1].xcor()
        y = body[i - 1].ycor()
        body[i].goto(x, y)

    # If the snake touches itself (Die)
    if len(body) >= 3:
        for i in range(2, len(body)):
            if snake.xcor() == body[i].xcor() and snake.ycor() == body[i].ycor():
                print('You died')
                snake.goto(0, 0)
                for item in body:
                    item.goto(1000, 1000)
                body.clear()
                body.append(snake)
                score = 0
                pen.clear()
                pen.write('Score: %s  Higherscore: %s' % (score, highscore), align='center',
                          font=('Courier', 24, 'normal'))

                play_again = tkinter.messagebox.askquestion('', 'Play again?')
                if play_again == 'no':
                    print('Your highscore is: ', highscore)
                    quit()

                delay += score * 0.001
                time.sleep(2)

    # If the snake touches the border (Die)
    if abs(snake.xcor()) > 290 or abs(snake.ycor()) > 290:
        print('You died')
        snake.goto(0, 0)
        body.remove(snake)
        for item in body:
            item.goto(1000, 1000)
        body.clear()
        body.append(snake)
        score = 0
        pen.clear()
        pen.write('Score: %s  Higherscore: %s' % (score, highscore), align='center', font=('Courier', 24, 'normal'))

        play_again = tkinter.messagebox.askquestion('', 'Play again?')
        if play_again == 'no':
            print('Your highscore is: ', highscore)
            quit()

        delay += score * 0.001
        time.sleep(2)

    move()

    time.sleep(delay)

turtle.mainloop()
