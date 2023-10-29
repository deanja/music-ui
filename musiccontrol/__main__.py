from musiccontrol.spotify import player


def take_input():
    user_input = input(
        "Choose a music genre to play: [s]ocial_intrigue, [a]nything, [c]ombat, celtic_[b]angers. [n]ext_track or e[x]it."
    )
    # doing something with the input
    return user_input.lower()


def play_social_intrigue_music(spotify):
    # Select the tracks
    track_uris = [
        "spotify:track:6roFHBn0kFsj0H0ud7gSTn",
        "spotify:track:2a75ZwRbjH0HoN2ICXwcfV",
        "spotify:track:3IXjLPOHEnWPqBupP5IlQM",
    ]

    # Play them
    player.play_tracks(spotify, track_uris)

    result = {"genre": "social intrigue", "tracks": len(track_uris)}
    return result


def play_celtic_bangers(spotify):
    playlist_uri = "spotify:playlist:3HXdGvoKWYfjd6PxWvYb7D"

    player.play_playlist(spotify, playlist_uri, shuffle=False)


def play_neutral_music():
    raise NotImplementedError


def play_combat_music():
    raise NotImplementedError


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
                play_neutral_music()
            case "c":
                play_combat_music()
            case "b":
                play_celtic_bangers(spotify)
            case "n":
                player.next_track(spotify)
            case "x":
                keep_running = False
            case _:
                print("Warning: unkown option selected.")

    print("Exiting.")
