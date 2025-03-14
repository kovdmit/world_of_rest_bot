import logging
from enum import Enum

import colorlog


log = logging.getLogger()
log.setLevel(logging.INFO)
formatter = colorlog.ColoredFormatter(
    '%(asctime)s - %(log_color)s%(levelname)s%(reset)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
log.addHandler(handler)


class Color(Enum):
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'


def color_text(text, color: Color):

    return f'{color.value}{text}{Color.RESET.value}'
