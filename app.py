from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {"q": "What is 2 + 2?", "a": "4"},
    {"q": "Capital of India?", "a": "Delhi"},
    {"q": "What is 5 x 3?", "a": "15"}
]

@app.route("/")
def home():
    return render_template("index.html", questions=questions)

@app.route("/submit", methods=["POST"])
def submit():
    score = 0

    for i, q in enumerate(questions):
        ans = request.form.get(str(i))
        if ans and ans.lower() == q["a"].lower():
            score += 1

    return f"Your Score: {score}/{len(questions)}"

if __name__ == "__main__":
    app.run(debug=True)