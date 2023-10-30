from musiccontrol.data.moods import moods
from musiccontrol.spotify import player


def take_input():
    user_input = input(
        "Choose a music mood to play: [s]ocial_intrigue, [a]nything, [c]ombat, celtic_[b]angers. [n]ext_track or e[x]it. "
    )
    # doing something with the input
    return user_input.lower()


def play_mood(mood_id, spotify):
    playlist_uri = None
    track_uris = None

    mood_config = moods[mood_id]

    # todo: support track_uris
    shuffle = mood_config[1]
    playlist_uri = mood_config[3]

    result = player.play_selection(spotify, playlist_uri=playlist_uri, shuffle=shuffle)
    if result.is_success:
        # todo: add mood description.
        print("Playing: ", mood_id)
    else:
        print("Problem: ", result.message)


def check_config():
    if not isinstance(moods, dict):
        raise RuntimeError("Invalid moods config - must be a dictionary.")


if __name__ == "__main__":
    print("Welcome to Music Control.")

    check_config()

    keep_running = True

    spotify = player.get_spotify()

    while keep_running == True:
        input_string = take_input()
        match input_string:
            # App control
            case "x":
                keep_running = False
                break

            # Music player control - general
            case "n":
                player.next_track(spotify)

            case _:
                # Assume a mood was selected
                try:
                    # reverse lookup the config to get mood id for the input string
                    mood_id = next(
                        key for key, value in moods.items() if value[0] == input_string
                    )
                except StopIteration:
                    print("Unkown option selected:", input_string)
                else:
                    play_mood(mood_id, spotify)

    print("Exiting.")
