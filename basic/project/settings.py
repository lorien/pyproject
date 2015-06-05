GRAB_SPIDER_CONFIG = {
    'global': {
        'spider_modules': [
            'spider.{{ PROJECT_NAME }}',
        ],
    },
}

MONGODB_CONNECTION = {}
MONGODB_NAME = '{{ PROJECT_NAME }}'

try:
    from project.settings_local import *
except ImportError:
    pass
