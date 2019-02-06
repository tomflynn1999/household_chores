from typing import List

from flask import Flask
import random

app = Flask(__name__)

chores = ["clean the bathroom", "clean the kitchen", "empty the dishwasher","mop the floors",
          "vaccuum the floor","sweep the floor"]

people = ["Tom", "Alex", "Carter", "Spencer", "Kyle","Maliek"]

@app.route('/')
def chores():
    chore2 = random.choice(chores)
    person = random.choice(people)
    print(person + " needs to " + chore2)


if __name__ == '__main__':
    app.run()
