from flask import Flask, render_template, request

app=Flask (__name__)
@app.route('/')
def registration():
    return render_template('file_detch.html')
@app.route('/success', methods=['POST'])
def data():
    if request.method == 'POST':
        f=request.files['file']
        f.save(f'static/images/{f.filename}')

        return "success"



app.run(debug=True,port=5007)