from flask import Flask, render_template, request, session, redirect, url_for, jsonify, send_file
from flask_socketio import SocketIO, emit, join_room, leave_room
import os

# Original Engine Imports
from engine.calculations import (
    calculate_bmi,
    bmi_category,
    calculate_bmr,
    calculate_tdee,
    calculate_target_calories,
    calculate_macros,
    calculate_water_intake,
)

from engine.workout_generator import generate_workout_plan
from engine.meal_generator import generate_meal_plan
from engine.chatbot import get_chatbot_reply
from engine.pdf_exporter import generate_pdf
from engine.recommendation import generate_recommendations

# Healthcare Engine
from engine.healthcare_service import HealthcareService


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "fitforge-dev-secret-key")

socketio = SocketIO(app, cors_allowed_origins="*")
health_service = HealthcareService()


# -----------------------------
# Global Template Variables
# -----------------------------

@app.context_processor
def inject_global_variables():
    return {
        "user": session.get("user", {"name": "Guest"}),
        "results": session.get("results"),
        "recommendations": session.get("recommendations"),
    }


# -----------------------------
# Helper Functions
# -----------------------------

def get_required_session_data():
    user = session.get("user")
    results = session.get("results")

    if not user or not results:
        return None

    return {
        "user": user,
        "results": results,
        "workout_plan": session.get("workout_plan"),
        "meal_plan": session.get("meal_plan"),
        "recommendations": session.get("recommendations"),
    }


def to_int(value, default=0):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def to_float(value, default=0.0):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


# -----------------------------
# Main Routes
# -----------------------------

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/assessment")
def assessment():
    return render_template("assessment.html")


@app.route("/generate-plan", methods=["POST"])
def generate_plan():
    data = request.form.to_dict()

    name = data.get("name", "User").strip()
    age = to_int(data.get("age"))
    gender = data.get("gender", "").strip()
    height = to_float(data.get("height"))
    weight = to_float(data.get("weight"))
    goal = data.get("goal", "").strip()
    experience = data.get("experience", "").strip()
    days = to_int(data.get("days"), 3)
    place = data.get("place", "").strip()
    budget = data.get("budget", "").strip()
    injuries = data.get("injuries", "").strip()
    activity = data.get("activity", "").strip()

    if not name:
        name = "User"

    if age <= 0 or height <= 0 or weight <= 0:
        return redirect(url_for("assessment"))

    bmi = calculate_bmi(weight, height)
    bmi_status = bmi_category(bmi)

    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity)
    target_calories = calculate_target_calories(tdee, goal)

    macros = calculate_macros(weight, target_calories, goal)
    water = calculate_water_intake(weight)

    user_data = {
        "name": name,
        "age": age,
        "gender": gender,
        "height": height,
        "weight": weight,
        "goal": goal,
        "experience": experience,
        "days": days,
        "place": place,
        "budget": budget,
        "injuries": injuries if injuries else "None",
        "activity": activity,
    }

    results = {
        "bmi": bmi,
        "bmi_status": bmi_status,
        "bmr": bmr,
        "tdee": tdee,
        "target_calories": target_calories,
        "protein": macros["protein"],
        "fat": macros["fat"],
        "carbs": macros["carbs"],
        "water": water,
    }

    workout_plan = generate_workout_plan(
        days,
        place,
        experience,
        injuries if injuries else "",
    )

    meal_plan = generate_meal_plan(
        goal,
        budget,
        target_calories,
        macros["protein"],
        macros["carbs"],
        macros["fat"],
    )

    recommendations = generate_recommendations(user_data, results)

    session["user"] = user_data
    session["results"] = results
    session["workout_plan"] = workout_plan
    session["meal_plan"] = meal_plan
    session["recommendations"] = recommendations

    return redirect(url_for("dashboard"))


@app.route("/dashboard")
def dashboard():
    page_data = get_required_session_data()

    if not page_data:
        return redirect(url_for("assessment"))

    return render_template(
        "dashboard.html",
        user=page_data["user"],
        results=page_data["results"],
        recommendations=page_data["recommendations"],
    )


@app.route("/workout")
def workout():
    page_data = get_required_session_data()

    if not page_data:
        return redirect(url_for("assessment"))

    return render_template(
        "workout.html",
        user=page_data["user"],
        results=page_data["results"],
        workout_plan=page_data["workout_plan"],
    )


@app.route("/nutrition")
def nutrition():
    page_data = get_required_session_data()

    if not page_data:
        return redirect(url_for("assessment"))

    return render_template(
        "nutrition.html",
        user=page_data["user"],
        results=page_data["results"],
        meal_plan=page_data["meal_plan"],
    )


@app.route("/progress")
def progress():
    page_data = get_required_session_data()

    if not page_data:
        return redirect(url_for("assessment"))

    return render_template(
        "progress.html",
        user=page_data["user"],
        results=page_data["results"],
        workout_plan=page_data["workout_plan"],
        meal_plan=page_data["meal_plan"],
        recommendations=page_data["recommendations"],
    )


@app.route("/chat")
def chat():
    current_user = session.get("user", {"name": "Guest"})
    current_results = session.get("results")

    return render_template(
        "chat.html",
        user=current_user,
        results=current_results,
    )


@app.route("/export-pdf")
def export_pdf():
    page_data = get_required_session_data()

    if not page_data:
        return redirect(url_for("assessment"))

    try:
        pdf_file = generate_pdf(
            page_data["user"],
            page_data["results"],
            page_data["workout_plan"],
            page_data["meal_plan"],
            page_data["recommendations"],
        )
    except TypeError:
        pdf_file = generate_pdf(
            page_data["user"],
            page_data["results"],
            page_data["workout_plan"],
            page_data["meal_plan"],
        )

    if isinstance(pdf_file, (str, os.PathLike)):
        if not os.path.exists(pdf_file):
            return "PDF file was not created.", 500

        return send_file(
            pdf_file,
            as_attachment=True,
            download_name="fitforge_plan.pdf",
        )

    return send_file(
        pdf_file,
        as_attachment=True,
        download_name="fitforge_plan.pdf",
    )


# -----------------------------
# Healthcare Routes
# -----------------------------

@app.route("/healthcare")
def healthcare():
    doctors = health_service.get_heliopolis_doctors()

    return render_template(
        "healthcare.html",
        doctors=doctors,
    )


@app.route("/api/medicine/search")
def search_meds():
    query = request.args.get("q", "").strip()

    if not query:
        return jsonify([])

    medicines = health_service.search_medicine(query)
    return jsonify(medicines)


@app.route("/live-chat")
def live_chat():
    room = request.args.get("room", "General")

    return render_template(
        "live_chat.html",
        room=room,
    )


# -----------------------------
# AI Chatbot API
# -----------------------------

@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "").strip()

    if not message:
        return jsonify({"reply": "Please enter a message."})

    reply = get_chatbot_reply(message)
    return jsonify({"reply": reply})


# -----------------------------
# Socket.IO Live Chat Logic
# -----------------------------

@socketio.on("join")
def on_join(data):
    room = data.get("room", "General")
    join_room(room)

    emit(
        "message",
        f"System: A user has joined {room}.",
        room=room,
    )


@socketio.on("leave")
def on_leave(data):
    room = data.get("room", "General")
    leave_room(room)

    emit(
        "message",
        f"System: A user has left {room}.",
        room=room,
    )


@socketio.on("private_message")
def handle_private_message(data):
    room = data.get("room", "General")
    msg = data.get("message", "").strip()

    if msg:
        emit("message", msg, room=room)


# -----------------------------
# Error Pages
# -----------------------------

@app.errorhandler(404)
def page_not_found(error):
    return render_template("home.html"), 404


@app.errorhandler(500)
def internal_server_error(error):
    return "Internal Server Error. Check the terminal for details.", 500


# -----------------------------
# Run App
# -----------------------------

if __name__ == "__main__":
    socketio.run(
        app,
        host="127.0.0.1",
        port=5000,
        debug=True,
        allow_unsafe_werkzeug=True,
    )
