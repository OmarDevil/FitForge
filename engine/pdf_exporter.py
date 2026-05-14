from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def draw_line(c, text, x, y, font="Helvetica", size=11):
    c.setFont(font, size)
    c.drawString(x, y, str(text))
    return y - 16


def draw_wrapped_text(c, text, x, y, max_width=480, font="Helvetica", size=11, line_height=15):
    c.setFont(font, size)

    words = str(text).split()
    line = ""

    for word in words:
        test_line = f"{line} {word}".strip()
        if c.stringWidth(test_line, font, size) <= max_width:
            line = test_line
        else:
            c.drawString(x, y, line)
            y -= line_height
            line = word

    if line:
        c.drawString(x, y, line)
        y -= line_height

    return y


def check_new_page(c, y):
    if y < 70:
        c.showPage()
        return 800
    return y


def generate_pdf(output_path, user, results, workout_plan, meal_plan, recommendations=None):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    y = height - 50
    x = 45

    c.setTitle("FitForge Plan")

    y = draw_line(c, "FitForge - Full Fitness Plan", x, y, "Helvetica-Bold", 18)
    y -= 10

    y = draw_line(c, "User Profile", x, y, "Helvetica-Bold", 14)
    y = draw_line(c, f"Name: {user.get('name')}", x, y)
    y = draw_line(c, f"Age: {user.get('age')}", x, y)
    y = draw_line(c, f"Gender: {user.get('gender')}", x, y)
    y = draw_line(c, f"Height: {user.get('height')} cm", x, y)
    y = draw_line(c, f"Weight: {user.get('weight')} kg", x, y)
    y = draw_line(c, f"Goal: {user.get('goal')}", x, y)
    y = draw_line(c, f"Experience: {user.get('experience')}", x, y)
    y = draw_line(c, f"Workout Days: {user.get('days')}", x, y)
    y = draw_line(c, f"Place: {user.get('place')}", x, y)
    y = draw_line(c, f"Budget: {user.get('budget')}", x, y)
    y = draw_line(c, f"Injuries: {user.get('injuries')}", x, y)

    y -= 10
    y = check_new_page(c, y)

    y = draw_line(c, "Body Analysis", x, y, "Helvetica-Bold", 14)
    y = draw_line(c, f"BMI: {results.get('bmi')} ({results.get('bmi_status')})", x, y)
    y = draw_line(c, f"BMR: {results.get('bmr')}", x, y)
    y = draw_line(c, f"TDEE: {results.get('tdee')}", x, y)
    y = draw_line(c, f"Target Calories: {results.get('target_calories')} kcal", x, y)
    y = draw_line(c, f"Protein: {results.get('protein')} g", x, y)
    y = draw_line(c, f"Carbs: {results.get('carbs')} g", x, y)
    y = draw_line(c, f"Fat: {results.get('fat')} g", x, y)
    y = draw_line(c, f"Water: {results.get('water')} L", x, y)

    y -= 10
    y = check_new_page(c, y)

    if recommendations:
        y = draw_line(c, "Smart Recommendations", x, y, "Helvetica-Bold", 14)
        for item in recommendations:
            y = check_new_page(c, y)
            y = draw_wrapped_text(c, f"- {item}", x + 10, y, max_width=490)
        y -= 10
        y = check_new_page(c, y)

    y = draw_line(c, "Nutrition Plan", x, y, "Helvetica-Bold", 14)
    y = draw_line(c, f"Meals Per Day: {meal_plan.get('meal_count')}", x, y)
    y = draw_line(c, f"Breakfast: {meal_plan.get('breakfast')}", x, y)
    y = draw_line(c, f"Lunch: {meal_plan.get('lunch')}", x, y)
    y = draw_line(c, f"Dinner: {meal_plan.get('dinner')}", x, y)
    y = draw_line(c, f"Snack 1: {meal_plan.get('snack_1')}", x, y)
    y = draw_line(c, f"Snack 2: {meal_plan.get('snack_2')}", x, y)

    y = draw_wrapped_text(c, f"Pre-Workout: {meal_plan.get('pre_workout')}", x, y, max_width=500)
    y = draw_wrapped_text(c, f"Post-Workout: {meal_plan.get('post_workout')}", x, y, max_width=500)

    y = draw_line(c, "Nutrition Tips:", x, y, "Helvetica-Bold", 12)
    for tip in meal_plan.get("tips", []):
        y = check_new_page(c, y)
        y = draw_wrapped_text(c, f"- {tip}", x + 10, y, max_width=490)

    y -= 10
    y = check_new_page(c, y)

    y = draw_line(c, "Workout Plan", x, y, "Helvetica-Bold", 14)

    for day in workout_plan:
        y = check_new_page(c, y)
        y = draw_line(c, day.get("title"), x, y, "Helvetica-Bold", 12)

        for exercise in day.get("exercises", []):
            y = check_new_page(c, y)
            line = f"- {exercise.get('name')} | Sets: {exercise.get('sets')} | Reps: {exercise.get('reps')} | Rest: {exercise.get('rest')}"
            y = draw_wrapped_text(c, line, x + 10, y, max_width=490)

        y -= 6

    c.save()