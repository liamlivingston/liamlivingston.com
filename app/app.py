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

@app.route('/projects/kenya')
def kenya():
    return render_template("kenya.html", home="/")

@app.route('/projects/csp')
def csp():
    return render_template("csp.html", home="/")

@app.route('/projects/motor_rewinding')
def motor_rewinding():
    return render_template("rewinding.html", home="/")

@app.route('/projects/solar_car_v1')
def solar_car_v1():
    return render_template("solar_car_v1.html", home="/")

@app.route('/projects/solar_car_v2')
def solar_car_v2():
    return render_template("solar_car_v2.html", home="/")

@app.route('/projects/seminar')
def seminar():
    return render_template("seminar.html", home="/")

@app.route('/projects/battery_business')
def battery_business():
    return render_template("battery_business.html", home="/")

@app.route('/projects/battery_business/zero')
def battery_business_zero():
    return render_template("zero.html", home="/")

@app.route('/solar_car', methods = ['POST'])
def solar_car():
    data = request.form
    
    pass

@app.route('/github')
def github():
    return redirect("https://github.com/liamlivingston/liamlivingston.com")

@app.route('/instagram')
def instagram():
    return redirect("https://www.instagram.com/liamklivingston")

@app.route('/test')
def test():
    return render_template("test.html", home="/")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='80')