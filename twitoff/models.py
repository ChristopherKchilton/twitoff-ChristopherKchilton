"""SQLAlchemy models (schema) for twitoff"""
# Models in DS run datapredictions
# Models in WebDev are associated with databases. How the database looks
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

# Creates User Table
# Similar to saying 'CREATE TABLE user ...' in SQL
class User(DB.Model):
    """Twitter Users corresponding to tweets table"""
    # creating id column (primary key)
    id = DB.Column(DB.BigInteger, primary_key=True) # id column (primary key)
    name = DB.Column(DB.String, nullable=False) # name column
    # newest_tweet_id = DB.Column(DB.BigInteger)

    def __repr__(self):
        return f"<User: {self.name}>"


# Creates Tweet Table
# Similar to saying 'CREATE TABLE tweet ...' in SQL
class Tweet(DB.Model):
    """Tweet text and data"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    # Pickletype is a serialization type
    vect = DB.Column(DB.PickleType, nullable=False)
    #This user references the user.id column which is made lowercase
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'))
    # This User references the Class
    user = DB.relationship("User", backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return f"<Tweet: {self.name}>"


# """SQLAlchemy models (schema) for twitoff"""
# from flask_sqlalchemy import SQLAlchemy
# DB = SQLAlchemy()
# # Creates User Table
# # Similar to saying `CREATE TABLE user ...` in SQL
# class User(DB.Model):
#     """Twitter Users corresponding to tweets table"""
#     # creating id column (primary key)
#     id = DB.Column(DB.BigInteger, primary_key=True)
#     name = DB.Column(DB.String, nullable=False)

#     def __repr__(self):
#         return f"<User: {self.name}>"

# # Creates Tweet Table
# # Similar to saying `CREATE TABLE tweet ...` in SQL
# class Tweet(DB.Model):
#     """Tweet text and data"""
#     id = DB.Column(DB.BigInteger, primary_key=True)
#     text = DB.Column(DB.Unicode(300))
#     user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'))
#     user = DB.relationship("User", backref=DB.backref('tweets', lazy=True))

#     def __repr__(self):
#         return f"<User: {self.text}>"