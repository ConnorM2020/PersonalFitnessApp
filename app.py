from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from templates.workouts import get_todays_workouts, jsonify
import json # using JSON instead 

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
        return render_template('frontend.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/api/todays-workouts')
def todays_workouts_api():
    todays_workouts = get_todays_workouts()
    return jsonify(todays_workouts)

@app.route('/Profile', methods=['GET', 'POST'])
def profile():
    if 'username' in session:
        if request.method == 'POST':
            # Extract and validate form data, then update the user profile
            name = request.form['name']
            password = request.form['changepassword']  # Hash the password before storing
            age = request.form['age']
            try:
                update_user_profile(name, password, age, session['username'])
                # If the update is successful, you might want to redirect to a confirmation page or back to the profile
                return jsonify({'success': True, 'message': 'Profile updated successfully'})
            except Exception as e:
                return jsonify({'success': False, 'message': str(e)}), 500
        else:
            # If it's a GET request, you want to render the Profile.html template
            user_data = get_user_data(session['username'])
            # Make sure to pass any necessary data to the template
            return render_template('Profile.html', user=user_data)
    else:
        # If the user is not logged in, redirect to the login page
        return redirect(url_for('login'))
    
# save data from inital login aswell    
def save_user_data(user_data):
     with open('users.json', 'w') as file:
        json.dump(user_data, file)


def load_user_data():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def update_user_profile(name, password, age, username):
    # Load the existing data
    user_data = load_user_data()

    user_data[username] = {
        'name': name,
        'password': password,  # Hash the password before storing it in a real application
        'age': age
    }
    save_user_data(user_data)
    return True

def get_user_data(username):
    user_data = load_user_data()
    return user_data.get(username, {'name': '', 'age': ''})


if __name__ == '__main__':
    app.run(debug=True)