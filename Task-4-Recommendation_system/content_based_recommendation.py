import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("top_movies.csv")

# Create tags used for vectorization
df["tags"] = (df["genre"] + " "+ df["description"])

# Convert movie features into TF-IDF vectors
tfidf = TfidfVectorizer()
vectors = tfidf.fit_transform(df["tags"])

# Calculate similarity matrix
similarity = cosine_similarity(vectors)

def show_movies():
    """
    Display all available movies.
    """
    for i, movie in enumerate(df["movie_name"]):
        print(f"{i + 1}. {movie}")


def find_movie(title):
    """
    Find the index of a movie by title.

    Args:
        title (str): Movie name entered by the user.

    Returns:
        int: Movie index if found, otherwise -1.
    """
    for index, movie in enumerate(df["movie_name"]):
        if movie.lower() == title.lower():
            return index

    print("Movie not found.")
    return -1


def recommendations(ref):
    """
    Generate top 3 movie recommendations.

    Args:
        movie (str): Selected movie title.

    Returns:
        list: Top 3 recommended movies with similarity scores.
    """
    recommended = []

    for i, score in enumerate(similarity[ref]):

        # Skip the selected movie itself
        if i == ref:
            continue

        if score > 0:
            recommended.append([score, df["movie_name"][i]])

    recommended.sort(key=lambda x: x[0],reverse=True)

    return recommended[:3]


show_movies()
while True:

    movie_name = input("\nEnter movie name or type 0 for exit: ")
    if(movie_name=="0"):
        break
    ref=find_movie(movie_name)
    if(ref==-1):
        break
    recommends = recommendations(ref)
    if recommends:
        print("\nTop Recommendations:\n")
    for i, movie in enumerate(recommends):
        print(f"{i + 1}. {movie[1]}")


