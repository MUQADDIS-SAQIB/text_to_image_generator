from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    dic={'math':80,'phy':20,'chem':100}
    return render_template('msg.html',result=dic)

@app.route('/<int:score>')
def route(score):
    return render_template('msg.html', name=score)

if __name__ == '__main__':
    app.run(debug=True, port=5004)
