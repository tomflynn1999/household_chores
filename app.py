from typing import List

from flask import Flask, render_template
import random
import schedule
import time
import jinja2
import template

app = Flask(__name__)

chores = ["clean the bathroom", "clean the kitchen", "empty the dishwasher","mop the floors",
          "vaccuum the floor","sweep the floor"]

people = ["Tom", "Alex", "Carter", "Spencer", "Kyle","Maliek"]

due_dates = ["Feb 20","Feb 17","Feb 18","Feb 21", "Feb 16", "Feb 22"]


def chores1():
    while len(chores) > 0:
        chore2 = random.choice(chores)
        chores.remove(chore2)
        person = random.choice(people)
        people.remove(person)
        dates = random.choice(due_dates)
        due_dates.remove(dates)
        return person + " needs to " + chore2 + " by " + dates


@app.route('/2')
def chores_():
    for p in people:
        chore2 = random.choice(chores)
        chores.remove(chore2)
        dates2 = random.choice(due_dates)
        return p + " needs to " + chore2 + "by" + dates2

@app.route('/3')
def chores_assignment():
    schedule.every().sunday.do(chores_)

@app.route('/')
def chores_template():
    return render_template('chores.html')

if __name__ == '__main__':
    app.run()
