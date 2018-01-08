
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
from .queries import checkUserEmail, registerUser, checkLoginEmail


blogs = blogsFunction()
topic_dict = sampleContent()
currentTime = datetime.now()

# =============================================================================
# Add routes:
# =============================================================================

@app.route('/')
@app.route('/home/')
def homePage():
    flash ("Flash Test!")
    flash ("Flash Test2!")
    flash ("Flash Test3!")
    return render_template('home.html')    

	
@app.route('/dashboard/')
def dashboardPage():
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
			cur.execute(q, (email,))
			x = cur.fetchone()
			if x[0] > 0:
				flash("This email address is already registered.")
				return render_template('register.html'
										, form=regForm)
			else:
				q = registerUser()
				activeFlag = True
				n = datetime.utcnow()
				cur.execute(q, (email, password, firstName, lastName, activeFlag))
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
		cur, conn = connection()
		if request.method == "POST":
			email = request.form['email']
			qe = checkUserEmail()
			cur.execute(qe, (email,))
			x = cur.fetchone()
			if x[0] == 0:
				error = "Invalid credentials. Please try again"
				#gc.collect()
				flash("Wrong email address")
			else:
				qp = checkLoginEmail()
				cur.execute (qp, (email,))
				passwd = cur.fetchone()[1]
			
				if sha256_crypt.verify(request.form['password'], passwd):
					session['logged in'] = True
					session['email'] = request.form['email']
					flash ("You have successfully signed in!!!!!!")
					gc.collect()
					return redirect(url_for("dashboardPage"))
				else:
					error = "Invalid credentials. Please try again"
					flash("Password is wrong")
					gc.collect()
					return render_template("login.html", error=error)
			gc.collect()
			return render_template("login.html", error=error) 
		else:
			gc.collect()
			return render_template("login.html", error=error)
	except Exception as e:
		flash(e)
		gc.collect()
		return render_template("login.html", error=error)




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

