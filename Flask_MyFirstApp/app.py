
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
#from config import Config


app = Flask (__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aceh40user:pass@localhost/aceh40db'
db = SQLAlchemy(app)
#   migrate = Migrate(app,db)



from app import routes, models

# =============================================================================
# Secret key:
# =============================================================================
app.secret_key = '\xa7\xf0o\xb8W\xb3\x03\x063\x08\n5\xc4I\x7f28\x1d-\xc9u\xcd\xf9\xd9'


# =============================================================================
# Run app:
# =============================================================================
if __name__ == '__main__':
    app.run(debug=True)






