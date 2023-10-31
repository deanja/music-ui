from musiccontrol.data.moods import moods
from musiccontrol import controller


def take_input():
    """Take input from the user on console."""
    user_input = input(
        "Choose a music mood to play: [s]ocial_intrigue, [a]nything, [c]ombat, celtic_[b]angers. [n]ext_track or e[x]it. "
    )
    return user_input.lower()


def run():
    keep_running = True

    while keep_running == True:
        input_string = take_input()
        match input_string:
            # App control
            case "x":
                keep_running = False
                break

            # Music player control - general
            case "n":
                controller.next_track()

            case _:
                # Assume a mood was selected
                try:
                    # reverse lookup the config to find the mood id by its ui_key.
                    mood_id = next(
                        key
                        for key, value in moods.items()
                        if value["ui_key"] == input_string
                    )
                except StopIteration:
                    print("Unkown option selected:", input_string)
                else:
                    controller.play_mood(mood_id)
