# music-ui

Novel ways to control music playback without losing your flow.

# Overview
Did you ever open your phone to change what's playing on Spotify, only to be distracted by a notification about a new podcast, or an email from your accountant! music-ui supports using dedicated software or hardware to change what's playing without losing your flow.

Use cases:
- Running a Dungeons & Dragons campaign
- Cooking, gardening, coding
- Hosting a party

The app has been used for:
- playing Spotify playlists by placing different Lego character figures on the back of a mobile phone. (The lego figures have RFID tags under their bases).
- choosing Spotify playlists in a console window without leaving VSCode.

The philosophy is to keep each dedicated UI simple.  For example, play a mood/genre , skip to next track, stop playback.  For finer control, whip out yor mobile and use the the existing Spotify apps, and don't forget to text your mother back!

# Installation

1. Install Poetry if you don't have it already.
2. Clone this github repo.
3. From the app's root folder (same as repo root), `poetry install` to install dependencies.

# Configuration

## Core app configuration

See `config.py` for configurable elements and their allowed and default values.

The configuration values are loaded from (in order of precedence):

1. command line arguments
2. environment variables
3. TOML configuration files
4. the defaults in `config.py`

So, for example, command line arguments will override environment variables.

Command line arguments are in the format `--<argname> <argvalue>`, for example, `--log_level DEBUG`, `--web.enabled true`.

Environment variable names require a prefix of `MUSICUI_`, for example `MUSICUI_LOG_LEVEL` is converted to `log_level`. A dot is used for nested names, for example, `MUSICUI_WEB.ENABLED` is converted to `web.enabled`.

TOML file configuration requires this structure in your home directory:

```
├── .musicui
    ├── config.toml
    ├── secrets.toml
```

An example `config.toml` file:
```
log_level = "DEBUG"

[web]
enabled = true
port = 8811

[spotify]
redirect_uri = "https://my-cool-music-app.com"
```

## Spotify configuration

Register an app on [Spotify for Developers](https://developer.spotify.com/). 

music-ui uses Spotipy, which is a Python wrapper for the Spotify Web API. Authentication is via Spotify OAuth2 so music-ui needs values for your Spotify app's:

- `client_id`
- `client_secret`
- `redirect_uri` 

They can be supplied to music-ui in the same way as other music-ui configuration (see above). 
If using TOML files, put the `client_id` and `client_secret` in the `secrets.toml` file 
because they are sensitive fields.

See the Spotipy documentation for more details on those values.

## Music mood and UI configuration

Edit `musicui/moods/moods.py` to map your own `mood_id`s to console keys and playlists.  

If using console mode (see below) also need to edit the input prompts in `musicui/console_app.py` in the `take_input` function.

# Usage

## Console mode

Start the console application with `python -m music-ui`

Then use predefined keyboard keys to play music from your predefined moods/playlists, or to skip to next track.

## Web mode

`python -m music-ui --web.enabled true`

Then hit these endpoints from your own UI hardware/app:

- `/mood/play/<mood_id>` where `<mood_id>` is a mood_id you configured in  `musicui/moods/moods.py`
- `/next` to skip to next track.

# Roadmap

- Stop/resume playback. A must-have feature on any device that controls noise.
- Multiple threads - to handle input from hardware controls built on Raspberry Pi
- Music sources other than Spotify

# Contributing

Feel free to create an issue or submit a PR.

Seeking assistance with:

- unit/integration testing. How to mock service dependencies (Spotipy), and simplify or abstract functions to make them easier to test.

# License

MIT.  Please respect the Spotify for Develpers terms of use.
