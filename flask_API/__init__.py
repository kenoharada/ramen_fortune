from flask import Flask
from  flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('ramen.config')

db = SQLAlchemy(app)

import ramen.views
