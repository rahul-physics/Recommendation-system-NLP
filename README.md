🎬 Movie Recommendation System
An innovative Content-Based Movie Recommendation System that suggests similar movies based on user input. This end-to-end project extracts and processes multiple movie features, generates custom tags, and uses CountVectorizer and Cosine Similarity to deliver high-quality recommendations. The system is deployed with an interactive user interface using Streamlit.

🚀 Features
Extracted and engineered features from movie metadata

Designed custom movie tags using multiple features

Vectorized movie tags using CountVectorizer

Computed Cosine Similarity to find and recommend top 5 similar movies

Deployed a fully interactive and user-friendly UI using Streamlit

🛠️ Tech Stack
Python

Pandas, NumPy

Scikit-learn (CountVectorizer, Cosine Similarity)

Streamlit (for UI deployment)

💡 How It Works
Feature Engineering: Merges genres, cast, director, and keywords into a single tag for each movie.

Text Vectorization: Applies CountVectorizer to convert text tags into numeric vectors.

Similarity Calculation: Uses cosine_similarity to find the most similar movies.

Interactive Deployment: Streamlit provides an intuitive UI for users to input a movie and receive suggestions.
