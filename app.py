
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def voting():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
