from flask import Flask, render_template
import requests
from flask import request
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()


app = Flask(__name__)
blog_response = requests.get('https://gist.githubusercontent.com/gellowg/389b1e4d6ff8effac71badff67e4d388/raw/fc31e41f8e1a6b713eafb9859f3f7e335939d518/data.json')
blog_data = blog_response.json()

my_google_email = os.getenv('my_google_email')
google_password = os.getenv('google_password')

@app.route('/')
def home_page():
    return render_template('index.html',blog_data=blog_data)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact",methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone_number = request.form['number']
        message = request.form['message']

        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_google_email, password=google_password)
            connection.sendmail(from_addr=my_google_email, to_addrs=my_google_email,
                                msg=f'Subject:User Message !!\n\n Name: {name}\nEmail: {email}\nPhone Number: {phone_number}\nMessage: {message}')

        return  render_template("contact.html",msg=request.form['message'])

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