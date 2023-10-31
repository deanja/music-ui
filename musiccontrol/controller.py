from musiccontrol.data.moods import moods
from musiccontrol.spotify import player


spotify = None


def get_spotify():
    """Lazy initialise Spotify."""
    global spotify
    if spotify == None:
        spotify = player.get_spotify()
    return spotify


def next_track():
    player.next_track(get_spotify())


def play_mood(mood_id):
    """Play music for a given mood"""

    mood_config = moods[mood_id]

    shuffle = mood_config["shuffle"]
    context_uri = mood_config["spotify_context_uri"]

    result = player.play_selection(
        get_spotify(), context_uri=context_uri, shuffle=shuffle
    )
    if result.is_success:
        # todo: add mood description.
        print("Playing: ", mood_id)
    else:
        print("Problem: ", result.message)
