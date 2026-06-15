# Movie Recommendation System

## Overview

This project implements two different recommendation system approaches:

1. **Content-Based Recommendation System**
2. **Collaborative Filtering Recommendation System**

The goal of this project was to understand how recommendation engines work and compare different recommendation techniques.

---

## Features

### Content-Based Recommendation

* Recommends movies similar to a selected movie.
* Uses movie genres and descriptions as features.
* Converts text data into numerical vectors using TF-IDF Vectorization.
* Calculates similarity between movies using Cosine Similarity.
* Returns the Top 3 most similar movies.

### Collaborative Filtering Recommendation

* Recommends movies based on user preferences.
* Finds users with similar rating patterns.
* Uses Cosine Similarity to identify similar users.
* Generates recommendations from highly-rated movies of similar users.
* Returns the Top 3 recommended movies.

---

## Technologies Used

* Python
* Pandas
* Scikit-Learn
* TF-IDF Vectorizer
* Cosine Similarity

---

# Approach 1: Content-Based Filtering

## Workflow

Movie Dataset
→ Genre + Description
→ TF-IDF Vectorization
→ Cosine Similarity
→ Movie Recommendations

### Dataset Columns

* movie_name
* genre
* description

### Example

Input:

Interstellar

Output:

1. The Martian
2. Gravity
3. Inception

### Concepts Learned

* Text Vectorization
* Feature Engineering
* TF-IDF
* Cosine Similarity
* Ranking Systems

---

# Approach 2: Collaborative Filtering

## Workflow

User Ratings
→ User Similarity
→ Similar Users
→ Recommendation Score
→ Movie Recommendations

### Dataset Structure

Rows represent users.

Columns represent movies.

Ratings:

* 0 = Not Watched
* 1-5 = User Rating

### Example

User_1 likes:

* RRR
* Pushpa
* Baahubali

The system finds users with similar tastes and recommends movies that those users enjoyed but User_1 has not watched.

### Recommendation Score

The recommendation score is calculated using:

Recommendation Score = Similarity × User Rating

Movies with higher scores are recommended first.

### Concepts Learned

* User-Item Matrix
* Collaborative Filtering
* Similarity Measurement
* Recommendation Ranking

---

## Project Structure

```text
Movie-Recommendation-System/
│
├── content_based_recommendation.py
├── user_based_recomendation.py
├── top_movies.csv
├── ratings.csv
└── README.md
```

---

## How to Run

### Install Dependencies

```bash
pip install pandas scikit-learn
```

### Run Content-Based Recommendation

```bash
python content_based_recommendation.py
```

### Run Collaborative Filtering Recommendation

```bash
python collaborative_filtering.py
```

---

## Learning Journey

This project was developed in multiple phases:

### Phase 1

Implemented a basic recommendation system using genre matching and set intersections.

### Phase 2

Upgraded to a Content-Based Recommendation System using:

* TF-IDF Vectorization
* Cosine Similarity

### Phase 3

Implemented Collaborative Filtering using:

* User Ratings
* User Similarity
* Weighted Recommendation Scores

This progression helped in understanding both movie-based and user-based recommendation techniques.

---

## Future Improvements

* Hybrid Recommendation System
* Larger Movie Dataset
* Movie Posters and GUI
* Web Application Deployment
* Advanced Recommendation Algorithms

---

## Author

Manidweep Chintam

CodSoft Internship Project
