from flask_ngrok import run_with_ngrok
from flask import Flask, render_template

app=Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def display_dashboard():
  return render_template('dashboard.html')

@app.route('/user')
def display_user():
  return render_template('user.html')

@app.route('/appointments')
def display_appointment():
  return render_template('tables.html')

@app.route('/map')
def display_user():
  return render_template('maps.html')

@app.route('/notifications')
def display_notifications():
  return render_template('notifications.html')

if __name__ == '__main__':
  app.run(debug=True)
