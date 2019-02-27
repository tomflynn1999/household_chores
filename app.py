from flask import Flask, render_template, request
import random
import schedule
import sqlite3 as sql
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


@app.route('/enternew')
def new_student():
   return render_template('db_builder.html')


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']

            with sql.connect("database.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO students (name,addr,city,pin) VALUES(?, ?, ?, ?)",(nm,addr,city,pin) )

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)

if __name__ == '__main__':
    app.run()
