import sys, os, logging
from musicui import config
from confz import validate_all_configs
from musicui.data.moods import MOODS
from musicui import console_app, web_app


LOG_LEVEL = config.Config().log_level.upper()
logging.basicConfig(level=LOG_LEVEL)


def check_mood_config():
    """Check for errors in user configuration settings"""
    if not isinstance(MOODS, dict):
        raise RuntimeError("Invalid moods config - must be a dictionary.")


if __name__ == "__main__":
    print("Welcome to Music Control.")

    check_mood_config()
    validate_all_configs()

    if config.Config().web.enabled:
        flask_host = config.Config().web.host
        flask_port = config.Config().web.port

        logging.debug(
            "Running app as web server on host: %s, port:%s.",
            flask_host,
            flask_port,
        )

        web_app.app.run(host=flask_host, port=flask_port)
    else:
        logging.info("Running app as console.")
        console_app.run()


logging.info("Exiting.")
