from flask import Flask, render_template
import random
import sqlite3

app = Flask(__name__)

people = ["Tom", "Alex", "Carter", "Spencer", "Kyle", "Maliek"]

chores = ["clean the bathroom", "clean the movie room", "empty the dishwasher", "wipe the counters",
              "vaccuum the floor", "sweep the floor"]

due_dates = ["March 20","March 17","March 18","March 21", "March 16", "March 22"]


def create_table():
    conn = sqlite3.connect('chores.db')
    c = conn.cursor()
    c.execute("Create Table IF NOT EXISTS stuffToPlot(name TEXT, chore TEXT, date DATE , completed )")


create_table()


@app.route('/')
def db_template():
    conn = sqlite3.connect('chores.db')
    c = conn.cursor()
    c.execute("SELECT * FROM stuffToPlot")
    data = c.fetchall()
    return render_template('db_chores.html', data = data)


@app.route('/1')
def chores_template():
    people = ["Tom", "Alex", "Carter", "Spencer", "Kyle", "Maliek"]
    chores = ["clean the bathroom", "clean the movie room", "empty the dishwasher", "wipe the counters",
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
