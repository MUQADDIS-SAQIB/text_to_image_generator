from flask import Flask, render_template, request

app=Flask (__name__)
@app.route('/')
def registration():
    return render_template('formfetch.html')
@app.route('/get_data',methods=['POST'])
def data():
    result=request.form
    return render_template('result.html',result=result)
app.run(debug=True,port=5005)
