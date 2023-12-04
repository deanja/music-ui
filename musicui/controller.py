import logging
from musicui.data.moods import MOODS
from musicui.spotify import player


def next_track():
    """Skip playback forward to next track."""
    player.next_track()


def play_mood(mood_id: str) -> bool:
    """Play music for a given mood.
    
    Args:
        mood_id: String key for the mood of music to play, for example, "combat".

    Returns:
        Boolean, whether the mood could be played.

    Raises:
        KeyError: If the mood_id is not configured.
    """

    try:
        mood_config = MOODS[mood_id]
    except KeyError as error:
        logging.error("Mood: \"%s\" not found in configuration.", mood_id)
        raise error

    logging.debug("Requested mood config: %s", mood_config)

    shuffle = mood_config["shuffle"]
    context_uri = mood_config["spotify_context_uri"]

    result = player.play_selection(context_uri=context_uri, shuffle=shuffle
    )
    if result.is_success:
        # todo: add mood description.
        logging.info("Playing mood: %s with context_uri: %s", mood_id, mood_config["spotify_context_uri"])
        return True
    else:
        logging.warn("Problem: %s", result.message)
        return False
