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
    intform = romanToInt(rnumeral)

    if intform != 'Invalid':
        integer = intform
        return render_template('index.html', integer=integer, roman_numeral=rnumeral, random_numeral=session['random_numeral'])
    
    invalid = 'Invalid'
    return render_template('index.html', invalid=invalid, roman_numeral=rnumeral, random_numeral=session['random_numeral'])

@app.route('/practice', methods=['POST'])
def practice():

    intGuess = int(request.form['guess'])
    correctAnswer = romanToInt(session['random_numeral'])

    if intGuess == correctAnswer:
        guess='Correct, try another one!'
        session['random_numeral'] = rgenNumeral()

    else:
        guess='Wrong, try again!'

    return render_template('index.html', guess=guess, random_numeral=session['random_numeral'])

@app.route('/regen', methods=['POST'])
def regen():
    session['random_numeral'] = rgenNumeral()
    return render_template('index.html', random_numeral=session['random_numeral'])
    
if __name__ == '__main__':
    app.run()