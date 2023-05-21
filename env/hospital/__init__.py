import os
from flask import Flask
import uuid
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.secret_key = str(uuid.uuid4())
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#         'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
app.app_context().push()
from hospital import routes