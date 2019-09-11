#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='home')


## おまじない
if __name__ == "__main__":
    app.run(debug=True)
