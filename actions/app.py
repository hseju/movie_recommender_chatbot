import pandas as pd
import numpy as np
import pickle

# with open("movies_with_genres", "rb") as f:
#     movies_with_genres = pickle.load(f)

# with open("movies_with_genres", "rb") as f:
#     movies_df = pickle.load(f)

movies_with_genres = pd.read_csv("movies_with_genres.csv", encoding="unicode_escape", index_col=0)
movies_df = pd.read_csv("movies_df.csv", encoding="unicode_escape",  index_col=0)

def get_movies(user_input):

    #user_input = user_input +" "
    #lets get the user ratings
    user_ratings = [{'title':user_input, 'rating':5}]

    user_ratings = pd.DataFrame(user_ratings)

    movies = movies_with_genres[movies_with_genres['title'].isin(user_ratings.title.to_list())]

    #create a vector having user profile ratings for different generes based on the user input movies
    user_ratings_profile = movies.iloc[:,4:].reset_index(drop=True).transpose().dot(user_ratings['rating'])


    #Now let's get the genres of every movie in our original dataframe
    genreTable = movies_with_genres.set_index('movieId')

    recommended_score = (((user_ratings_profile*genreTable).sum(axis=1))/user_ratings_profile.sum()).sort_values(ascending=False)

    movies_result = movies_df[movies_with_genres['movieId'].isin(recommended_score.head(100).keys())]
 

    
    return movies_result.sort_values(by="year", ascending=False)['title'].to_list()[:5]




