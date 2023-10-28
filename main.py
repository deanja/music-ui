def take_input():
    user_input = input(
        "Choose a music genre to play: [s]ocial_intrigue, [a]nything, [c]ombat. Or e[x]it."
    )
    # doing something with the input
    return user_input

def play_social_intrigue_music():
    print("switching to social intrigue music ...")

    # Select the tracks (or playlist?)

    # Fade out the currently playing track, if any

    # Play the selected tracks

def play_neutral_music():
    raise NotImplementedError

def play_combat_music():
    raise NotImplementedError

if __name__ == "__main__":
    print("Welcome to Music Control.")
    keep_running = True

    while keep_running == True:
        action = take_input()
        match action:
            case "s":
                play_social_intrigue_music()
            case "a":
                play_neutral_music()
            case "c":
                play_combat_music()
            case "x":
                keep_running = False
            case _:
                print("Warning: unkown option selected.")

    print("Exiting.")
