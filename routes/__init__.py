from flask import request, render_template
from models.User import User, user_schema, users_schema
from app import app

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def create_user():
    name = request.json['name']
    password = request.json['password']
    user = User(name, password)
    user.save()

    return user_schema.jsonify(user)

@app.route('/user', methods=['GET'])
def get():
    users = User.query.all()
    return users_schema.jsonify(users)

@app.route('/user/<id>', methods=['GET'])
def get_one(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

@app.route('/user/<id>', methods=['PUT'])
def edit(id):
    user = User.query.get(id)
    user.name = request.json['name']
    user.password = request.json['password']
    user.save()
    return user_schema.jsonify(user)

@app.route('/user/<id>', methods=['DELETE'])
def delete(id):
    user = User.query.get(id)
    user.delete()
    return ""