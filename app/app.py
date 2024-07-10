import os
from flask import Flask, session, abort, redirect, request, render_template, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/liam/Downloads/uploads'
ALLOWED_EXTENSIONS = {'zip', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


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

@app.route('/seminar')
def seminar_redirect():
    return redirect("/projects/seminar")

@app.route('/projects/battery_business')
def battery_business():
    return render_template("battery_business.html", home="/")

@app.route('/projects/battery_business/zero')
def battery_business_zero():
    return render_template("zero.html", home="/")

@app.route('/projects/website')
def website():
    return render_template("website.html", home="/")

@app.route('/solar_car', methods = ['POST'])
def solar_car():
    data = request.form
    
    return 'a'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect("/upload")
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/github')
def github():
    return redirect("https://github.com/liamlivingston")

@app.route('/instagram')
def instagram():
    return redirect("https://www.instagram.com/liamklivingston")

@app.route('/test')
def test():
    return render_template("test.html", home="/")

if __name__ == "__main__":
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.run(debug=True, host='0.0.0.0', port='80')
