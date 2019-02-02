from pprint import pprint
from urllib.parse import quote_plus, urlsplit, urljoin
from datetime import datetime

from grab.spider import Spider, Task
from grab import Grab
from weblib.error import DataNotValid

from project.database import db


class {{ cookiecutter.project_name.title().replace('_', '') }}Spider(Spider):
    def task_generator(self):
        pass
