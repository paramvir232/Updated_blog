from flask import Flask, render_template
import requests
from flask import request


app = Flask(__name__)
blog_response = requests.get('https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json')
blog_data = blog_response.json()

@app.route('/')
def home_page():
    return render_template('index.html',blog_data=blog_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact",methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return request.form['message']
    else:
        return render_template("contact.html")


@app.route('/post/<int:id>')
def post(id):
    curr_blog = None
    for blog in blog_data:
        if blog['id'] == id:
            curr_blog = blog

    return render_template('post.html',blog=curr_blog)

@app.route('/form')
def test_form():
    return render_template('testing_form.html')

@app.route('/login',methods=['GET', 'POST'])
def login():
        return f'<h1>Name: {request.form['username']}  Password: {request.form['password']}</h1>'



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')