from musiccontrol import __main__


def test_play_social_intrigue_music():
    result = __main__.play_social_intrigue_music()
    print("result is: ", result)
    assert result["genre"] == "social_intrigue"
