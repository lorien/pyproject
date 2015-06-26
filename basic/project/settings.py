GRAB_SPIDER_CONFIG = {
    'global': {
        'spider_modules': [
            'spider.{{ PROJECT_NAME }}',
        ],
        #'cache': {
        #    'backend': 'mongo',
        #    'database': '{{ PROJECT_NAME }}_cache',
        #},
        #'proxy_list': {
        #    'source': '/web/proxy.txt',
        #    'source_type': 'text_file',
        #},

    },
}

MONGODB_CONNECTION = {}
MONGODB_NAME = '{{ PROJECT_NAME }}'

try:
    from project.settings_local import *
except ImportError:
    pass
