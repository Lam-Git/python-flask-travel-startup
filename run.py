from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/destination")
def destination():
    return render_template("destination.html")


@app.route("/specials")
def specials():
    return render_template("specials.html")


@app.route("/reservation")
def reservation():
    return render_template("reservation.html")


if __name__ == "__main__":
    app.run(debug=True)
