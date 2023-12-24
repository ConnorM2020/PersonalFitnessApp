from flask import Flask, render_template
import workouts  # This assumes your workouts.py has functions you want to use

app = Flask(__name__)

@app.route('/')
def home():
    # You can call a function from workouts.py to get the data you want to display
    daily_workouts = workouts.get_daily_workouts()
    return render_template('frontend.html', workouts=daily_workouts)

if __name__ == '__main__':
    app.run(debug=True)