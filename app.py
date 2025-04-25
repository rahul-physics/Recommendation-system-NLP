import streamlit as st
import pickle

# Load the movies list and similarity matrix
movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')


def recommend(movie):
    # Get the index of the selected movie
    movie_index = movies[movies['title'] == movie].index[0]
    # Get the similarity scores for the selected movie
    distances = similarity[movie_index]
    # Sort the movies based on similarity scores
    movie_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    # Create a list of recommended movie titles
    recommended_movies = []
    for i in movie_indices:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


# Select a movie from the dropdown
selected_movie_name = st.selectbox(
    'Please select your movie',
    movies_list
)

# Recommend movies when the button is clicked
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for rec in recommendations:
        st.write(rec)

