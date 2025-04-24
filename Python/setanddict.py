movie_suggestions = {"Movie A", "Movie B", "Movie C", "Movie D", "Movie E", "Movie D" }

movie_details = {
    "Movie A" : 8,
    "Movie B" : 3,
    "Movie C" : 6,
}

movie_suggestions.add("Movie G")
movie_suggestions.remove("Movie E")

print(movie_suggestions)

movie_details["Movie F"] = "7"
movie_details.update({"Movie B": "8"})

print(movie_details["Movie A"])

friend_suggestions = {"Movie G", "Movie H", "Movie I"}

common_suggestions = movie_suggestions.intersection(friend_suggestions)
print(common_suggestions)