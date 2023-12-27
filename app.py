from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from templates.workouts import get_todays_workouts
app = Flask(__name__)
app.secret_key = 'secret_key' 

# here are all the routes taken and posible throughout the application
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['username'] = username
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove 'username' from session
    return redirect(url_for('login'))

@app.route('/')
def home():
    if 'username' in session:
        todays_workouts = get_todays_workouts()
        # Pass the username to the template
        return render_template('frontend.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/api/todays-workouts')
def todays_workouts_api():
    todays_workouts = get_todays_workouts()
    return jsonify(todays_workouts)


def profile():
    if 'username' in session:
        return render_template('profile.html', username=session['username'])
    else:
        return redirect(url_for('login'))
    
if __name__ == '__main__':
    app.run(debug=True)
