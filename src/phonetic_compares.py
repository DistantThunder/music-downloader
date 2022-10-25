import jellyfish

TITLE_THRESHOLD_LEVENSHTEIN = 2


def match_titles(title_1: str, title_2: str) -> (bool, int):
    distance = jellyfish.levenshtein_distance(title_1, title_2)
    return distance > 1, distance


def match_artists(artist_1, artist_2: str) -> (bool, int):
    if type(artist_1) == list:
        distances = []

        for artist_1_ in artist_1:
            print(artist_1_)
            match, distance = match_titles(artist_1_, artist_2)
            if not match:
                return match, distance

            distances.append(distance)
        return True, min(distances)
    return match_titles(artist_1, artist_2)
