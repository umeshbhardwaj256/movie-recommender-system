import streamlit as st
import pickle


movies_list = pickle.load(open('movie.pkl', 'rb'))
movie_list = movies_list['title'].values
st.title("Movie Recommender System")

similarity = pickle.load(open('similarity.pkl', 'rb'))

select_movie = st.selectbox("Movies",(movie_list))


def recommanded_movie(movie):
    movie_index = int(movies_list[movies_list['title'] == movie].index[0])
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommanded_movies = []

    for i in movie_list:
        recommanded_movies.append(movies_list.iloc[i[0]].title)

    return recommanded_movies


if st.button("Recommended Movie"):
    # st.write(select_movie)
    recommandation = recommanded_movie(select_movie)
    for i in recommandation:
        st.write(i)