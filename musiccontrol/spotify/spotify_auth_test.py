# Manually test spotipy functions that require authorised user.
# 1. Play something on Spotify.
# 2. When this code runs it should make Spotify skip to the next track.

import spotipy
from spotipy import util

if __name__ == "__main__":
    scope = ["user-modify-playback-state", "user-read-playback-state"]
    redirect_uri = "https://xxz123.notexist.local"
    show_dialog = "true"

    token = util.prompt_for_user_token(
        scope=scope, redirect_uri=redirect_uri, show_dialog=show_dialog
    )

    spotify = spotipy.Spotify(auth=token)

    spotify.next_track(device_id=None)
