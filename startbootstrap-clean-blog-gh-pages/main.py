from flask import Flask, render_template
import requests


app = Flask(__name__)
blog_response = requests.get('https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json')
blog_data = blog_response.json()

@app.route('/')
def home_page():
    return render_template('index.html',blog_data=blog_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')