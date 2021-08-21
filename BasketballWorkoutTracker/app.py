from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/workouts')
def workouts():
    return render_template("workouts.html")


@app.route('/history')
def history():
    return render_template("history.html")


if __name__ == "__main__":
    app.run(debug=True)
