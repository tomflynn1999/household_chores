from typing import List

from flask import Flask
import random

app = Flask(__name__)

chores = ["clean the bathroom", "clean the kitchen", "empty the dishwasher","mop the floors",
          "vaccuum the floor","sweep the floor"]

people = ["Tom", "Alex", "Carter", "Spencer", "Kyle","Maliek"]

@app.route('/')
def chores1():
    while (len(chores) < 0)
          chore2 = random.choice(chores)
          chores.remove(chores2)
          person = random.choice(people)
          people.remove(person)
    return person + " needs to " + chore2


if __name__ == '__main__':
    app.run()
