from flask import Flask, render_template
import random
import schedule
import time
import template

app = Flask(__name__)

people = ["Tom", "Alex", "Carter", "Spencer", "Kyle", "Maliek"]

chores = ["clean the bathroom", "clean the kitchen", "empty the dishwasher","mop the floors",
          "vaccuum the floor","sweep the floor"]

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
    people = ["Tom", "Alex", "Carter", "Spencer", "Kyle", "Maliek"]
    chores = ["clean the bathroom", "clean the kitchen", "empty the dishwasher", "mop the floors",
              "vaccuum the floor", "sweep the floor"]

    chore_list = []
    for i in range(len(people)):
        idx_person = random.randint(0, len(people)-1)
        person = people[idx_person]
        del people[idx_person]
        idx_chore = random.randint(0, len(chores)-1)
        chore = chores[idx_chore]
        del chores[idx_chore]
        chore_list.append([person, chore])

    return render_template('chores.html', people=people, chores=chores, chore_list=chore_list)

if __name__ == '__main__':
    app.run()
