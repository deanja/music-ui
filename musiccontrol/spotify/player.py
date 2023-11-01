import logging
import spotipy
from spotipy import util
from collections import namedtuple

Result = namedtuple("Result", ["is_success", "message"])


def get_spotify():
    """Get an authenticated Spotify client."""
    scope = ["user-modify-playback-state", "user-read-playback-state"]

    auth_manager = spotipy.SpotifyOAuth(scope=scope)
    spotify = spotipy.Spotify(auth_manager=auth_manager)

    logging.debug("Got new instance of spotipy.Spotify.")
    return spotify


def play_selection(spotify, context_uri, shuffle=True):
    """Play a Spotify playlist, artist or album."""

    # For etiquette, if there's no active device, don't activate one, as
    # the user may then get sound in an unexpected place. Instead, ask them
    # to activate device.
    if spotify.current_playback() == None:
        return Result(
            False, "No device active. Press Play on any Spotify device and try again."
        )

    if context_uri == None:
        return Result(False, "No content (playlist, artist or album) selected.")

    spotify.shuffle(state=shuffle)

    # Change playback now, not at completion of current track.
    # todo: implement a fade of any currently playing track for a few seconds, if the
    # device supports volume adjustment.
    spotify.start_playback(context_uri=context_uri)
    logging.debug("Started playback of: ", context_uri)

    return Result(True, "New selection now playing.")


def next_track(spotify):
    """Start playing next track."""
    spotify.next_track()
    logging.debug("Skipped to next track")
