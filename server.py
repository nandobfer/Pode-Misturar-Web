from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)

# index page
@app.route('/', methods=['GET', 'POST'])
def index():
    # redirecting to another endpoint
    return redirect(url_for('home'))

# home page
@app.route('/home/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if 'client_panel' in request.form:
            telefone = request.form.get('telefone')
            password = request.form.get('password_client')
        
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")

""" flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) """
