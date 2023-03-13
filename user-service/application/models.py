from . import db
from datetime import datetime
from flask_login import UserMixin
from passlib.hash import sha256_crypt


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), unique=False, nullable=True)
    last_name = db.Column(db.String(255), unique=False, nullable=True)
    password = db.Column(db.String(255), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    authenticated = db.Column(db.Boolean, default=False)
    api_key = db.Column(db.String(255), unique=True, nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def encode_api_key(self):
        self.api_key = sha256_crypt.hash(self.username + str(datetime.utcnow))

    def encode_password(self):
        self.password = sha256_crypt.hash(self.password)

    def __repr__(self) -> str:
        return '< User %r >' % self.username

    def to_json(self):
        return {
            'First Name': self.first_name,
            'Last Name': self.last_name,
            'UserName': self.username,
            'Email': self.email,
            'Id': self.id,
            'API_KEY': self.api_key,
            'is_active': True,
            'is_admin': self.is_admin
        }
