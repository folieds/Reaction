from os import environ as env

class Telegram:
    API_ID = int(env.get("API_ID", "24371796"))
    API_HASH = env.get("API_HASH", "8121c78f4b8b31e88cc2623d1277338d")
    BOT_TOKEN = env.get("BOT_TOKEN", "7377487112:AAHglIWFGUPPNR6N5u7H03KGK3Z3eB58QtQ")
    BOT_USERNAME = env.get("BOT_USERNAME", "luffyleechRobot")
    EMOJIS = [
        "👍", "❤", "🔥", 
        "🥰", "👏", "😁", "🤔",
        "🤯", "😱", "😢",
        "🥶", "🤩",
        "🙏", "👌",
        "🥱", "🥴", "😍", "🤓",
        "❤‍🔥", "🌚", "😐", "💯",
        "🤣", "⚡", "🏆",
        "🤨", "😐", "😡",
        "👅", "🆒", "😈",
        "😴", "😭", "👻", "⚡",
        "👨‍💻", "👀", "🎃", "🙄",
        "😇", "😨", "🤝",
        "🤗", "🫡", "🎅", "🥸",
        "🤫", "😶‍🌫", "🤪", "😏",
        "😘", "👾", "🤷‍♂", "😎"
    ]

LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'pyrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
