import sys
import logging
from musicui.data.moods import moods
from musicui import console_app, web_app


def check_config():
    """Check for errors in user configuration settings"""
    if not isinstance(moods, dict):
        raise RuntimeError("Invalid moods config - must be a dictionary.")


if __name__ == "__main__":
    print("Welcome to Music Control.")

    check_config()

    if len(sys.argv) > 1:
        if sys.argv[1] == "web":
            # Flask web server seems to need specific host IP when Windows ports are
            # explicitly forwarded to WSL2.
            flask_host = "172.21.187.50"
            flask_port = 8811

            logging.info("Running app as web server.")
            web_app.app.run(host=flask_host, port=flask_port)
        else:
            logging.exception("Invalid command line argument.")
            raise LookupError(
                "'%s' is not a valid command line argument." % sys.argv[1]
            )
    else:
        logging.info("Running app as console.")
        console_app.run()

logging.info("Exiting.")
