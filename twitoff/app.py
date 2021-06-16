"""
Main app/routing file for Twitoff.
The File that holds the function 'create_app'
to collect our modules and ourganize the flask app.
"""

from os import getenv
from flask import Flask, render_template
from .models import DB, User, Tweet
from .twitter import add_or_update_user

def create_app():

    # initilizes our applicatoin
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    DB.init_app(app)

    @app.route("/")
    def root():
        """ This will be presented when we visit <BASE_URL>/"""
        insert_example_users()
        users = User.query.all() # AQL equivalent SELECT * FROM user;
        return render_template("base.html", title='Home', users=users)

    @app.route("/reset")
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template("base.html", title="The DB has been Reset")

    @app.route("/update")
    def update():
        users = User.query.all()
        for user in users:
            add_or_update_user(user)
        return render_template("base.html", title="All the users have been updated!")

        

    # @app.route("/say_something")
    # def say_something():
    #     """ This will be presented when we visit <BASE_URL>/say_something"""
    #     return "I am saying something"
    
    return app




def insert_example_users():
    """
    Will get error if ran twice becaues of duplicate primary keys

    Not real data - just to play with
    """
    add_or_update_user("therock")
    # elonmusk = User(id=2, name='ElonMusk')
    # johnwick = User(id=3, name='JohnWick')
    # marysue= User(id=4, name='MarySue')
    # DB.session.add(jackblack)
    # DB.session.add(elonmusk)
    # DB.session.add(johnwick)
    # DB.session.add(marysue)
    DB.session.commit()

# def insert_example_tweet():
#     """
#     Will get error if ran twice becaues of duplicate primary keys

#     Not real data - just to play with
#     """
#     tweet1 = Tweet(id=1, text="Hello", user_id=1, user="JackBlack")
#     tweet2 = Tweet(id=2, text="Hi!", user_id=2, user="ElonMusk")
#     tweet3 = Tweet(id=3, text="Good Afternoon", user_id=3, user="JohnWick")
#     tweet4 = Tweet(id=4, text="Good Morning", user_id=4, user="MarySue")
#     tweet5 = Tweet(id=5, text="How are you?", user_id=1, user="JackBlack")
#     tweet6 = Tweet(id=6, text="Top of the morning!", user_id=2, user="ElonMusk")
#     DB.session.add(tweet1)
#     DB.session.add(tweet2)
#     DB.session.add(tweet3)
#     DB.session.add(tweet4)
#     DB.session.add(tweet5)
#     DB.session.add(tweet6)
#     DB.session.commit()
# def insert_example_tweets():
#     """
#     Will get error if ran twice becaues of duplicate primary keys

#     Not real data - just to play with
#     """
#     hello = Tweet(id=1, text='This is a tweet.', user_id=1, user='elonmusk')
#     tweet2 = 
