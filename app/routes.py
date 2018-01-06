
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask, render_template, request, flash, url_for, redirect, session, logging
from app.content_management import blogsFunction, sampleContent
from datetime import datetime
from passlib.hash import sha256_crypt
import gc
from app import app
from app import models
from .forms import RegistrationForm
from .db_connection import connection
from .queries import checkUserEmail, registerUser


blogs = blogsFunction()
topic_dict = sampleContent()
currentTime = datetime.now()

# =============================================================================
# Add routes:
# =============================================================================

@app.route('/')
def homePage():
    flash ("Flash Test!")
    flash ("Flash Test2!")
    flash ("Flash Test3!")
    return render_template('home.html')    

	
@app.route('/dashboard/')
def dashboardPage():
    flash ("you have successfully logged in")
    flash ("you have successfully logged in")
    flash ("you have successfully logged in")
    return render_template('dashboard.html')   	
	
	
@app.route('/programming/')
def programmingPage():
    return render_template("programming.html", topic_dict=topic_dict)


@app.route('/register/', methods=['GET', 'POST'])
def registerPage():
	try:
		cur, conn = connection()
		regForm = RegistrationForm(request.form)
		if request.method == "POST" and regForm.validate():
			firstName = regForm.firstName.data
			lastName = regForm.lastName.data
			email = regForm.email.data
			password = sha256_crypt.encrypt((str(regForm.password.data)))
			cur, conn = connection()
			q = checkUserEmail()
			x = 0 #cur.execute('SELECT * FROM public."User" WHERE email = %s', (email))
			if int(x)> 0:
				flash("This email address is already registered.")
				return render_template('register.html'
										, form=regForm)
			else:
				q = registerUser()
				activeFlag = True
				cur.execute('INSERT INTO public."User" (email, password_hash, "firstName", "lastName", "activeFlag") VALUES (%s, %s, %s, %s, %s)'				
							, (email, password, firstName, lastName, activeFlag))
				conn.commit()
				flash ("Thanks for registering")
				cur.close()
				conn.close()
				gc.collect() # garbage collector - good to collect after closing conn.

				session['logged in'] = True # to track that the user is logged in this session.
				session ['email'] = email
				return redirect (url_for('dashboardPage'))
		
		return render_template("register.html", form=regForm)
	
	except Exception as e:
		return (str(e))

## Above: When i change redirect to registerPage, I get redirected endlessly.
## How do I clear the data from the form?    

@app.route('/login/', methods=["GET","POST"])
def loginPage():
	error = ''
	try:
		if request.method == "POST":
			attempted_username = request.form['username']
			attempted_password = request.form['password']
			
			#flash (attempted_username)
			#flash (attempted_password)
			
			if attempted_username  == 'admin' and attempted_password == 'pass':
				return redirect(url_for('dashboardPage'))
			else:
				error = "Invalid credentials. Try again."
		
		return render_template("login.html", error=error)
	
	except Exception as e:
		#flash (e)
		return render_template('login.html', error=error)  


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
    return render_template ('error_404.html')

