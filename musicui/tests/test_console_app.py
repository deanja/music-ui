from musicui import console_app


def test_take_input_returns_lowercase(monkeypatch):
    # monkeypatch the "input" function, so that it returns "N".
    # This simulates the user entering "N" in the terminal:
    monkeypatch.setattr("builtins.input", lambda _: "N")

    # go about using input() like you normally would:
    result = console_app.take_input()
    assert result == "n"
