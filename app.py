from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/rose")
def rose():
    return render_template("rose.html")

@app.route("/propose")
def propose():
    return render_template("propose.html")

@app.route("/chocolate")
def chocolate():
    return render_template("chocolate.html")

@app.route("/teddy")
def teddy():
    return render_template("teddy.html")

@app.route("/promise")
def promise():
    return render_template("promise.html")

@app.route("/hug")
def hug():
    return render_template("hug.html")

@app.route("/kiss")
def kiss():
    return render_template("kiss.html")

if __name__ == "__main__":
    app.run(debug=True)
