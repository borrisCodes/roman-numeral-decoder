from flask import Flask, render_template, request
from main import romanToInt, rgenNumeral

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit_form():
    numerals = request.form['calc']
    return numerals
    
if __name__ == '__main__':
    app.run()