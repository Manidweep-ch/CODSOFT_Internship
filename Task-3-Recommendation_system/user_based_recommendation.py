import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load ratings dataset
# Rows -> Users
# Columns -> Movies
# Values -> Ratings (0 means not watched)
df = pd.read_csv("ratings.csv",index_col=0)

# Calculate similarity between users
similarity = cosine_similarity(df)

# Store usernames for easy indexing
users = list(df.index)


def most_similar_user(username):
    """
    Find the top 3 users most similar to the given user.
    Returns:
    [
        [similarity_score, username],
        ...
    ]
    """

    user_index = users.index(username)

    similar_users = []

    for i, score in enumerate(similarity[user_index]):

        # Skip self-comparison
        if i == user_index:
            continue

        # Ignore very weak similarities
        if score >= 0.1:
            similar_users.append([score, users[i]])

    # Sort by similarity score in descending order
    similar_users.sort(reverse=True)

    # Return top 3 similar users
    return similar_users[:3]


def recommend_movies(username):
    """
    Recommend movies using collaborative filtering.

    Logic:
    1. Find top 3 similar users.
    2. Find movies not watched by current user.
    3. Calculate recommendation score:
         similarity * rating
    4. Return top 3 recommendations.
    """

    similar_users = most_similar_user(username)

    recommendations = {}

    for movie in df.columns:

        # Skip movies already watched
        user_rating = df.loc[username, movie]

        if user_rating != 0:
            continue

        score = 0

        # Calculate weighted recommendation score
        for similar_user in similar_users:

            similarity_score = similar_user[0]
            similar_username = similar_user[1]

            similar_user_rating = df.loc[
                similar_username,
                movie
            ]

            score += (
                similarity_score
                * similar_user_rating
            )

        recommendations[movie] = score

    # Sort recommendations by score
    rec_list = sorted(
        recommendations.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # Return only movie titles
    rec_list = [movie for movie, score in rec_list]

    return rec_list[:3]


# Example Usage
while True:
    n=int(input("Choose any user from 1 to 20 or choose 0 to exit"))
    if(n==0):
        break
    if(n>20 or n<1):
        print("Please enter valid User")
        continue

    User="User_"+str(n)
    print("Top Similar Users:")
    sim_u=most_similar_user(User)
    for i,j in enumerate(sim_u):
        print(i+1," ",j[1])

    print("\nTop Recommendations:")
    rec=recommend_movies(User)
    for i,j in enumerate(rec):
        print(i+1," ",j)
