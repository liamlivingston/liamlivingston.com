from flask import Flask, session, abort, redirect, request, render_template

app = Flask("liamlivingston")

@app.route('/')
def home():
    return render_template("home.html", home="/")

@app.route('/projects')
def projects():
    return render_template("projects.html", home="/")

@app.route('/projects/ebike_v1')
def ebike_v1():
    return render_template("ebike_v1.html", home="/")

@app.route('/projects/ebike_v2')
def ebike_v2():
    return render_template("ebike_v2.html", home="/")

@app.route('/projects/ebike_v3')
def ebike_v3():
    return render_template("ebike_v3.html", home="/")

@app.route('/projects/batteries')
def batteries():
    return render_template("batteries.html", home="/")


@app.route('/github')
def github():
    return redirect("https://github.com/liamlivingston/liamlivingston.com")

@app.route('/instagram')
def instagram():
    return redirect("https://www.instagram.com/liamklivingston")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')