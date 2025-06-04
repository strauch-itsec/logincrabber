from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
import os

app = Flask(__name__)
data_file = 'data/users.json'

# Ensure the data directory exists
if not os.path.exists('data'):
    os.makedirs('data')

# Load existing user data
def load_users():
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            return json.load(f)
    return []

# Save user data
def save_user(username, password):
    users = load_users()
    users.append({'username': username, 'password': password})
    with open(data_file, 'w') as f:
        json.dump(users, f)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    save_user(username, password)
    return redirect(url_for('users'))

@app.route('/users')
def users():
    users = load_users()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)