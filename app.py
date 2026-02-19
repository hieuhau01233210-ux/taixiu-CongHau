from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "taixiu_secret_key"

@app.route("/", methods=["GET", "POST"])
def index():

    if "balance" not in session:
        session["balance"] = 1000000

    result = None
    dice = []
    total = 0

    if request.method == "POST":
        bet = int(request.form["bet"])
        choice = request.form["choice"]

        if bet > session["balance"]:
            return redirect("/")

        dice = [random.randint(1,6) for _ in range(3)]
        total = sum(dice)

        if (total >= 11 and choice == "tai") or (total <= 10 and choice == "xiu"):
            session["balance"] += bet
            result = "🎉 Bạn thắng!"
        else:
            session["balance"] -= bet
            result = "💀 Bạn thua!"

    return render_template("index.html",
                           balance=f"{session['balance']:,}",
                           result=result,
                           dice=dice,
                           total=total)

if __name__ == "__main__":
    app.run(debug=True)
