"""Prediction of users based on tweet vectors"""
# np.vstack is like concat but stacks on list on top of another
import numpy as np
from sklearn.linear_model import LogisticRegression
from .models import User
from .twitter import vectorize_tweet

def predict_user(user0_name, user1_name, hypo_tweet_text):
    """
    Determines and returns which user 
    is more likely to say a given tweet.

    Example Run: predict_user("elonmusk", "jackblack", "Tesla Cars are cool")
    Returns either 0 (user0_name) or 1 (user1_name)
    """


    # Grabbing users form our DB - need to exist
    user0 = User.query.filter(User.name == user0_name).one()
    user1 = User.query.filter(User.name == user1_name).one()

    # Grab vectors from the tweets attribute
    user0_vects = np.array([tweet.vect for tweet in user0.tweets])
    user1_vects = np.array([tweet.vect for tweet in user1.tweets])

    # Vertically stack tweet vectors on top of each other
    vects = np.vstack([user0_vects, user1_vects])
    
    # Creating a list of labels the same length as user0 tweets + user1 tweets
    labels = np.concatenate(
        [np.zeros(len(user0.tweets)), np.ones(len(user1.tweets))])

    # Creating instance and training model
    log_reg = LogisticRegression().fit(vects, labels)

    # Creating vectors for hypothetical tweet parameter
    hypo_tweet_vect = vectorize_tweet(hypo_tweet_text).reshape(1, -1)
    return log_reg.predict(hypo_tweet_vect)


