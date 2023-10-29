import spotipy
from spotipy import util


def get_spotify():
    scope = ["user-modify-playback-state", "user-read-playback-state"]
    redirect_uri = "https://xxz123.notexist.local"
    show_dialog = "true"

    token = util.prompt_for_user_token(
        scope=scope, redirect_uri=redirect_uri, show_dialog=show_dialog
    )

    spotify = spotipy.Spotify(auth=token)

    return spotify


def play_tracks(spotify, track_uris, shuffle=True):
    spotify.shuffle(state=shuffle)

    # DM wants the mood to change almost immediately, not at completion
    # of currently playing track.
    spotify.start_playback(uris=track_uris)


def play_playlist(spotify, playlist_uri, shuffle=True):
    spotify.shuffle(state=shuffle)
    spotify.start_playback(context_uri=playlist_uri)


def next_track(spotify):
    spotify.next_track()
