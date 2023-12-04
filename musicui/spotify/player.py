import logging
from musicui import config
import spotipy
from collections import namedtuple

Result = namedtuple("Result", ["is_success", "message"])

spotify = None

def get_spotify() -> spotipy.Spotify:
    """Get an authenticated Spotify client using lazy initialisation."""

    global spotify
    if spotify != None:
        logging.debug("Got existing instance of spotipy.Spotify")
        return spotify
    else:
        scope = ["user-modify-playback-state", "user-read-playback-state"]

        auth_manager = spotipy.SpotifyOAuth(
            client_id=config.Config().spotify.client_id.get_secret_value(),
            client_secret=config.Config().spotify.client_secret.get_secret_value(),
            redirect_uri=str(config.Config().spotify.redirect_uri),
            scope=scope,
        )
        spotify = spotipy.Spotify(auth_manager=auth_manager)

        logging.debug("Got new instance of spotipy.Spotify.")
        return spotify


def play_selection(context_uri, shuffle=True):
    """Play a Spotify playlist, artist or album."""

    # For etiquette, if there's no active device, don't activate one, as
    # the user may then get sound in an unexpected place. Instead, ask them
    # to activate device.
    if get_spotify().current_playback() == None:
        return Result(
            False, "No device active. Press Play on any Spotify device and try again."
        )

    if context_uri == None:
        return Result(False, "No content (playlist, artist or album) selected.")

    get_spotify().shuffle(state=shuffle)

    # Change playback now, not at completion of current track.
    # todo: implement a fade of any currently playing track for a few seconds, if the
    # device supports volume adjustment.
    get_spotify().start_playback(context_uri=context_uri)
    logging.debug("Started playback of: ", context_uri)

    return Result(True, "New selection now playing.")


def next_track():
    """Start playing next track."""
    get_spotify().next_track()
    logging.debug("Skipped to next track")
