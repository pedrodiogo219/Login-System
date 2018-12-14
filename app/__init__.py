from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db',  MigrateCommand)

lm = LoginManager()
lm.init_app(app)

engine = create_engine('postgresql://postgres:postgres@localhost:5432', echo=True)
conn = engine.connect()
session = sessionmaker(bind=engine)()
from app.models import tables

from app.controllers import default

from app.controllers.functions import shufflecards
app.jinja_env.globals.update(shufflecards=shufflecards)
