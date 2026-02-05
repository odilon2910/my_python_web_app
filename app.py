from flask import Flask, render_template, request, redirect, url_for, session
import os


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', '1234567890')


# Utilisateur de démonstration (en production, utiliser une base de données)
UTILISATEUR_DEMO = {
    'username': 'etudiant',
    'password': 'edt2026'
}


@app.route('/')
def index():
    # Redirige vers la page de connexion si non authentifié
    if 'username' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('home'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Vérification simple (à remplacer par une vraie vérification)
        if username == UTILISATEUR_DEMO['username'] and password == UTILISATEUR_DEMO['password']:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            message = "Identifiants incorrects. Essayez à nouveau."
    return render_template('login.html', message=message)


@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('home.html', username=session['username'])


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000, debug=True)
