def remove_exercises_by_keywords(exercises, keywords):
    filtered = []
    for exercise in exercises:
        name_lower = exercise["name"].lower()
        if not any(keyword in name_lower for keyword in keywords):
            filtered.append(exercise)
    return filtered


def apply_injury_modifications(plan, injuries_text):
    injuries = injuries_text.lower()

    for day in plan:
        exercises = day["exercises"]

        if "knee" in injuries:
            exercises = remove_exercises_by_keywords(
                exercises,
                ["squat", "lunge", "jump"]
            )

        if "shoulder" in injuries:
            exercises = remove_exercises_by_keywords(
                exercises,
                ["overhead", "shoulder press", "upright row", "dip"]
            )

        if "back" in injuries or "lower back" in injuries:
            exercises = remove_exercises_by_keywords(
                exercises,
                ["deadlift", "bent-over", "barbell row", "good morning"]
            )

        day["exercises"] = exercises

    return plan


def gym_full_body_3():
    return [
        {
            "title": "Day 1 - Full Body A",
            "exercises": [
                {"name": "Goblet Squat", "sets": 3, "reps": "10-12", "rest": "60 sec"},
                {"name": "Bench Press", "sets": 3, "reps": "8-10", "rest": "90 sec"},
                {"name": "Lat Pulldown", "sets": 3, "reps": "10-12", "rest": "60 sec"},
                {"name": "Romanian Deadlift", "sets": 3, "reps": "10", "rest": "90 sec"},
                {"name": "Plank", "sets": 3, "reps": "30-45 sec", "rest": "45 sec"},
            ],
        },
        {
            "title": "Day 2 - Full Body B",
            "exercises": [
                {"name": "Leg Press", "sets": 3, "reps": "10-12", "rest": "60 sec"},
                {"name": "Incline Dumbbell Press", "sets": 3, "reps": "10", "rest": "60 sec"},
                {"name": "Seated Cable Row", "sets": 3, "reps": "10-12", "rest": "60 sec"},
                {"name": "Dumbbell Shoulder Press", "sets": 3, "reps": "10", "rest": "60 sec"},
                {"name": "Hanging Knee Raise", "sets": 3, "reps": "12-15", "rest": "45 sec"},
            ],
        },
        {
            "title": "Day 3 - Full Body C",
            "exercises": [
                {"name": "Smith Machine Squat", "sets": 3, "reps": "10", "rest": "75 sec"},
                {"name": "Chest Press Machine", "sets": 3, "reps": "10-12", "rest": "60 sec"},
                {"name": "One Arm Dumbbell Row", "sets": 3, "reps": "10 each side", "rest": "60 sec"},
                {"name": "Hamstring Curl", "sets": 3, "reps": "12", "rest": "45 sec"},
                {"name": "Cable Crunch", "sets": 3, "reps": "15", "rest": "45 sec"},
            ],
        },
    ]


def gym_upper_lower_4():
    return [
        {
            "title": "Day 1 - Upper Body",
            "exercises": [
                {"name": "Bench Press", "sets": 4, "reps": "8-10", "rest": "90 sec"},
                {"name": "Lat Pulldown", "sets": 4, "reps": "10-12", "rest": "60 sec"},
                {"name": "Dumbbell Shoulder Press", "sets": 3, "reps": "10", "rest": "60 sec"},
                {"name": "Cable Row", "sets": 3, "reps": "10-12", "rest": "60 sec"},
                {"name": "Biceps Curl", "sets": 3, "reps": "12", "rest": "45 sec"},
                {"name": "Triceps Pushdown", "sets": 3, "reps": "12", "rest": "45 sec"},
            ],
        },
        {
            "title": "Day 2 - Lower Body",
            "exercises": [
                {"name": "Squat", "sets": 4, "reps": "8-10", "rest": "90 sec"},
                {"name": "Romanian Deadlift", "sets": 3, "reps": "10", "rest": "90 sec"},
                {"name": "Leg Press", "sets": 3, "reps": "12", "rest": "60 sec"},
                {"name": "Hamstring Curl", "sets": 3, "reps": "12", "rest": "45 sec"},
                {"name": "Standing Calf Raise", "sets": 3, "reps": "15", "rest": "30 sec"},
            ],
        },
        {
            "title": "Day 3 - Upper Body",
            "exercises": [
                {"name": "Incline Dumbbell Press", "sets": 4, "reps": "10", "rest": "60 sec"},
                {"name": "Seated Cable Row", "sets": 4, "reps": "10-12", "rest": "60 sec"},
                {"name": "Lateral Raise", "sets": 3, "reps": "15", "rest": "30 sec"},
                {"name": "Chest Fly Machine", "sets": 3, "reps": "12", "rest": "45 sec"},
                {"name": "Hammer Curl", "sets": 3, "reps": "12", "rest": "45 sec"},
                {"name": "Overhead Triceps Extension", "sets": 3, "reps": "12", "rest": "45 sec"},
            ],
        },
        {
            "title": "Day 4 - Lower Body",
            "exercises": [
                {"name": "Deadlift", "sets": 3, "reps": "6-8", "rest": "120 sec"},
                {"name": "Walking Lunges", "sets": 3, "reps": "12 each leg", "rest": "60 sec"},
                {"name": "Leg Extension", "sets": 3, "reps": "12", "rest": "45 sec"},
                {"name": "Hip Thrust", "sets": 3, "reps": "10-12", "rest": "60 sec"},
                {"name": "Seated Calf Raise", "sets": 3, "reps": "15", "rest": "30 sec"},
            ],
        },
    ]


def home_full_body_3():
    return [
        {
            "title": "Day 1 - Full Body A",
            "exercises": [
                {"name": "Bodyweight Squat", "sets": 3, "reps": "15", "rest": "45 sec"},
                {"name": "Push Up", "sets": 3, "reps": "10-15", "rest": "60 sec"},
                {"name": "Glute Bridge", "sets": 3, "reps": "15", "rest": "45 sec"},
                {"name": "Backpack Row", "sets": 3, "reps": "12", "rest": "60 sec"},
                {"name": "Plank", "sets": 3, "reps": "30-45 sec", "rest": "45 sec"},
            ],
        },
        {
            "title": "Day 2 - Full Body B",
            "exercises": [
                {"name": "Reverse Lunge", "sets": 3, "reps": "12 each leg", "rest": "45 sec"},
                {"name": "Pike Push Up", "sets": 3, "reps": "8-12", "rest": "60 sec"},
                {"name": "Chair Step Up", "sets": 3, "reps": "12 each leg", "rest": "45 sec"},
                {"name": "Superman Hold", "sets": 3, "reps": "20 sec", "rest": "30 sec"},
                {"name": "Dead Bug", "sets": 3, "reps": "12", "rest": "30 sec"},
            ],
        },
        {
            "title": "Day 3 - Full Body C",
            "exercises": [
                {"name": "Wall Sit", "sets": 3, "reps": "30 sec", "rest": "30 sec"},
                {"name": "Incline Push Up", "sets": 3, "reps": "12-15", "rest": "45 sec"},
                {"name": "Single Leg Glute Bridge", "sets": 3, "reps": "10 each leg", "rest": "45 sec"},
                {"name": "Towel Row", "sets": 3, "reps": "12", "rest": "60 sec"},
                {"name": "Mountain Climbers", "sets": 3, "reps": "20", "rest": "30 sec"},
            ],
        },
    ]


def home_upper_lower_4():
    return [
        {
            "title": "Day 1 - Upper Body",
            "exercises": [
                {"name": "Push Up", "sets": 4, "reps": "10-15", "rest": "60 sec"},
                {"name": "Backpack Row", "sets": 4, "reps": "12", "rest": "60 sec"},
                {"name": "Pike Push Up", "sets": 3, "reps": "8-12", "rest": "60 sec"},
                {"name": "Chair Dips", "sets": 3, "reps": "10", "rest": "45 sec"},
                {"name": "Biceps Curl with Backpack", "sets": 3, "reps": "12", "rest": "45 sec"},
            ],
        },
        {
            "title": "Day 2 - Lower Body",
            "exercises": [
                {"name": "Bodyweight Squat", "sets": 4, "reps": "15", "rest": "45 sec"},
                {"name": "Reverse Lunge", "sets": 3, "reps": "12 each leg", "rest": "45 sec"},
                {"name": "Glute Bridge", "sets": 3, "reps": "15", "rest": "45 sec"},
                {"name": "Wall Sit", "sets": 3, "reps": "30 sec", "rest": "30 sec"},
                {"name": "Standing Calf Raise", "sets": 3, "reps": "20", "rest": "30 sec"},
            ],
        },
        {
            "title": "Day 3 - Upper Body",
            "exercises": [
                {"name": "Incline Push Up", "sets": 4, "reps": "12-15", "rest": "45 sec"},
                {"name": "Towel Row", "sets": 4, "reps": "12", "rest": "60 sec"},
                {"name": "Shoulder Tap Push Up", "sets": 3, "reps": "10", "rest": "45 sec"},
                {"name": "Chair Dips", "sets": 3, "reps": "10", "rest": "45 sec"},
                {"name": "Plank", "sets": 3, "reps": "40 sec", "rest": "30 sec"},
            ],
        },
        {
            "title": "Day 4 - Lower Body",
            "exercises": [
                {"name": "Chair Step Up", "sets": 4, "reps": "12 each leg", "rest": "45 sec"},
                {"name": "Single Leg Glute Bridge", "sets": 3, "reps": "10 each leg", "rest": "45 sec"},
                {"name": "Jump Squat", "sets": 3, "reps": "12", "rest": "45 sec"},
                {"name": "Hamstring Slide", "sets": 3, "reps": "12", "rest": "45 sec"},
                {"name": "Standing Calf Raise", "sets": 3, "reps": "20", "rest": "30 sec"},
            ],
        },
    ]


def generate_workout_plan(days, place, experience, injuries):
    place = place.lower()
    experience = experience.lower()

    if days <= 3:
        plan = gym_full_body_3() if place == "gym" else home_full_body_3()
    else:
        plan = gym_upper_lower_4() if place == "gym" else home_upper_lower_4()

    if experience == "advanced":
        for day in plan:
            for exercise in day["exercises"]:
                if exercise["sets"] < 4:
                    exercise["sets"] += 1

    plan = apply_injury_modifications(plan, injuries)
    return plan