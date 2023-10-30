import spotipy
from spotipy import util
from collections import namedtuple

Result = namedtuple("Result", ["is_success", "message"])


def get_spotify():
    scope = ["user-modify-playback-state", "user-read-playback-state"]
    redirect_uri = "https://xxz123.notexist.local"
    show_dialog = "true"

    token = util.prompt_for_user_token(
        scope=scope, redirect_uri=redirect_uri, show_dialog=show_dialog
    )

    spotify = spotipy.Spotify(auth=token)

    return spotify


def play_selection(spotify, playlist_uri=None, track_uris=None, shuffle=True):
    # Play selected music on Spotify.
    # Requires either a playlist or list of tracks.

    # For etiquette don't assume we can start playing on an inactive device.
    if spotify.current_playback() == None:
        return Result(
            False, "No device active. Press Play on any Spotify device and try again."
        )

    if playlist_uri == track_uris == None:
        return Result(False, "No playlist or track(s) selected.")

    spotify.shuffle(state=shuffle)

    # Change playback now, not at completion of current track.
    # todo: implement a fade of a few seconds if device supports volume adjustment.
    spotify.start_playback(context_uri=playlist_uri, uris=track_uris)

    return Result(True, "New selection now playing.")


# def play_playlist(spotify, playlist_uri, shuffle=True):
#     spotify.shuffle(state=shuffle)
#     spotify.start_playback(context_uri=playlist_uri)


def next_track(spotify):
    # Start playing next track.
    spotify.next_track()
