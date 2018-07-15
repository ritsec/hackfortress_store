from store.models import User
from store import db

db.create_all()
user = User(username='test', team='blue')
user.set_password('test')
db.session.add(user)
db.session.commit()
