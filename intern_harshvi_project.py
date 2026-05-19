

import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv("movies.csv")



movies['genres'] = movies['genres'].fillna('')
movies['genres'] = movies['genres'].str.replace('|', ' ', regex=False)

# Convert genres into vectors
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['genres']).toarray()

# Calculate similarity
similarity = cosine_similarity(vectors)



def recommend(movie_name):

    movie_name = movie_name.lower()

    movies['title_lower'] = movies['title'].str.lower()

    # Check if movie exists
    if movie_name not in movies['title_lower'].values:
        return ["Movie not found"]

    # Get movie index
    index = movies[movies['title_lower'] == movie_name].index[0]

    # Get similarity scores
    distances = similarity[index]

    # Sort movies based on similarity
    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommendations = []

    for i in movie_list:
        recommendations.append(movies.iloc[i[0]].title)

    return recommendations



st.set_page_config(page_title="Movie Recommender", page_icon="🎬")

st.title("🎬 Movie Recommendation System")

st.write("Select a movie and get top 5 recommendations.")

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Choose a movie",
    movie_list
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    st.subheader("Top 5 Recommended Movies")

    for movie in recommendations:
        st.write("✅", movie)



st.write("-----------------------------------")
st.write("Built using Python, Sklearn & Streamlit")