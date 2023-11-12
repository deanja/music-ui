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

Register an app on [Spotify for Developers](https://developer.spotify.com/) .   

Create a file called `.env` in the app's root folder. Populate your settings.  See `.env_example` file for guidance.

Authentication is via Spotify OAuth2. See the Spotipy documentation. Spotipy is a Pyhon wrapper for the Spotify Web API.

## Music mood and UI configuration

Edit `musicui/moods/moods.py` to map your own `mood_id`s to console keys and playlists.  

If using console mode (see below) also need to edit the input prompts in `musicui/console_app.py` in the `take_input` function.

# Usage

## Console mode

Start the console application with `python -m music-ui`

Then use predefined keyboard keys to play music from your predefined moods/playlists, or to skip to next track.

## Web mode

`python -m music-ui web`

Then hit these endpoints from your own UI hardware/app:
`/mood/play/<mood_id>` where `<mood_id>` is a mood_id you configured in  `musicui/moods/moods.py`

# Roadmap

- Stop/resume playback. A must-have feature on any device that controls noise.
- Multiple threads - to handle input from hardware controls built on Raspberry Pi
- File-based configuration (YAML?)
- Music sources other than Spotify

# Contributing

Feel free to create an issue or submit a PR.

Seeking assistance with:

- unit/integration testing. How to mock service dependencies (Spotipy), and simplify or abstract functions to make them easier to test.

# License

MIT.  Please respect the Spotify for Develpers terms of use.
