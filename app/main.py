from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simüle edilmiş kullanıcı - gerçek uygulamada DB olur
VALID_USERNAME = "furkan"
VALID_PASSWORD = "1234"

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            return redirect(url_for('home'))
        else:
            error = "Kullanıcı adı veya şifre yanlış!"
    return render_template('login.html', error=error)

if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, port=5001)    # Custom Port Number Setting
