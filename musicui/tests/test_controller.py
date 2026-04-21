import pytest

from musicui import controller


def test_play_mood_raises_key_error_for_unknown_mood():
    with pytest.raises(KeyError):
        controller.play_mood("not_a_mood")
