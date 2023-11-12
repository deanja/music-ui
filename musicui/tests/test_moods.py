from musicui.data.moods import MOODS


def test_moods_is_dict():
    assert isinstance(MOODS, dict)
