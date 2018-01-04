
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request, flash, url_for, redirect, session, logging
from content_management import blogsFunction, sampleContent
from datetime import datetime
from app import app
from app.forms import LoginForm


blogs = blogsFunction()
topic_dict = sampleContent()
currentTime = datetime.now()

# =============================================================================
# Add routes:
# =============================================================================

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
        emailCheck = Users.query.filter_by(email=emailInput).all()
        if emailCheck is None:s
            user = Users(emailInput,firstNameInput,lastNameInput)
            db.session.add(user)
            db.session.commit()
            message = 'You have successfully regierered.'
        else:
            message = 'This email has already been registered'
    else:
        message = 'You need to register to use the site.'
        ## This needs to be fixed. 
    flash(message) # use the layout.html template to flash messages. 
    return render_template ('register.html', mymessage=message)

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

