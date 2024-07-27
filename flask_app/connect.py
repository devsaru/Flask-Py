from flask import Flask,render_template
import sqlite3

conn = sqlite3.connect('sqlite-sakile.db')
conn.row_factory = sqlite3.Row
print('open the database successfully')

cur = conn.cursor()

app = Flask(__name__)
@app.route('/sql')

def sql_data():
    conn = sqlite3.connect('sqlite-sakila.db')
    conn.row_factory = sqlite3.Row
    print('Opened the databse successfully in our python function=============')

    cur = conn.cursor()
    sql = """SELECT customer_id,store_id,first_name,last_name,email,address_id,active,create_date,last_update from customer"""
    print(sql)

    cur.execute(sql)
    results = cur.fetchall()
    print('SQL Data:',results)
    return render_template('test.html',test=results)

#sql_data()

app.run(debug=True)