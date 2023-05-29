from flask import Flask, session, abort, redirect, request, render_template

app = Flask("liamlivingston")

@app.route('/')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')