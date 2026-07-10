from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

# HOME
@app.route('/')
def home():
    return redirect('/login')


# REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        password = generate_password_hash(request.form['password'])

        cur = mysql.connection.cursor()

        cur.execute(
            "INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",
            (name, email, password)
        )

        mysql.connection.commit()
        cur.close()

        flash("Registration Successful")
        return redirect('/login')

    return render_template('register.html')


# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT * FROM users WHERE email=%s",
            [email]
        )

        user = cur.fetchone()

        cur.close()

        if user and check_password_hash(user[3], password):

            session['user_id'] = user[0]
            session['name'] = user[1]

            return redirect('/dashboard')

        flash("Invalid Credentials")

    return render_template('login.html')


# LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# DASHBOARD
@app.route('/dashboard')
def dashboard():

    if 'user_id' not in session:
        return redirect('/login')

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT * FROM tasks WHERE user_id=%s ORDER BY id DESC",
        [session['user_id']]
    )

    tasks = cur.fetchall()

    cur.execute(
        "SELECT COUNT(*) FROM tasks WHERE user_id=%s",
        [session['user_id']]
    )

    total = cur.fetchone()[0]

    cur.execute(
        "SELECT COUNT(*) FROM tasks WHERE user_id=%s AND status='Completed'",
        [session['user_id']]
    )

    completed = cur.fetchone()[0]

    pending = total - completed

    cur.close()

    return render_template(
        'dashboard.html',
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending
    )


# ADD TASK
@app.route('/add', methods=['GET', 'POST'])
def add_task():

    if request.method == 'POST':

        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        status = request.form['status']
        due_date = request.form['due_date']

        cur = mysql.connection.cursor()

        cur.execute("""
        INSERT INTO tasks
        (user_id,title,description,priority,status,due_date)
        VALUES(%s,%s,%s,%s,%s,%s)
        """,
        (
            session['user_id'],
            title,
            description,
            priority,
            status,
            due_date
        ))

        mysql.connection.commit()
        cur.close()

        return redirect('/dashboard')

    return render_template('add_task.html')


# EDIT TASK
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):

    cur = mysql.connection.cursor()

    if request.method == 'POST':

        title = request.form['title']
        description = request.form['description']
        priority = request.form['priority']
        status = request.form['status']
        due_date = request.form['due_date']

        cur.execute("""
        UPDATE tasks
        SET title=%s,
            description=%s,
            priority=%s,
            status=%s,
            due_date=%s
        WHERE id=%s
        """,
        (
            title,
            description,
            priority,
            status,
            due_date,
            id
        ))

        mysql.connection.commit()

        return redirect('/dashboard')

    cur.execute("SELECT * FROM tasks WHERE id=%s", [id])

    task = cur.fetchone()

    cur.close()

    return render_template('edit_task.html', task=task)


# DELETE TASK
@app.route('/delete/<int:id>')
def delete_task(id):

    cur = mysql.connection.cursor()

    cur.execute(
        "DELETE FROM tasks WHERE id=%s",
        [id]
    )

    mysql.connection.commit()

    cur.close()

    return redirect('/dashboard')


if __name__ == "__main__":
    app.run(debug=True)