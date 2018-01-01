
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request, flash, url_for, redirect, session, logging
from flask_sqlalchemy import SQLAlchemy
from content_management import blogsFunction, sampleContent
from datetime import datetime
#import psycopg2

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aceh40user:pass@localhost/aceh40db'
db = SQLAlchemy(app)

blogs = blogsFunction()
topic_dict = sampleContent()
currentTime = datetime.now()

## Create database model:
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    registeredDate = db.Column(db.DateTime)
    
    def __init__(self,email, firstName, lastName, registeredDate=datetime.now()):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.registeredDate = registeredDate
        
#        registeredDate=datetime.now()
    def __repr__(self):
        return '<E-mail %r>' % self.email

@app.route('/')
def homePage():
    return render_template('home.html')    

@app.route('/programming/')
def programmingPage():
    return render_template("programming.html", topic_dict=topic_dict)


@app.route('/register/', methods=['GET', 'POST'])
def registerPage():
    message =''
    user = ''
    if request.method == 'POST' and 'email' in request.form:
        emailInput = request.form.get('email')
        firstNameInput = request.form.get('firstName')
        lastNameInput = request.form.get('lastName')
        emailCheck = User.query.filter_by(email=emailInput).all()
        if emailCheck is None:
            user = User(emailInput,firstNameInput,lastNameInput)
            db.session.add(user)
            db.session.commit()
            message = 'You have successfully regierered.'
            return render_template ('register.html', message=message)
        else:
            message = 'This email has already been registered'
            return render_template ('register.html', message=message)        

    else:
        message = 'You need to register to use the site.'
        return render_template ('register.html', message=message)
       ## This needs to be fixed. 


## Above: When i change redirect to registerPage, I get redirected endlessly.
## How do I clear the data from the form?    

@app.route('/blog/')
def blogPage():
    return render_template('blog.html'
                           , blogs=blogs)  

""" Route to individual blog posts. Use 'id' as dynamic value. Enter 'id' as 
    argument in the blogPostPage function.
"""
@app.route('/blog/<string:id>/')
def blogPostPage(id):
    return render_template('blogpost.html'
                           , id=id) 


@app.route('/about/')
def aboutPage():
    return render_template('about.html')   

@app.errorhandler(404)
def error404(e):
    return render_template ('error404.html')

if __name__ == '__main__':
    app.run(debug=True)






