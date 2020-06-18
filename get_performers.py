def stars(movies, tvshows):
    """
    Takes in two dictionaries, `movies` and `tvshows`, which contains values of
    names of performers. Returns a new dictionary with the performers' names as the keys,
    and the movies and TV shows as the values, sorted alphabetically.
    """
    new_dict = {}

    for (movie, actors) in movies.items():
        for actor in actors:
            if actor in new_dict:
                new_dict[actor].append(movie)
            else:
                new_dict[actor] = [movie]
    for (tv_show, performers) in tvshows.items():
        for performer in performers:
            if performer in new_dict:
                new_dict[performer].append(tv_show)
            else:
                new_dict[performer] = [tv_show]
    for value in new_dict.values():
        value.sort()

    return new_dict


# sample values
movies = {
    "How to Be Single": ["Alison Brie", "Dakota Johnson", "Rebel Wilson"],
    "The Lego Movie": ["Will Arnett", "Elizabeth Banks", "Alison Brie", "Will Ferrell"],
}
tvshows = {
    "Community": [
        "Alison Brie",
        "Joel McHale",
        "Danny Pudi",
        "Yvette Brown",
        "Donald Glover",
    ],
    "30 Rock": [
        "Tina Fey",
        "Tracy Morgan",
        "Jack McBrayer",
        "Alec Baldwin",
        "Elizabeth Banks",
    ],
    "Arrested Development": ["Jason Bateman", "Will Arnett", "Portia de Rossi"],
}

print(stars(movies, tvshows))
