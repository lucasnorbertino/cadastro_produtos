import os

from src.config.settings import settings

if not os.path.exists(settings.LOG_PATH):
    os.makedirs(settings.LOG_PATH)

log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s [product-registration-api] %(module)s.%(funcName)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "stream": "ext://sys.stdout"
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "formatter": "default",
            "filename": f"{settings.LOG_PATH}/{settings.LOG_FILE_NAME}",
            "when": "midnight",
            "interval": 1,
            "backupCount": 30,
            "encoding": "utf-8"
        }
    },
    "loggers": {
        "fastapi": {
            "level": "INFO",
            "handlers": ["console", "file"],
            "propagate": False
        },
        "uvicorn": {
            "level": "INFO",
            "handlers": [],
            "propagate": False
        },
        "uvicorn.error": {
            "level": "INFO",
            "handlers": [],
            "propagate": False
        },
        "uvicorn.access": {
            "level": "CRITICAL",
            "handlers": [],
            "propagate": False
        }
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO"
    }
}
