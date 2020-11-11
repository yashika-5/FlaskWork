# users/view.py

from flask import render_template,request,Blueprint, redirect, url_for,flash
from flask_login import login_user, logout_user, current_user, login_required
from peoplecompanyblog import db
from peoplecompanyblog.models import User, BlogPost
from peoplecompanyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from peoplecompanyblog.users.picture_handler import add_profile_pic

users = Blueprint('user',__name__)


#REGISTER
@users.route('/register',methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration.')
        return redirect(url_for('user.login'))

    return render_template('register.html',form=form)


#LOGIN
@users.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:

            login_user(user)
            flash('Login Successfully')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
               next = url_for('core.index')
            return redirect(next)

    return render_template('login.html',form=form)


#LOGOUT
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("core.index"))

#update UserForm
@users.route('/account',methods=['GET','POST'])
@login_required
def account():

    form = UpdateUserForm()

    if form.validate_on_submit():

        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data,username)
            current_user.profile_image = pic

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash(f"{User.id} Account Updated")
        redirect(url_for('core.index'))

    profile_image = url_for('static',filename='profile_pics/'+current_user.profile_image)

    return render_template('account.html',profile_image=profile_image,form=form)


@users.route("/<username>")
def user_posts(username):
    page = request.args.get('page',1,type=int)
    user = User.query.filter_by(username=username).first_or_404()
    blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    return render_template('user_blog_posts.html',blog_posts=blog_posts,user=user)