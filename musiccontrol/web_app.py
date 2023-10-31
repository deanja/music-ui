from flask import Flask
from musiccontrol import controller


app = Flask(__name__)


@app.route("/")
def index():
    return "Music Control"


@app.route("/next")
def next_track():
    controller.next_track()
    return "Skipped to next track."


@app.route("/mood/play/<mood_id>")
def play_mood(mood_id):
    controller.play_mood(mood_id)
    return "Playing: %s" % mood_id
