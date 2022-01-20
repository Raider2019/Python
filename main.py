from app import app
from flask_sqlalchemy import SQLAlchemy
from models import User
db = SQLAlchemy(app)
if  __name__ == "__main__":
        app.run()