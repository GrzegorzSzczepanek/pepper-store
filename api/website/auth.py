from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    # print(data)
    return render_template('login.html', text="test login", user="test user")


@auth.route('/logout')
def logout():

    return "render_template('logout.html')"


@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')
        repeat_password = data.get('repeat_password')
        print(username, password, repeat_password)

        if password == repeat_password and len(password) >= 8:
            flash('Account created!', category='success')
        else:
            flash('Passwords don\'t match!', category='error')

    return render_template('signup.html')
