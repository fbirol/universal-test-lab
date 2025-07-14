from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simüle edilmiş kullanıcı - gerçek uygulamada DB olur
VALID_USERNAME = "furkan"
VALID_PASSWORD = "1234"

# Basit kayıtlar (DB olmadan RAMde)
records = [
    {"id": 1, "name": "Ali Veli", "email": "ali@example.com"},
    {"id": 2, "name": "Fatma Yılmaz", "email": "fatma@example.com"},
]

@app.route('/', methods=['GET'])
def home():
    # return render_template('home.html')

    # Artık istersen home'u hemen liste sayfasına yönlendirebilirsin
    return redirect(url_for('list_records'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            # return redirect(url_for('home'))
            return redirect(url_for('list_records'))    # login sonrası yeni sayfa
        else:
            error = "Kullanıcı adı veya şifre yanlış!"
    return render_template('login.html', error=error)

@app.route('/list', methods=['GET'])
def list_records():
    return render_template('list.html', records=records)


if __name__ == "__main__":
    app.run(debug=True)
    # app.run(debug=True, port=5001)    # Custom Port Number Setting
