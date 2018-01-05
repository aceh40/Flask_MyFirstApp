from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aceh40user:pass@localhost/aceh40db'
db = SQLAlchemy(app)

from app import routes, models