from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def random_car(self):

        random_chance = random.randint(1,6)        ## random chance ensure the cars didnt appear fast,
        # if the random chance picks 1 between 1 and 6 then oly the car will appear
        if random_chance == 1:
            new_turtle = Turtle()
            new_turtle.shape("square")

            new_turtle.color(random.choice(COLORS))
            new_turtle.shapesize(stretch_wid=1,stretch_len=2)

            new_turtle.penup()
            new_y= random.randint(-250, 250)
            new_turtle.goto(300, new_y)

            self.all_cars.append(new_turtle)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


