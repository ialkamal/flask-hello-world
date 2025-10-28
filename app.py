from flask import Flask
app = Flask(__name__)
import psycopg2

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://flaskdb_30hv_user:GjYAjXsiwu0JKVQnDcJezevBJ3YsyWKY@dpg-d40bfvjipnbc73cii1f0-a/flaskdb_30hv")
    conn.close()
    return "Database Connection Successful"