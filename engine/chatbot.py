def get_chatbot_reply(message):
    text = message.strip().lower()

    if not text:
        return "Please type your question."

    rules = [
        {
            "keywords": ["pre workout", "before workout", "قبل التمرين"],
            "reply": "Eat a light meal 60 to 90 minutes before training. A good option is banana with coffee, or toast with honey and yogurt."
        },
        {
            "keywords": ["post workout", "after workout", "بعد التمرين"],
            "reply": "Eat protein with carbs after training. Good examples: chicken with rice, eggs with bread, or yogurt with oats."
        },
        {
            "keywords": ["water", "hydration", "مية", "مياه", "hydrated"],
            "reply": "Drink water through the whole day, not only during training. A simple target is around 35 ml per kg of body weight daily."
        },
        {
            "keywords": ["sleep", "recovery", "النوم", "الاستشفاء"],
            "reply": "Sleep 7 to 9 hours daily. Recovery quality affects muscle gain, fat loss, and training performance."
        },
        {
            "keywords": ["protein", "بروتين"],
            "reply": "Protein should be spread across the day. Main food sources: eggs, chicken, tuna, yogurt, cottage cheese, lean beef, and legumes."
        },
        {
            "keywords": ["fat loss", "lose weight", "weight loss", "خس", "تخسيس", "تنشيف"],
            "reply": "For fat loss, keep calories below maintenance, maintain high protein, train consistently, and track body weight weekly."
        },
        {
            "keywords": ["muscle gain", "bulk", "gain muscle", "زيادة عضل", "تضخيم"],
            "reply": "For muscle gain, eat slightly above maintenance, keep protein high, train with progression, and monitor weight changes weekly."
        },
        {
            "keywords": ["plateau", "stuck", "ثبات", "واقف"],
            "reply": "If progress stops, first check consistency. Then adjust calories slightly, improve sleep, and review training intensity."
        },
        {
            "keywords": ["squat replacement", "replace squat", "بديل squat", "بديل السكوات"],
            "reply": "Possible squat alternatives: leg press, goblet squat, split squat, glute bridge, or wall sit depending on equipment and injuries."
        },
        {
            "keywords": ["deadlift replacement", "replace deadlift", "بديل الديدليفت", "بديل deadlift"],
            "reply": "Possible deadlift alternatives: Romanian deadlift with lighter load, hip thrust, hamstring curl, glute bridge, or cable pull-through."
        },
        {
            "keywords": ["shoulder pain", "knee pain", "back pain", "pain", "وجع", "الم", "إصابة"],
            "reply": "Do not force painful movements. Reduce load, avoid aggravating exercises, and switch to controlled alternatives. Severe or persistent pain should be checked by a qualified professional."
        },
        {
            "keywords": ["how many days", "days per week", "كام يوم", "عدد الأيام"],
            "reply": "Beginners usually do well with 3 to 4 training days weekly. Consistency is more important than adding random extra days."
        },
        {
            "keywords": ["cardio", "كارديو"],
            "reply": "Use cardio as support, not as the main strategy. For fat loss, 2 to 4 sessions weekly is usually enough depending on your total activity."
        },
        {
            "keywords": ["hello", "hi", "hey", "السلام", "اهلا", "مرحبا"],
            "reply": "Ask about workout, nutrition, recovery, fat loss, muscle gain, or exercise replacement."
        }
    ]

    for rule in rules:
        for keyword in rule["keywords"]:
            if keyword in text:
                return rule["reply"]

    return "I can help with workout, nutrition, sleep, water intake, fat loss, muscle gain, recovery, cardio, and exercise replacements."