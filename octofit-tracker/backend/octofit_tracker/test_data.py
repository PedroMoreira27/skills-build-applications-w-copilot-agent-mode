# Test data for populating the octofit_db database

test_data = {
    "users": [
        {"username": "john_doe", "email": "john@example.com", "password": "password123"},
        {"username": "jane_doe", "email": "jane@example.com", "password": "password123"}
    ],
    "teams": [
        {"name": "Team Alpha", "members": ["john_doe", "jane_doe"]}
    ],
    "activities": [
        {"user": "john_doe", "activity_type": "Running", "duration": "00:30:00"},
        {"user": "jane_doe", "activity_type": "Cycling", "duration": "01:00:00"}
    ],
    "leaderboard": [
        {"user": "john_doe", "score": 100},
        {"user": "jane_doe", "score": 150}
    ],
    "workouts": [
        {"name": "Morning Yoga", "description": "A relaxing yoga session to start the day."},
        {"name": "HIIT", "description": "High-intensity interval training for advanced users."}
    ]
}
