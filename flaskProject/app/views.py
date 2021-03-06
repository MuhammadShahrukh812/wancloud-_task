from app.models import User_data, Car_data
from flask_jsonschema import validate
import urllib
import requests
from app import app, db
from app.schema_validation import *
import json
from flask import request
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


def updateandget(model_list, db):
    for record in model_list:
        db_cardata = db.session.query(Car_data).filter_by(objectid=record['objectId']).first()
        if not db_cardata:
            adddata = Car_data(record['objectId'], record['Year'], record['Make'], record['Model'],
                               record['Category'], record['createdAt'], record['updatedAt'])
            adddata.create()


@app.route('/signup', methods=['POST'])
@validate(signup_validate)
def signup():  # put application's code here
    if request.method == 'POST':
        data = request.get_json()
        email = data['email']
        username = data['username']
        password = data['password']
        lname = data['lname']
        fname = data['fname']
        if db.session.query(User_data).filter_by(user=username).first():
            return 'Username already exists'
        missingg = db.session.query(User_data).filter_by(email=email).first()
        if missingg is not None:
            return "email already has an account!!"
        encrypted_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        adddata = User_data(username, email, encrypted_pw, lname, fname)
        adddata.create()
    return 'Id created'


@app.route('/signin', methods=['POST'])
@validate(login_validate)
def signin():
    data = request.get_json()
    email = data['email']
    password = data['password']
    userdata = db.session.query(User_data).filter_by(email=email).first()
    if not userdata:
        return 'invalid email'
    pswd_hash = db.session.query(User_data).filter_by(email=email).first().password
    if pswd_hash:
        if not bcrypt.check_password_hash(pswd_hash, password):
            print(pswd_hash)
            return 'Invalid password!!'
    return f'welcome {userdata.user}'


@app.route('/make/search', methods=['POST'])
def search():
    data = request.get_json()
    objid = data['Make']
    db_data = db.session.query(Car_data).filter_by(make=objid).paginate(1, 2, False, 40)
    print(db_data)
    if not db_data:
        return "not such make found"
    items = {"items": [dbdata.dictionary() for dbdata in db_data.items],
             "previous": db_data.prev_num if db_data.has_prev else None,
             "next": db_data.next_num if db_data.has_next else None,
             "pages": db_data.pages
             }
    return items


@app.route('/year/search', methods=['POST'])
def search():
    data = request.get_json()
    objid = data['year']
    db_data = db.session.query(Car_data).filter_by(year=objid).paginate(1, 2, False, 40)
    print(db_data)
    if not db_data:
        return "not such make found"
    items = {"items": [dbdata.dictionary() for dbdata in db_data.items],
             "previous": db_data.prev_num if db_data.has_prev else None,
             "next": db_data.next_num if db_data.has_next else None,
             "pages": db_data.pages
             }
    return items


@app.route('/model/search', methods=['POST'])
def search():
    data = request.get_json()
    objid = data['model']
    db_data = db.session.query(Car_data).filter_by(model=objid).paginate(1, 2, False, 40)
    print(db_data)
    if not db_data:
        return "not such make found"
    items = {"items": [dbdata.dictionary() for dbdata in db_data.items],
             "previous": db_data.prev_num if db_data.has_prev else None,
             "next": db_data.next_num if db_data.has_next else None,
             "pages": db_data.pages
             }
    return items


@app.route('/category/search', methods=['POST'])
def search():
    data = request.get_json()
    objid = data['category']
    db_data = db.session.query(Car_data).filter_by(category=objid).paginate(1, 2, False, 40)
    print(db_data)
    if not db_data:
        return "not such make found"
    items = {"items": [dbdata.dictionary() for dbdata in db_data.items],
             "previous": db_data.prev_num if db_data.has_prev else None,
             "next": db_data.next_num if db_data.has_next else None,
             "pages": db_data.pages
             }
    return items


@app.route('/updatetable', methods=['GET'])
def getdata():
    where = urllib.parse.quote_plus("""
    {
        "Year": {
            "$lt": 2032
        }
    }
    """)
    url = 'https://parseapi.back4app.com/classes/Car_Model_List?limit=10'
    headers = {
        'X-Parse-Application-Id': 'hlhoNKjOvEhqzcVAJ1lxjicJLZNVv36GdbboZj3Z',  # This is the fake app's application id
        'X-Parse-Master-Key': 'SNMJJF0CZZhTPhLDIqGhTlUNV9r60M2Z5spyWfXW'  # This is the fake app's readonly master key
    }
    response = json.loads(
        requests.get(url, headers=headers).content.decode('utf-8'))  # Here you have the data that you need
    list_models = []
    records = None
    for data in response['results']:
        if data.get('Make') not in list_models:
            list_models.append(data.get('Make'))
            url = 'https://parseapi.back4app.com/classes/Car_Model_List_{}?limit=10&order=Year&where=%s'.\
                format(data.get("Make"))
            url = url % where
            records = json.loads(
                requests.get(url, headers=headers).content.decode('utf-8'))  # Here you have the data that you need
            updateandget(records['results'], db)

    return json.dumps(records)
