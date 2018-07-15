from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from store import db
from store import lm

class User(UserMixin, db.Model):
    """ User class """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    team = db.Column(db.String(4))

    def set_password(self, password):
        """ hashes a password and sets the users hash to the new password """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """ confirms a password matches the hash """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(id))
