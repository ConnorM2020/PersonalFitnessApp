from flask import Blueprint, Flask, jsonify
import datetime, random

app = Flask(__name__)

# Dummy data for demonstration purposes
exercises = ["Pushups", "Squats", "Running", "Pull-ups", "Muscle-ups", "Cardio", "Leg extension", "Stretching", "Chest-Press"]

# Function to create random workouts
def create_random_workouts():
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date(2023, 12, 31)
    delta = datetime.timedelta(days=1)

    workouts = {}
    current_date = start_date
    while current_date <= end_date:
        # Select 3 random exercises for each day
        workouts[current_date.isoformat()] = random.sample(exercises, 3)
        current_date += delta

    return workouts

# Generate workouts for the year
year_workouts = create_random_workouts()

@app.route('/api/todays-workouts')
def todays_workouts_api():
    todays_workouts = get_todays_workouts()
    return jsonify(todays_workouts)

def get_todays_workouts():
    today_date = datetime.date.today().isoformat()  # Get today's date in YYYY-MM-DD format
    return year_workouts.get(today_date, ["Rest Day"])

if __name__ == '__main__':
    app.run(debug=True)