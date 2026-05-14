def get_meal_templates(budget):
    budget = budget.lower()

    low = {
        "breakfast": [
            "3 eggs + oats + banana",
            "Foul + baladi bread + yogurt",
            "Cottage cheese + bread + cucumber"
        ],
        "lunch": [
            "Rice + chicken + vegetables",
            "Potatoes + eggs + salad",
            "Lentils + rice + yogurt"
        ],
        "dinner": [
            "Tuna + bread + salad",
            "Eggs + potatoes + cucumber",
            "Yogurt + oats + fruit"
        ],
        "snacks": [
            "Banana",
            "Peanuts",
            "Milk",
            "Dates"
        ]
    }

    medium = {
        "breakfast": [
            "Oats + milk + peanut butter + banana",
            "Eggs + toast + cheese + fruit",
            "Greek yogurt + oats + honey"
        ],
        "lunch": [
            "Chicken breast + rice + vegetables",
            "Lean beef + potatoes + salad",
            "Turkey sandwich + fruit"
        ],
        "dinner": [
            "Tuna pasta + salad",
            "Egg omelet + toast + yogurt",
            "Chicken sandwich + fruit"
        ],
        "snacks": [
            "Protein yogurt",
            "Fruit",
            "Nuts",
            "Milk"
        ]
    }

    high = {
        "breakfast": [
            "Greek yogurt + granola + berries + honey",
            "Omelet + avocado toast + orange juice",
            "Protein pancakes + peanut butter + banana"
        ],
        "lunch": [
            "Salmon + rice + vegetables",
            "Steak + sweet potato + salad",
            "Chicken bowl + avocado + quinoa"
        ],
        "dinner": [
            "Tuna wrap + salad + yogurt",
            "Chicken pasta + vegetables",
            "Egg whites + toast + cheese"
        ],
        "snacks": [
            "Protein bar",
            "Mixed nuts",
            "Fruit smoothie",
            "Greek yogurt"
        ]
    }

    if budget == "low":
        return low
    elif budget == "high":
        return high
    return medium


def get_meal_count(goal):
    goal = goal.lower()

    if goal == "muscle gain":
        return 5
    elif goal == "fat loss":
        return 4
    return 4


def get_goal_tips(goal):
    goal = goal.lower()

    if goal == "fat loss":
        return [
            "Keep protein high in every meal.",
            "Avoid liquid calories and excessive sugar.",
            "Use air-fried or grilled meals when possible."
        ]
    elif goal == "muscle gain":
        return [
            "Eat a protein source in every meal.",
            "Do not skip post-workout food.",
            "Increase calories gradually if weight is not going up."
        ]
    return [
        "Stay consistent with meal timing.",
        "Balance protein, carbs, and fats.",
        "Track body weight weekly."
    ]


def generate_meal_plan(goal, budget, calories, protein, carbs, fat):
    templates = get_meal_templates(budget)
    meal_count = get_meal_count(goal)
    tips = get_goal_tips(goal)

    plan = {
        "meal_count": meal_count,
        "calories": calories,
        "protein": protein,
        "carbs": carbs,
        "fat": fat,
        "breakfast": templates["breakfast"][0],
        "lunch": templates["lunch"][0],
        "dinner": templates["dinner"][0],
        "snack_1": templates["snacks"][0],
        "snack_2": templates["snacks"][1],
        "pre_workout": "Banana + coffee or toast + honey",
        "post_workout": "Protein meal with carbs like chicken + rice or eggs + bread",
        "tips": tips
    }

    return plan