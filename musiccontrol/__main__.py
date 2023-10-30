from musiccontrol.spotify import player


def take_input():
    user_input = input(
        "Choose a music genre to play: [s]ocial_intrigue, [a]nything, [c]ombat, celtic_[b]angers. [n]ext_track or e[x]it. "
    )
    # doing something with the input
    return user_input.lower()


def play_social_intrigue_music(spotify):
    playlist_uri = "https://open.spotify.com/playlist/0L5LqTiW0NOjke9FhsTUyA"
    result = player.play_selection(spotify, playlist_uri, shuffle=True)
    if not result.is_success:
        print(result.message)


def play_celtic_bangers(spotify):
    playlist_uri = "https://open.spotify.com/playlist/3HXdGvoKWYfjd6PxWvYb7D"
    result = player.play_selection(spotify, playlist_uri, shuffle=False)
    if not result.is_success:
        print(result.message)


def play_neutral_music(spotify):
    playlist_uri = "https://open.spotify.com/playlist/4vAFb3x82WjaE6Gqq5Doxm"
    result = player.play_selection(spotify, playlist_uri, shuffle=True)
    if not result.is_success:
        print(result.message)


def play_combat_music(spotify):
    playlist_uri = "https://open.spotify.com/playlist/6FohP6m1ipvNjgllOH4HLt"
    result = player.play_selection(spotify, playlist_uri, shuffle=True)
    if not result.is_success:
        print(result.message)


def fade_out_music():
    raise NotImplementedError


if __name__ == "__main__":
    print("Welcome to Music Control.")
    keep_running = True

    spotify = player.get_spotify()

    while keep_running == True:
        action = take_input()
        match action:
            case "s":
                play_social_intrigue_music(spotify)
            case "a":
                play_neutral_music(spotify)
            case "c":
                play_combat_music(spotify)
            case "b":
                play_celtic_bangers(spotify)
            case "n":
                player.next_track(spotify)
            case "x":
                keep_running = False
            case _:
                print("Warning: unkown option selected.")

    print("Exiting.")
