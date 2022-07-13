from app import db
from sqlalchemy import Integer, String, Column


class Car_data(db.Model):
    objectid = Column(String(100), primary_key=True)
    year = Column(Integer)
    make = Column(String(100))
    model = Column(String(100))
    category = Column(String(100))
    createdat = Column(String(100))
    updatedat = Column(String(100))

    __tablename__ = "car_data"

    def __init__(self, objectid, year, make, model, category, createdat, updatedat):
        self.objectid = objectid
        self.year = year
        self.make = make
        self.model = model
        self.category = category
        self.createdat = createdat
        self.updatedat = updatedat

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def dictionary(self):
        return {
            'objectid': self.objectid,
            'year': self.year,
            'make': self.make,
            'model': self.model,
            'category': self.category,
            'createdat': self.createdat,
            'updatedat': self.updatedat
        }


class User_data(db.Model):
    user = Column(String(100), primary_key=True)
    email = Column(String(100))
    fname = Column(String(100))
    lname = Column(String(100))
    password = Column(String(100))

    __tablename__ = "user_data"

    def __init__(self, user, email, password, fname, lname):
        self.lname = lname
        self.fname = fname
        self.password = password
        self.email = email
        self.user = user

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
