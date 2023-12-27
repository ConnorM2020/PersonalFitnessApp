from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'secret_key'

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    # Check if username is in the session
    if 'username' not in session:
        # Redirect to the login page if the user is not logged in
        return redirect(url_for('login'))

    username = session['username']

    # Fetch user details from database based on username
    user = user.query.filter_by(username=username).first()

    if request.method == 'POST':
        # Extract data from form submission
        name = request.form.get('name')
        age = request.form.get('age')
        password = request.form.get('changepassword')  # Ensure this matches your form's input name

        # Update user details and password if a new one is provided
        if user:
            user.name = name
            user.age = age

            if password:  # Update the password only if it's provided
                user.password_hash = generate_password_hash(password)

            # Save changes to database
            # db.session.commit()

            flash('Your profile was updated successfully!', 'success')

        # Redirect back to the profile page or a confirmation page as needed
        return redirect(url_for('profile'))

    # Render the profile template, passing in user details
    return render_template('profile.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
