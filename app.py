from flask import Flask, render_template
import random
import schedule
import calendar
import time

app = Flask(__name__)

people = ["Tom", "Alex", "Carter", "Spencer", "Kyle", "Maliek"]

chores = ["clean the bathroom", "clean the kitchen", "empty the dishwasher","mop the floors",
          "vaccuum the floor","sweep the floor"]

due_dates = ["March 20","March 17","March 18","March 21", "March 16", "March 22"]


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
    due_dates = ["March 20", "March 17", "March 18", "March 21", "March 16", "March 22"]
    chore_list = []
    for i in range(len(people)):
        idx_person = random.randint(0, len(people)-1)
        person = people[idx_person]
        del people[idx_person]
        idx_chore = random.randint(0, len(chores)-1)
        chore = chores[idx_chore]
        del chores[idx_chore]
        idx_due_dates = random.randint(0, len(due_dates)-1)
        due_date = due_dates[idx_due_dates]
        chore_list.append([person, chore, due_date])

    return render_template('chores.html', people=people, chores=chores, due_dates=due_dates, chore_list=chore_list)

if __name__ == '__main__':
    app.run()
