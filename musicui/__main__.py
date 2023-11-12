import sys
import os
import logging
from dotenv import load_dotenv
from musicui.data.moods import MOODS
from musicui import console_app, web_app

load_dotenv()

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(level=LOG_LEVEL)

SUPPORTED_RUN_MODES = ["CONSOLE", "WEB"]
DEFAULT_RUN_MODE = "CONSOLE"


def check_config():
    """Check for errors in user configuration settings"""
    if not isinstance(MOODS, dict):
        raise RuntimeError("Invalid moods config - must be a dictionary.")


def get_run_mode():
    run_mode = None

    if len(sys.argv) > 1:
        run_mode = sys.argv[1].upper()
    elif os.getenv("RUN_MODE"):
        run_mode = os.getenv("RUN_MODE").upper()
    else:
        run_mode = DEFAULT_RUN_MODE

    if run_mode in SUPPORTED_RUN_MODES:
        return run_mode
    else:
        logging.exception("Invalid run mode.")
        raise Exception("'%s' is not a supported run mode." % run_mode)


if __name__ == "__main__":
    print("Welcome to Music Control.")

    check_config()

    match get_run_mode():
        case "WEB":
            flask_host = os.getenv("HOSTNAME", None)
            flask_port = os.getenv("PORT", None)

            logging.debug(
                "Running app as web server on hostname: %s, port:%s.",
                flask_host,
                flask_port,
            )

            web_app.app.run(host=flask_host, port=flask_port)
        case "CONSOLE":
            logging.info("Running app as console.")
            console_app.run()
        case other:
            logging.exception("Could not determine run mode.")
            raise Exception("Could not determine run mode.")

logging.info("Exiting.")
