# """
# Main app/routing file for Twitoff.
# The File that holds the function 'create_app'
# to collect our modules and ourganize the flask app.
# """

# from os import getenv
# from flask import Flask, render_template, request
# from .twitter import add_or_update_user
# from .predict import predict_user
# from .models import DB, User, Tweet


# def create_app():

#     # initilizes our applicatoin
#     app = Flask(__name__)

#     app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
#     app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#     DB.init_app(app)

#     @app.route("/")
#     def root():
#         """ This will be presented when we visit <BASE_URL>/"""
#         users = User.query.all() # AQL equivalent SELECT * FROM user;
#         return render_template("base.html", title='Home', users=users)

#     @app.route("/compare")
#     def compare():
#         """ This will be presented when we visit <BASE_URL>/compare"""
#         user0, user1 = sorted([
#             request.values["user0"], request.values["user1"]])

#         if user0 == user1:
#             message = "Cannot compare users to themselves!"
        
#         else:
#             prediction = predict_user(user0, user1, request.values["tweet_text"])

#             message = "'{}' is more likely to be said by {} than {}".format(
#                 request.values["tweet_text"],
#                 user1 if prediction else user0,
#                 user0 if prediction else user1
#             )
        
#         return render_template("prediction.html", title="prediction", message=message)
    
#     @app.route("/user")
#     def user():
#         """ This will be presented when we visit <BASE_URL>/user"""


#     @app.route("/reset")
#     def reset():
#         """ This will be presented when we visit <BASE_URL>/reset"""
#         DB.drop_all()
#         DB.create_all()
#         insert_example_users()
#         return render_template("base.html", title="The DB has been Reset")

#     @app.route("/update")
#     def update():
#         users = User.query.all()
#         for user in users:
#             add_or_update_user(user.name)
#         return render_template("base.html", title="All the users have been updated!")

        

#     # @app.route("/say_something")
#     # def say_something():
#     #     """ This will be presented when we visit <BASE_URL>/say_something"""
#     #     return "I am saying something"
    
#     return app




# def insert_example_users():
#     """
#     Will get error if ran twice becaues of duplicate primary keys

#     Not real data - just to play with
#     """
#     add_or_update_user("elonmusk")
#     # elonmusk = User(id=2, name='ElonMusk')
#     # johnwick = User(id=3, name='JohnWick')
#     # marysue= User(id=4, name='MarySue')
#     # DB.session.add(jackblack)
#     # DB.session.add(elonmusk)
#     # DB.session.add(johnwick)
#     # DB.session.add(marysue)
#     DB.session.commit()

"""
Main app/routing file for Twitoff.
The file that holds the function `create_app`
to collect our modules and organize the flask app.
"""
from os import getenv
from flask import Flask, render_template, request
from .twitter import add_or_update_user
from .predict import predict_user
from .models import DB, User, Tweet


def create_app():
    # initilizes our application
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)

    @app.route("/")
    def root():
        """This will be presented when we visit '<BASE_URL>/ '"""
        users = User.query.all()  # SQL equivalent: `SELECT * FROM user;`
        return render_template("base.html", title='Home', users=users)

    @app.route("/compare", methods=["POST"])
    def compare():
        """This will be presented when we visit '<BASE_URL>/compare '"""
        user0, user1 = sorted(
            [request.values["user0"], request.values["user1"]])
        if user0 == user1:
            message = "Cannot compare users to themselves!"
        else:
            prediction = predict_user(
                user0, user1, request.values["tweet_text"])
            message = "'{}' is more likely to be said by {} than {}".format(
                request.values["tweet_text"],
                user1 if prediction else user0,
                user0 if prediction else user1
            )
        return render_template("prediction.html", title="prediction", message=message)

    @app.route("/user", methods=["POST"])
    @app.route("/user/<name>", methods=["GET"])
    def user(name=None, message=''):
        """This will be presented when we visit '<BASE_URL>/user '"""
        name = name or request.values["user_name"]
        try:
            if request.method == "POST":
                add_or_update_user(name)
                message = "User {} succesfully added!".format(name)
            tweets = User.query.filter(User.name == name).one().tweets
        except Exception as e:
            message = "Error handling {}: {}".format(name, e)
            tweets = []
        return render_template("user.html", title=name,
                               tweets=tweets, message=message)

    @app.route("/reset")
    def reset():
        """This will be presented when we visit '<BASE_URL>/reset '"""
        DB.drop_all()
        DB.create_all()
        users = User.query.all()  # SQL equivalent: `SELECT * FROM user;`
        return render_template("base.html", title='Home', users=users)

    @app.route("/update")
    def update():
        """This will be presented when we visit '<BASE_URL>/update '"""
        users = User.query.all()
        for user in users:
            add_or_update_user(user.name)
        return "All the users have been updated!"
    # @app.route("/say_something")
    # def say_something():
    #     """This will be presented when we visit '<BASE_URL>/say_something '"""
    #     return "I am saying something"
    return app

def insert_example_users():
    """
    Will get error if ran twice because of duplicate primary keys
    Not real data - just to play with
    """
    jackblack = User(id=1, name="JackBlack")
    elonmusk = User(id=2, name="ElonMusk")
    DB.session.add(jackblack)
    DB.session.add(elonmusk)
    DB.session.commit()
