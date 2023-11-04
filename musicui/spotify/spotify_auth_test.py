# Manually test spotipy functions that require authorised user.

import spotipy
from spotipy import util
from pprint import pprint

if __name__ == "__main__":
    scope = ["user-modify-playback-state", "user-read-playback-state"]
    show_dialog = "true"

    auth_manager = spotipy.SpotifyOAuth(scope=scope, show_dialog=show_dialog)
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    # Informaton about the current user.
    me = spotify.me()
    pprint(me)
