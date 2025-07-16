from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time



# === Screen Setup ===
screen = Screen()

screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)


# === Game Objects ===
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()



# === Key Bindings ===
screen.listen()
screen.onkeypress(fun=player.move_up, key="Up")


# === Game Loop ===
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect turtle collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect player's successful crossing
    if player.is_at_finish_line():
        scoreboard.increase_game_level()
        player.go_to_start()
        car_manager.level_up()





screen.exitonclick()