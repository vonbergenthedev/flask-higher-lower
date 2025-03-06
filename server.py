import random

from flask import Flask

app = Flask(__name__)

countdown_gif = 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXQ4ZzFtZmFvYWEydmplN2pkazVlb2lpc3F0aDl3bnc0aG56emduYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/dWekZnK0pKn0gdlvDK/giphy.gif'
wrong_cat_gif = 'https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXY2c2RieXExMWp6czk2ZXp0MXJsY2p1N2h3dW5kaDZ1Ym15MHh3dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LZaA5gGjbUJOw/giphy.gif'
right_cat_gif = 'https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWdtdmQ4eWFncngyOXdrczd4ZWt3dzI0Y3FhMXJqdmw2dnUwbDBuYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oriO0OEd9QIDdllqo/giphy.gif'
fire_gif = 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHMwc3ZoNG52c2d2bzh5Y3oybHpudmc4OTE4dDYybHQ4ZHAwd3B0aiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Lopx9eUi34rbq/giphy.gif'

random_number = random.randint(0, 9)


def too_low_or_high(func):
    def guess_check(guess):

        try:
            num_check = int(guess)
        except ValueError:
            return ('<h1>Enter a valid integer between 0-9!</h1>'
                    f'<img src="{fire_gif}">')

        if num_check > 9 or num_check < 0:
            return ('<h1>Enter a guess between 0-9!</h1>'
                    f'<img src="{fire_gif}"/>')
        elif num_check < random_number:
            return ('<h1 style="color:blue">Too low! Try again!</h1>'
                    f'<img src="{wrong_cat_gif}"/>')
        elif num_check > random_number:
            return ('<h1 style="color:red">Too high! Try again!</h1>'
                    f'<img src="{wrong_cat_gif}"/>')
        else:
            return ('<h1 style="color:green">Correct! You got it!!!</h1>'
                    f'<img src="{right_cat_gif}"/>')

    return guess_check


@app.route('/')
def home_page():
    return ('<h1>Guess a number between 0 and 9</h1>'
            f'<img src="{countdown_gif}">')


@app.route('/<guess>')
@too_low_or_high
def guess_number(guess):
    return guess


if __name__ == '__main__':
    app.run(debug=True)
