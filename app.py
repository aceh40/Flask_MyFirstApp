
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
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aceh40user:pass@localhost/aceh40db'
db = SQLAlchemy(app)

blogs = blogsFunction()
topic_dict = sampleContent()
currentTime = datetime.now()

# =============================================================================
# Create database models:
# =============================================================================

## sample table:
class Users(db.Model):
    __tablename__ = '_users'
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


class User(db.Model):
    __tablename__ = 'User'
    userId = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), index=True, unique=True)
    password_hash = db.Column(db.String(200))
    firstName = db.Column(db.String(50), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    activeFlag = db.Column(db.Boolean)
    registeredDate = db.Column(db.DateTime(timezone=True))
    userActivities = db.relationship("ActivityLog")
    
    def __init__(self,email):
        self.email = email
        
    def __repr__(self):
        return '<User: %r>' % self.email


class ActivityType(db.Model):
    __tablename__ = 'ActivityType'
    activityTypeId = db.Column(db.Integer, primary_key=True)
    activityName = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    activeFlag = db.Column(db.Boolean)
    isHabit = db.Column(db.Boolean)
    activityLogs = db.relationship("ActivityLog")
    
    def __init__(self,activityName):
        self.activityName = activityName
        
    def __repr__(self):
        return '<ActivityType: %r>' % self.activityName


class ActivityLog(db.Model):
    __tablename__ = 'ActivityLog'
    activityLogId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('User.userId'))
    activityTypeId = db.Column(db.Integer
                               , db.ForeignKey('ActivityType.activityTypeId'))
    effectiveDate = db.Column(db.DateTime(timezone=True))
    numerical = db.Column(db.Float(precision=6))
    notes = db.Column(db.String(1000))
    completed = db.Column(db.Boolean)
    
#    def __init__(self,activityName):
#        self.activityName = activityName
#        
    def __repr__(self):
        return '<ActivityLog: userId: %r, activityTypeId: %r, effectiveDate: %r>' % self.activityName, self.activityTypeId, self.effectiveDate

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
        if emailCheck is None:
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


# =============================================================================
# Secret key:
# =============================================================================
app.secret_key = '\xa7\xf0o\xb8W\xb3\x03\x063\x08\n5\xc4I\x7f28\x1d-\xc9u\xcd\xf9\xd9'


# =============================================================================
# Run app:
# =============================================================================
if __name__ == '__main__':
    app.run(debug=True)






