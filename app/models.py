
"""
Spyder Editor

This is a temporary script file.
"""
from datetime import datetime
from app import db




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
    registeredDate = db.Column(db.DateTime(timezone=False), index=True, default=datetime.utcnow)
    
#    def __init__(self,email, firstName, lastName, registeredDate=datetime.now()):
#        self.email = email
#        self.firstName = firstName
#        self.lastName = lastName
#        self.registeredDate = registeredDate

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
    registeredDate = db.Column(db.DateTime(timezone=False))
    userActivities = db.relationship("ActivityLog")
    
#    def __init__(self,email):
#        self.email = email
        
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
    
#    def __init__(self,activityName):
#        self.activityName = activityName
        
    def __repr__(self):
        return '<ActivityType: %r>' % self.activityName


class ActivityLog(db.Model):
    __tablename__ = 'ActivityLog'
    activityLogId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('User.userId'))
    activityTypeId = db.Column(db.Integer, db.ForeignKey('ActivityType.activityTypeId'))
    effectiveDate = db.Column(db.DateTime (timezone=False), index=True, default=datetime.now)
    numerical = db.Column(db.Float(precision=6))
    notes = db.Column(db.String(1000))
    completed = db.Column(db.Boolean)
    
#    def __init__(self,activityName):
#        self.activityName = activityName
#        
    def __repr__(self):
        return '<ActivityLog: userId: %r, activityTypeId: %r, effectiveDate: %r>' % self.activityName, self.activityTypeId, self.effectiveDate







