from flask import Flask, render_template, request, session
from main import romanToInt, rgenNumeral
import os

app = Flask(__name__)
app.secret_key = '23'

@app.route('/')
def start():

    session['random_numeral'] = rgenNumeral()
    
    return render_template('index.html', random_numeral=session['random_numeral'])

@app.route('/decode', methods=['POST'])
def decode():

    rnumeral = request.form['calc']
    integer = romanToInt(rnumeral)

    return render_template('index.html', integer=integer, roman_numeral=rnumeral, random_numeral=session['random_numeral'])

@app.route('/practice', methods=['POST'])
def practice():

    intGuess = int(request.form['guess'])
    correctAnswer = romanToInt(session['random_numeral'])

    if intGuess == correctAnswer:
        guess='Correct!'
        session['random_numeral'] = rgenNumeral()

    else:
        guess='Wrong!'

    return render_template('index.html', guess=guess, random_numeral=session['random_numeral'])

    
if __name__ == '__main__':
    app.run()