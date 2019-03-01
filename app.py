from flask import Flask, render_template, request
import random
import schedule
import sqlite3
import calendar
import time

app = Flask(__name__)

people = ["Tom", "Alex", "Carter", "Spencer", "Kyle", "Maliek"]

chores = ["clean the bathroom", "clean the kitchen", "empty the dishwasher","mop the floors",
          "vaccuum the floor","sweep the floor"]

due_dates = ["March 20","March 17","March 18","March 21", "March 16", "March 22"]


conn = sqlite3.connect('chores.db')
c = conn.cursor()

def create_table():
    c.execute("Create Table IF NOT EXISTS stuffToPlot(name TEXT, chore TEXT, date TEXT, completed TEXT)")

def data_entry():
    c.excecute('INSERT INTO stuffToPlot VALUES("Tom", "sweep the floor", "March 22nd", "False")')
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()


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
