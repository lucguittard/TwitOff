"""Main application for twitoff"""
#imports
from decouple import config
from flask import Flask, render_template, request
from .models import DB, User
from .twitter import add_or_update_user
def create_app():
    """create and configures an instance of a flask app"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')
    #app.config['ENV'] = config('ENV') #should change this later to production
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
    DB.init_app(app)
    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title='Home', users=users)
    @app.route('/user', methods=['POST','GET'])
    @app.route('/user/<name>', methods=['GET'])
    def user(name=None,message=''):
        try:
            if request.method == 'POST':
                add_or_update_user(name)
                message = "User {} successfully added!".format(name)
            tweets = User.query.filter(User.name == name).one().tweets
        except Exception as e:
            message = "Error adding {}: {}".format(name,e)
            tweets=[]
        return render_template('user.html', title=name, tweets=tweets,
        message=message)
    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='DB Reset', users=[])
    return app
#Collapse



