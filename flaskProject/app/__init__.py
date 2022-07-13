from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db/car_model'

db = SQLAlchemy(app)

from app import views
from app import models

db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.0', threaded=True)
