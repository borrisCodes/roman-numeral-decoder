from flask import Flask, render_template, request
from main import romanToInt, rgenNumeral

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def start():
    if request.method == 'POST':
        rnumeral = request.form['calc']
        integer = romanToInt(rnumeral)
        return render_template('index.html', integer=integer)
    
    return render_template('index.html')


    
if __name__ == '__main__':
    app.run()