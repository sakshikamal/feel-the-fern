from flask_ngrok import run_with_ngrok
from flask import Flask, render_template

app=Flask(__name__)
run_with_ngrok(app)

@app.route('/')
def hello_world():
  return render_template('dashboard.html')

if __name__ == '__main__':
  app.run(debug=True)
