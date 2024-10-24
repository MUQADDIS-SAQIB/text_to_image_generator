from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def registration():
    return render_template('form_task.html')


@app.route('/file_upload', methods=['POST'])
def file():
    if request.method == 'POST':
        # Getting the form data
        name = request.form.get("name")
        last_name=request.form.get("lastname")
        email = request.form.get("email")
        password = request.form.get("pass")
        country = request.form.get("country")
        city=request.form.get("city")
        phone=request.form.get("phone")
        address=request.form.get("address")
        position=request.form.get("position")
        info=request.form.get('info')
        if 'cv' not in request.files:
            return "no file selected"
        f=request.files['cv']
        if f.filename ==' ':
            return "no file is selected"
        f.save(f'static/images/{f.filename}')

        return "Successfully submitted"


if __name__ == '__main__':
    app.run(debug=True, port=5008)
