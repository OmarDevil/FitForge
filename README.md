# FitForge

FitForge is a Flask-based web application that helps gym users generate a personalized fitness plan based on their body data, goals, experience level, workout place, injuries, and food budget.

## Features

- User assessment form
- BMI, BMR, TDEE, calories, macros, and water intake calculation
- Smart dashboard with analysis results
- Workout plan generator
- Home workout / gym workout support
- Injury-aware exercise filtering
- Nutrition plan generator based on budget and goal
- Progress tracker with chart using localStorage
- Chat assistant for common fitness questions
- PDF export for the full plan
- Smart recommendations section
- Session-based navigation without login or database

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Chart.js
- ReportLab

## Project Structure

fitforge/
- app.py
- requirements.txt
- README.md
- engine/
- templates/
- static/
- exports/

## How to Run

1. Create virtual environment:
   `python -m venv venv`

2. Activate environment on Windows:
   `venv\Scripts\activate`

3. Install dependencies:
   `pip install -r requirements.txt`

4. Optional: set a production session secret:
   `set SECRET_KEY=your-secret-key`

5. Run the app:
   `python app.py`

6. Open in browser:
   `http://127.0.0.1:5000`

## Main Pages

- Home
- Assessment
- Dashboard
- Workout Plan
- Nutrition Plan
- Progress Tracker
- Chat Assistant

## Notes

- Healthcare search uses a local SQLite database generated automatically at runtime.
- User plan data is stored in session during runtime.
- Progress tracker data is stored in browser localStorage.
- PDF files are generated inside the exports folder.

## Author

Developed as a smart fitness assistant web project using Flask.
