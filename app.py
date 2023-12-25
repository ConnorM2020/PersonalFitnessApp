from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # You should set a secret key for session handling

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Here you would validate the username and password
        # For simplicity, we'll assume any user is valid
        session['username'] = username
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/')
def home():
    if 'username' in session:
        # Pass the username to the template
        return render_template('frontend.html', username=session['username'])
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
