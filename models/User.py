from app import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = True, nullable=False)
    password = db.Column(db.String(10), nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __str__(self):
        return self.name

class UserSchema(ma.Schema):
    class Meta:
        fields = ['name', 'password']

user_schema = UserSchema()
users_schema = UserSchema(many=True)