from flask import Flask, render_template, url_for

app = Flask(__name__)

# Home route
@app.route('/')
def hello():
    return render_template('index.html')

# /page route for the "msg" function
@app.route('/page')
def msg():
    return "hello"

if __name__ == '__main__':
    app.run(debug=True)

