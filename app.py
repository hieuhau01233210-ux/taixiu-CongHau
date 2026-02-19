from flask import Flask, render_template, request, redirect
import random

app = Flask(__name__)

balance = 1000000

@app.route("/", methods=["GET", "POST"])
def index():
    global balance
    result = None
    dice = []
    total = 0

    if request.method == "POST":
        bet = int(request.form["bet"])
        choice = request.form["choice"]

        if bet > balance:
            return redirect("/")

        dice = [random.randint(1,6) for _ in range(3)]
        total = sum(dice)

        if (total >= 11 and choice == "tai") or (total <= 10 and choice == "xiu"):
            balance += bet
            result = "🎉 Bạn thắng!"
        else:
            balance -= bet
            result = "💀 Bạn thua!"

    return render_template("index.html",
                           balance=f"{balance:,}",
                           result=result,
                           dice=dice,
                           total=total)

if __name__ == "__main__":
    app.run(debug=True)
