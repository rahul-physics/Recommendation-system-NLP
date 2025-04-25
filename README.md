# 🎬 Movie Recommendation System

An innovative **Content-Based Movie Recommendation System** that suggests similar movies based on user input. This end-to-end project extracts and processes multiple movie features, generates custom tags, and uses **CountVectorizer** and **Cosine Similarity** to deliver high-quality recommendations. The system is deployed with an interactive user interface using **Streamlit**.

---

## 🚀 Features

- **Extracted and Engineered Features:** Processes movie metadata to create robust feature sets.
- **Custom Movie Tags:** Generates custom tags by combining multiple movie features.
- **Text Vectorization:** Uses **CountVectorizer** to transform movie tags into numeric vectors.
- **Cosine Similarity Computation:** Calculates similarity between movies to recommend the top 5 similar movies.
- **Interactive UI:** Deployed with **Streamlit** for a user-friendly, interactive experience.

---

## 🛠️ Tech Stack

- **Python**
- **Pandas, NumPy**
- **Scikit-learn** (for CountVectorizer and Cosine Similarity)
- **Streamlit** (for UI deployment)

---

## 💡 How It Works

- **Feature Engineering:** Merges genres, cast, director, and keywords into a single tag for each movie.
- **Text Vectorization:** Applies CountVectorizer to convert text tags into numeric vectors.
- **Similarity Calculation:** Uses cosine similarity to identify the most similar movies.
- **Interactive Deployment:** A Streamlit-powered interface allows users to input a movie name and receive recommendations.

