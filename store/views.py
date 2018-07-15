from flask import render_template
from flask import Blueprint
from flask import redirect
from flask_login import login_required
from flask_login import login_user
from .forms import LoginForm
from .models import User

VIEWS = Blueprint('views', __name__)

@VIEWS.route('/')
def index():
    return render_template('index.html')

@VIEWS.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect('views.login')
        login_user(user)
        return redirect('views.index')
    return render_template('login.html')

@VIEWS.route('/store')
@login_required
def store():
    return render_template('store.html')

@VIEWS.route('/admin')
@login_required
def admin():
    return render_template('admin.html')

def order():
    pass

# may not be implementeed
def ctf():
    pass
