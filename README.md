# 🎬 Movie Recommendation System

## Overview
This project is a Movie Recommendation System built using Python, Scikit-learn, and Streamlit. 
It recommends movies based on genre similarity using Machine Learning techniques.

---

## Features
- Select a movie from the dropdown list
- Get top 5 similar movie recommendations
- Interactive web interface using Streamlit
- Uses cosine similarity for recommendations

---

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit

---

## Project Workflow
1. Load movie dataset
2. Preprocess movie genres
3. Convert text into vectors using CountVectorizer
4. Calculate cosine similarity
5. Recommend movies based on similarity scores
6. Display recommendations in Streamlit UI

---

## Installation

### Install Required Libraries
```bash
pip install pandas scikit-learn streamlit
```

---

## Run the Project
```bash
streamlit run app.py
```

---

## Dataset
The project uses a `movies.csv` dataset containing:
- Movie titles
- Genres

---

## Output
The system displays the top 5 recommended movies similar to the selected movie.

---

## Author
harshvi shah
