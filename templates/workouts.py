from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Dummy data for demonstration purposes
workouts = {
    "2023-12-24": ["Pushups", "Squats", "Running"],
    "2023-12-25": ["Pull-ups", "Lunges", "Cycling"]
    # Add more days and workouts as needed
}
def index():
    todays_workouts = get_todays_workouts()
    return render_template('frontend.html', workouts=todays_workouts)

def get_todays_workouts():
    today_date = datetime.date.today().isoformat()  # Get today's date in YYYY-MM-DD format
    return workouts.get(today_date, ["Rest Day"])

if __name__ == '__main__':
    app.run(debug=True)