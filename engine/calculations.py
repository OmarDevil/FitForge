def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    return round(bmi, 1)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    return "Obese"


def calculate_bmr(weight, height_cm, age, gender):
    gender = gender.lower()

    if gender == "male":
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161

    return round(bmr)


def calculate_tdee(bmr, activity_level):
    multipliers = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "active": 1.725,
        "very_active": 1.9
    }

    multiplier = multipliers.get(activity_level, 1.2)
    return round(bmr * multiplier)


def calculate_target_calories(tdee, goal):
    goal = goal.lower()

    if goal == "fat loss":
        return tdee - 400
    elif goal == "muscle gain":
        return tdee + 300
    elif goal == "maintain":
        return tdee
    else:
        return tdee - 100


def calculate_macros(weight, calories, goal):
    goal = goal.lower()

    if goal == "fat loss":
        protein = round(weight * 2.0)
        fat = round(weight * 0.8)
    elif goal == "muscle gain":
        protein = round(weight * 1.8)
        fat = round(weight * 0.9)
    else:
        protein = round(weight * 1.8)
        fat = round(weight * 0.8)

    protein_calories = protein * 4
    fat_calories = fat * 9
    carbs = round((calories - protein_calories - fat_calories) / 4)

    if carbs < 0:
        carbs = 0

    return {
        "protein": protein,
        "fat": fat,
        "carbs": carbs
    }


def calculate_water_intake(weight):
    return round(weight * 0.035, 1)