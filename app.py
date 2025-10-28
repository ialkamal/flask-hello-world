from flask import Flask
app = Flask(__name__)
import psycopg2

DB_URL = "postgresql://flaskdb_30hv_user:GjYAjXsiwu0JKVQnDcJezevBJ3YsyWKY@dpg-d40bfvjipnbc73cii1f0-a/flaskdb_30hv"

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect(DB_URL)
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"

@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"

@app.route('/db_select')
def selecting():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
        ''')
    records = cur.fetchall()
    conn.commit()
    conn.close()
    html = "<table>"
    for record in records:
        html += f"""
        <tr>
            <td>{record[0]}</td>
            <td>{record[1]}</td>
            <td>{record[2]}</td>
            <td>{record[3]}</td>
            <td>{record[4]}</td>
        </tr>"""
    html += "</table>"
    return html

@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"