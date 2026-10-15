
from flask import flask, render_template, request
import mysql.connector 
import re
app = Flask(__name__)
@app.route('/login', methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username'in request.form an 'password' in request.form:

        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(
            host="remotesql.com",
            user="Rz8hqnldk4",
            password = "nd0wK03xe0",
            database = "Rz8hqnldk4"
        )

        mycursor=mydb.cursor()
        mycursor.execute("SELECT * FROM LoginDetails WHERE Name= %s AND Password = %s", (username, password))
        account = mycursor.fetchone()
        if account:
            print('login success')
            name = account[1]
            id = account[0]
            msg = 'Logged in Successfully'
            print('login successful! ')
            return render_template('welcomepage.html', msg=msg, name=name, id=id)
        else: 
            return render_template('loginpage.html')

    def register():
        msg =''
        if request.method == 'POST' and username in request.form and password in request.form and email in request.form: 
            username = request.form['username']
            password = request.form['password']
            email = request.form['email']
            mydb = mysql.connector.connect(
                host='remoteysql.com',
                user='Rz8hqnlk4',
                password='nd6wK03xe0',
                database='Rz8hqnlk4'
            )
            mycursor = mydb.cursor()
            print(username)
            mycursor.execute('SELECT * FROM LoginDetails WHERE Name = %s AND Email_id = %s ', (username,email))
            account = mycursor.fetchone()
            print(account)
            if account: 
                msg = 'Account already exists'
            elif = not re.match(r'^[^\d]*@[^\d]*\.\.[^\d]*$', email):
