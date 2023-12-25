from flask import Flask, render_template
import datetime

app = Flask(__name__)

# Dummy data for demonstration purposes
workouts = {
    "2023-12-24": ["Pushups", "Squats", "Running"],
    "2023-12-25": ["Pull-ups", "Lunges", "Cycling"]
    # Add more days and workouts as needed
}

@app.route('/')
def home():
    today_date = datetime.date.today().isoformat()  # Get today's date in YYYY-MM-DD format
    todays_workouts = workouts.get(today_date, ["Rest Day"])  # Get workouts or default to rest
    return render_template('index.html', workouts=todays_workouts)

if __name__ == '__main__':
    app.run(debug=True)
