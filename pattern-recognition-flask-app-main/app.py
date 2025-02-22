from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Define 15 pattern recognition questions
questions = [
    {"question": "Select the next pattern in the sequence:", "sequence": ["⬛", "⚫", "⬛", "?"], "options": {"square": "⬛ Square", "circle": "⚫ Circle"}, "answer": "circle"},
    {"question": "Which shape comes next?", "sequence": ["🔺", "🔵", "🔺", "?"], "options": {"triangle": "🔺 Triangle", "circle": "🔵 Circle"}, "answer": "circle"},
    {"question": "Pick the correct pattern:", "sequence": ["🟢", "🟡", "🟢", "?"], "options": {"green": "🟢 Green", "yellow": "🟡 Yellow"}, "answer": "yellow"},
    {"question": "What comes next?", "sequence": ["🟥", "🟨", "🟥", "?"], "options": {"red": "🟥 Red", "yellow": "🟨 Yellow"}, "answer": "yellow"},
    {"question": "Identify the pattern:", "sequence": ["🔶", "🔷", "🔶", "?"], "options": {"diamond": "🔷 Diamond", "hexagon": "🔶 Hexagon"}, "answer": "diamond"},
    {"question": "Next shape?", "sequence": ["🔵", "🔴", "🔵", "?"], "options": {"blue": "🔵 Blue", "red": "🔴 Red"}, "answer": "red"},
    {"question": "Complete the sequence:", "sequence": ["⬜", "⬛", "⬜", "?"], "options": {"white": "⬜ White", "black": "⬛ Black"}, "answer": "black"},
    {"question": "What follows?", "sequence": ["🟧", "🟦", "🟧", "?"], "options": {"orange": "🟧 Orange", "blue": "🟦 Blue"}, "answer": "blue"},
    {"question": "Guess the missing shape:", "sequence": ["🟠", "🟣", "🟠", "?"], "options": {"purple": "🟣 Purple", "orange": "🟠 Orange"}, "answer": "purple"},
    {"question": "Find the next pattern:", "sequence": ["⬜", "⬛", "⬛", "⬜", "⬜", "?"], "options": {"black": "⬛ Black", "white": "⬜ White"}, "answer": "black"},
    {"question": "What is the missing shape?", "sequence": ["🔺", "🔻", "🔺", "?"], "options": {"up": "🔺 Up Triangle", "down": "🔻 Down Triangle"}, "answer": "down"},
    {"question": "Choose the correct pattern:", "sequence": ["🟥", "🟩", "🟦", "?"], "options": {"blue": "🟦 Blue", "green": "🟩 Green"}, "answer": "green"},
    {"question": "Complete the set:", "sequence": ["🟤", "⚪", "🟤", "?"], "options": {"white": "⚪ White", "brown": "🟤 Brown"}, "answer": "white"},
    {"question": "Identify the missing pattern:", "sequence": ["🟪", "🟨", "🟪", "?"], "options": {"yellow": "🟨 Yellow", "purple": "🟪 Purple"}, "answer": "yellow"},
    {"question": "Which shape continues the pattern?", "sequence": ["🟢", "🟠", "🟢", "?"], "options": {"green": "🟢 Green", "orange": "🟠 Orange"}, "answer": "orange"}
]


@app.route("/")
def index():
    selected_questions = random.sample(questions, 1)   #Add the required quesrions to be displayed
    return render_template("index.html", questions=list(enumerate(selected_questions)))

@app.route("/result", methods=["POST"])
def result():
    score = 0
    total = len(request.form) // 2
    user_answers = []
    
    for i in range(total):
        user_answer = request.form.get(f"answer_{i}")
        correct_answer = request.form.get(f"correct_{i}")
        user_answers.append((user_answer, correct_answer))
        if user_answer == correct_answer:
            score += 1

    return render_template("result.html", score=score, total=total, user_answers=user_answers)

if __name__ == "__main__":
    app.run(debug=True)
