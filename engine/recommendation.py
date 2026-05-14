def generate_recommendations(user, results):
    recommendations = []

    goal = str(user.get("goal", "")).lower()
    experience = str(user.get("experience", "")).lower()
    place = str(user.get("place", "")).lower()
    injuries = str(user.get("injuries", "")).lower()
    days = int(user.get("days", 3))
    bmi = float(user.get("weight", 0)) / ((float(user.get("height", 1)) / 100) ** 2)

    if goal == "fat loss":
        recommendations.append("Keep a moderate calorie deficit and track your body weight weekly.")
        recommendations.append("Prioritize protein in every meal to preserve muscle while losing fat.")
        recommendations.append("Add 2 to 4 cardio sessions weekly if daily activity is low.")

    elif goal == "muscle gain":
        recommendations.append("Stay in a small calorie surplus and monitor weekly weight gain.")
        recommendations.append("Focus on progressive overload in compound exercises.")
        recommendations.append("Do not skip post-workout meals and daily protein targets.")

    elif goal == "maintain":
        recommendations.append("Keep calories close to maintenance and focus on training quality.")
        recommendations.append("Track weight weekly to catch unwanted changes early.")

    else:
        recommendations.append("Train consistently and focus on technique, recovery, and balanced nutrition.")
        recommendations.append("Keep protein high and maintain regular activity through the week.")

    if experience == "beginner":
        recommendations.append("Focus on correct form before increasing weight or volume.")
        recommendations.append("3 to 4 training days are enough to make strong early progress.")
    elif experience == "intermediate":
        recommendations.append("Track weights, reps, and rest times to ensure progression.")
    elif experience == "advanced":
        recommendations.append("Use heavier top sets with controlled accessories and recovery management.")

    if place == "home":
        recommendations.append("Use slower tempo, pauses, and extra reps to increase difficulty at home.")
    else:
        recommendations.append("Base your progress around compound lifts and controlled machine work.")

    if days <= 3:
        recommendations.append("A full-body approach works well with your weekly schedule.")
    else:
        recommendations.append("An upper/lower split fits your available training days well.")

    if "knee" in injuries:
        recommendations.append("Avoid aggressive knee-dominant movements and use controlled lower body variations.")
    if "shoulder" in injuries:
        recommendations.append("Avoid painful overhead work and prioritize stable pressing angles.")
    if "back" in injuries or "lower back" in injuries:
        recommendations.append("Avoid heavy spinal loading and prioritize supported pulling variations.")

    if bmi < 18.5:
        recommendations.append("Your BMI is on the low side. Prioritize adequate calories and resistance training.")
    elif bmi >= 25:
        recommendations.append("A moderate calorie deficit with consistent training would improve body composition.")

    recommendations.append("Sleep 7 to 9 hours daily for recovery and performance.")
    recommendations.append(f"Your daily water target is about {results.get('water')} liters.")
    recommendations.append("Review progress every 2 weeks and adjust calories only when needed.")

    return recommendations