from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')