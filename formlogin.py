from flask import Flask, render_template, request

app = Flask(__name__)

# Route to serve the login form
@app.route('/')
def home():
    return render_template('loginform.html')

# Route to handle form submission
@app.route('/formlogin', methods=['GET'])
def login():
    user_name = request.args.get('name')
    password = request.args.get('pass')
    if user_name == 'muqaddis' and password == '123':
        return f"Welcome {user_name}!"
    else:
        return "Try again."

if __name__ == '__main__':
    app.run(port=5001, debug=True)  # Specify port 5001
