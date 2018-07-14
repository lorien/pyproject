GRAB_SPIDER_CONFIG = {
    'global': {
        'spider_modules': [
            'spider.{{ cookiecutter.project_name }}',
        ],
        #'cache': {
        #    'backend': 'mongodb',
        #    'database': '{{ cookiecutter.project_name }}_cache',
        #},
        'proxy_list': {
        #    'source': '/web/proxy.txt',
        #    'source_type': 'text_file',
        },

    },
}

MONGODB = {
    'connection': {},
    'dbname': '{{ cookiecutter.project_name }}',
}

try:
    from project.settings_local import *
except ImportError:
    pass
