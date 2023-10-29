from musiccontrol import __main__


def test_take_input_returns_lowercase(monkeypatch):
    # monkeypatch the "input" function, so that it returns "N".
    # This simulates the user entering "N" in the terminal:
    monkeypatch.setattr("builtins.input", lambda _: "N")

    # go about using input() like you normally would:
    result = __main__.take_input()
    assert result == "n"


# def test_play_social_intrigue_music():
#     result = __main__.play_social_intrigue_music()
#     print("result is: ", result)
#     assert result["genre"] == "social intrigue"
